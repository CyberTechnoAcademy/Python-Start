from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin
from data_base import sqlite_db

async def on_startup(_):
	sqlite_db.sql_start()

admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
executor.start_polling(dp, skip_updates=True)