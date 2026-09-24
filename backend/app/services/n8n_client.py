"""HTTP client that calls the n8n customer-message webhook (WF-001)."""

from typing import Any, Optional
import httpx

from app.core.config import settings
from app.core.errors import AppError


class N8nClient:
    def __init__(
        self,
        webhook_url: Optional[str] = None,
        timeout: float = 60.0,
    ):
        self.webhook_url = webhook_url or settings.N8N_WEBHOOK_URL
        self.timeout = timeout
        self.secret = settings.N8N_WEBHOOK_SECRET

    async def process_customer_message(
        self,
        *,
        message: str,
        conversation_id: str,
        customer_id: Optional[str] = None,
        request_id: Optional[str] = None,
        idempotency_key: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        POST validated payload to n8n WF-001 webhook.

        Expected n8n response shape (from API_SPECIFICATION):
        {
          "conversation_id": "...",
          "lead_id": "...",
          "response": "...",
          "processing_status": "SUCCESS"
        }
        """
        payload = {
            "message": message,
            "conversation_id": conversation_id,
            "customer_id": customer_id,
            "request_id": request_id,
            "idempotency_key": idempotency_key,
            "source": "web_chat",
            "channel": "web",
        }

        headers: dict[str, str] = {
            "Content-Type": "application/json",
        }
        if request_id:
            headers["X-Request-ID"] = request_id
        if idempotency_key:
            headers["Idempotency-Key"] = idempotency_key
        if self.secret:
            headers["X-Webhook-Secret"] = self.secret

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                res = await client.post(
                    self.webhook_url,
                    json=payload,
                    headers=headers,
                )
        except httpx.TimeoutException as exc:
            raise AppError(
                code="WORKFLOW_ERROR",
                message="n8n workflow timed out.",
                status_code=504,
                request_id=request_id,
            ) from exc
        except httpx.RequestError as exc:
            raise AppError(
                code="SERVICE_UNAVAILABLE",
                message=f"Could not reach n8n: {exc}",
                status_code=503,
                request_id=request_id,
            ) from exc

        if res.status_code >= 400:
            raise AppError(
                code="WORKFLOW_ERROR",
                message=f"n8n returned HTTP {res.status_code}.",
                status_code=502,
                details=[{"body": _safe_body(res)}],
                request_id=request_id,
            )

        try:
            data = res.json()
        except ValueError as exc:
            raise AppError(
                code="WORKFLOW_ERROR",
                message="n8n returned non-JSON response.",
                status_code=502,
                request_id=request_id,
            ) from exc

        # Support both flat and { data: {...} } wrappers
        if isinstance(data, dict) and "data" in data and isinstance(data["data"], dict):
            data = data["data"]

        if not isinstance(data, dict):
            raise AppError(
                code="WORKFLOW_ERROR",
                message="n8n response must be a JSON object.",
                status_code=502,
                request_id=request_id,
            )

        response_text = data.get("response") or data.get("message") or ""
        if not response_text:
            raise AppError(
                code="WORKFLOW_ERROR",
                message="n8n response missing 'response' field.",
                status_code=502,
                details=[data],
                request_id=request_id,
            )

        return {
            "conversation_id": data.get("conversation_id") or conversation_id,
            "lead_id": data.get("lead_id"),
            "response": response_text,
            "processing_status": data.get("processing_status") or "SUCCESS",
        }


def _safe_body(res: httpx.Response) -> Any:
    try:
        return res.json()
    except Exception:
        return res.text[:500]


n8n_client = N8nClient()
