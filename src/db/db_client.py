from config import DB_CONNECTION_STRING
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker
from db.models import Base, User
from sqlalchemy import select


class DBClient:
    engine = None
    session = None

    def __init__(self):
        if self.engine is None:
            self.engine: AsyncEngine = create_async_engine(DB_CONNECTION_STRING)
            self.session = async_sessionmaker(self.engine, expire_on_commit=False)

    async def insert_user(self, row) -> str:
        row = User(**row.dict())   # convert pydantic model to dict and unpack it
        async with self.session() as session:
            async with session.begin():
                session.add(row)
                await session.commit()
                return row.id

    async def retrieve_all_users(self, entity: Base):
        async with self.session() as session:
            async with session.begin():
                db = await session.execute(select(entity))
                users = db.scalars(entity).all()
                return {"users": users}

    async def retrieve_one_user(self, user_id):
        async with self.session() as session:
            async with session.begin():
                db = await session.execute(select(User).where(User.id == user_id))
                user = db.scalars().first()
                return user

    async def update_user(self, user_id, payload):
        async with self.session() as session:
            async with session.begin():
                user = await session.execute(select(User).where(User.id == user_id))
                user = user.scalar_one()

                for key, value in payload.dict().items():
                    setattr(user, key, value)

                await session.commit()
                return user

    async def delete_user(self, user_id):
        async with self.session() as session:
            async with session.begin():
                user = await session.execute(select(User).where(User.id == user_id))
                user = user.scalar_one()
                await session.delete(user)
                await session.commit()
