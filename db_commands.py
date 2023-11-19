from main import get_pool

class DBCommands:
    def __init__(self):
        self.pool = get_pool()
    
    async def get_all_users(self):
        #with pool.acquire() as conn:
        #    ...
