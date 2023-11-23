from fastapi import FastAPI, Depends

from app.services.db.db_commands import DBCommands

async def register_user_route(db: DBCommands = Depends()):
  ...


def register_route(app: FastAPI):
    app.add_route("/register", register_user_route, ['GET'])
