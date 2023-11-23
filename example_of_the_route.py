from fastapi import FastAPI, Depends

from app.services.db.db_commands import DBCommands
from main import appPlug

db = DBCommands()

async def register_user_route(...):
  ...


def register_route(app: appPlug = Depends()):
    app.add_route("/register", register_user_route, ['GET'])
