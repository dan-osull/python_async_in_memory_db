from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from async_in_memory_db import InMemoryDatabase
from example_data import DB_FILENAME, User

app = FastAPI()
db = InMemoryDatabase()


@app.on_event("startup")
async def setup_db():
    db.setup(DB_FILENAME)


@app.get("/")
async def example_route(session: AsyncSession = Depends(db)) -> list[User]:
    results = await session.execute(select(User))
    return results.scalars().all()
