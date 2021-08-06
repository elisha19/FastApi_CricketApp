from fastapi import HTTPException
from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# async def get_query_token(token: str):
#     if token != "apiToken":
#         raise HTTPException(status_code=400, detail="No api token provided")
