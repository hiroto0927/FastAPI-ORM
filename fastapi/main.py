from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.db.database import SessionLocal
from src.router.department import dep_router
from src.router.member import member_router

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def redirect():
    return RedirectResponse("/docs")

app.include_router(dep_router)
app.include_router(member_router)