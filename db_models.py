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














import asyncpg

from app.misc.logger import logger
from app.settings.config import load_config

config = load_config()
db_config = config.db


class User:
    def __init__(self, id: str):
        self.id = id

    @staticmethod
    def create_users_db(conn):
        await conn.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    id bigint PRIMARY KEY
                )
            ''')

    def __repr__(self):
        return f"User(id={self.id})"



async def create_db():
    logger.info("Connecting to database")
    conn = await asyncpg.connect(user=db_config.user, password=db_config.password, database=db_config.database,
                                 host=db_config.host)

    # create all db
    User.create_users_db(conn)
    ...

    try:
        yield conn
    finally:
        await conn.close()

