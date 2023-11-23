import asyncio
import uvicorn

from fastapi import FastAPI

from app.misc.logger import logger
from app.settings.config import load_config
from app.services.db.db_models import create_db
from app.routers.register import api_router as register_router
from bla import db_plug # пустая функция


def include_all_routers(app):
    app.include_router(register_router)
    ...

async def main():
    logger.info("Starting app")

    config = load_config(".env")

    pool = create_db()
    app = FastAPI()

    app.dependency_overrides[db_plug] = lambda: pool

    include_all_routers(app)

    return app




if __name__ == '__main__':
    try:
        app = asyncio.run(main())
        uvicorn.run(app, host="0.0.0.0", port=80)

    except (KeyboardInterrupt, SystemExit):
        logger.error("API stopped")
