from fastapi import Depends

from bla import db_plug

class DBCommands:
    def __init__(self, pool: Pool = Depends(db_plug)):
        print(pool) # Depends(db_plug)
        print(type(pool)) # <class 'fastapi.params.Depends'>
        self.pool: Pool = pool
    
    async def get_all_users(self):
        #with pool.acquire() as conn:
        #    ...
