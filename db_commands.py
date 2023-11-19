from app.services.db.db_models import create_db

class DBCommands:
    def __init__(self):
        self.pool = await create_db()
    
    async def get_all_users(self):
        #with pool.acquire() as conn:
        #    ...
