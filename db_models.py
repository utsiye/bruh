import asyncpg

from app.misc.logger import logger
from app.settings.config import load_config

config = load_config()
db_config = config.db


def create_all_tables(pool: asyncpg.Pool):
    with pool.acquire() as conn:
        await conn.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    id bigint PRIMARY KEY
                )
            ''')
        ...


async def create_db() -> asyncpg.Pool:
    logger.info("Connecting to database")
    pool = pool = await asyncpg.create_pool(
        user=db_config.user,
        password=db_config.password,
        database=db_config.database,
        host=db_config.host,
    )

    create_all_tables(pool)

    yield pool

    pool.close()
