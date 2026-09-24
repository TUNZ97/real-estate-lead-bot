interface LoadingProps {
  label?: string
}

export default function Loading({ label = 'Loading…' }: LoadingProps) {
  return (
    <div className="loading" role="status" aria-live="polite">
      <span className="loading__dot" />
      <span className="loading__dot" />
      <span className="loading__dot" />
      <span className="sr-only">{label}</span>
    </div>
  )
}
