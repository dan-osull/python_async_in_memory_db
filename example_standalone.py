import asyncio

from sqlalchemy import select

from async_in_memory_db import InMemoryDatabase
from example_data import DB_FILENAME, User


async def main():
    db = InMemoryDatabase()
    db.setup(DB_FILENAME)
    data = await example_query(db)
    print([item.name for item in data])


async def example_query(db: InMemoryDatabase) -> list[User]:
    async with db.get_session() as session:
        results = await session.execute(select(User))
        return results.scalars().all()


if __name__ == "__main__":
    asyncio.run(main())
