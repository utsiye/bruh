from app.services.db.db_models import User

class DBCommands:
    async def get_all_users(self):
        return await User.query.gino.all()
