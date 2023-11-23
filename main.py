import asyncio
import uvicorn

from fastapi import FastAPI, Depends

from app.misc.logger import logger
from app.settings.config import load_config
from app.services.db.db_models import create_db
from app.services.db.db_commands import DBCommands




async def main():
    logger.info("Starting app")

    config = load_config(".env")

    pool = create_db()
    app = FastAPI()

    db =  DBCommands(pool)
    app.dependency_overrides[DBCommands] = lambda: db

    return app




if __name__ == '__main__':
    try:
        app = asyncio.run(main())
        uvicorn.run(app, host="0.0.0.0", port=80)

    except (KeyboardInterrupt, SystemExit):
        logger.error("API stopped")
