from fastapi import APIRouter, Request
from asyncpg import Pool as Pool

from app.services.db.db_commands import DBCommands
from app.misc.models.user import User
from bla import db_plug

db = DBCommands()
api_router = APIRouter()

@api_router.post('/register/')
async def register_route(user: User) -> dict:
    user = await db.get_or_create_user(login=user.login, password=user.password)
    return user
