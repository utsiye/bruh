from app.services.db.db_models import create_db
from main import poolPlug

from fastapi import Depends

class DBCommands:
    def __init__(self, pool: poolPlug = Depends()):
        self.pool: Pool = pool
    
    async def get_all_users(self):
        #with pool.acquire() as conn:
        #    ...
