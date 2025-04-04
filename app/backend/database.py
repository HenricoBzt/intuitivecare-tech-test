from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from app.backend.settings import Settings

engine = create_async_engine(Settings().DATABASE_URL)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


Base = declarative_base()

async def get_session():
    async with async_session() as session:
        yield session
        
