

class DBCommands:
    def __init__(self, pool: Pool):
        self.pool = pool
    
    async def get_all_users(self):
        #with pool.acquire() as conn:
        #    ...
