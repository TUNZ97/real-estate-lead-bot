"""
Database engine and session factory.

Development uses local MySQL via DATABASE_URL (mysql+pymysql://...).
Phase 1 will uncomment and wire this fully with models + Alembic.
"""

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.core.config import settings
#
# engine = create_engine(
#     settings.DATABASE_URL,
#     pool_pre_ping=True,
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
