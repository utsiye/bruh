from db_commands import DBCommands

db = DBCommands()


@app.get("/bruh/")
async def bruh_():
  users = await db.get_all_users()
  ...
