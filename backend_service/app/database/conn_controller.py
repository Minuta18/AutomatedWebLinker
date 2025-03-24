from sqlalchemy import orm
from sqlalchemy.ext import asyncio as asyncsql
from app import DbName

class DBConnectionController:
    def __init__(self, connection_string: str, type: DbName):
        self.connection_string = connection_string
        self.engine = asyncsql.create_async_engine(self.connection_string)
        self.session_maker = asyncsql.async_sessionmaker(
            self.engine, expire_on_commit=False)
        self._session = self.session_maker()
        self.db_type = type

    async def close_connection(self):
        await self._session.close()
        await self.engine.dispose()        
    
    async def create_tables(self, base_model: orm.DeclarativeBase):
        async with self.engine.begin() as conn:
            await conn.run_sync(base_model.metadata.create_all)
    
    async def drop_tables(self, base_model: orm.DeclarativeBase):
        async with self.engine.begin() as conn:
            await conn.run_sync(base_model.metadata.drop_all)
            
    async def get_session(
        self) -> asyncsql.AsyncSession:
        return self._session