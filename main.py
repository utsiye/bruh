import asyncio

from fastapi import FastAPI

from app.misc.logger import logger
from app.settings.config import load_config
from app.services.db.db_models import create_db


def register_all_routes():
    ...

async def main():
    logger.info("Starting app")

    config = load_config(".env")

    pool = await create_db()

    app = FastAPI()
    register_all_routes()



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("App is stopped")
