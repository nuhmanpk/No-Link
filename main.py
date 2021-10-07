import os 
import pyrogram
from pyrogram import Client, filters

bughunter0 = Client(
    "NoLink-BOT",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@bughunter0.on_message(filters.regex("http") | filters.regex("www") | filters.regex("t.me"))
async def nolink(bot,message):
	try:
		await message.delete()
	except:
		return

bughunter0.run()
 	
