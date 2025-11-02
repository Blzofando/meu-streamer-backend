from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = 25657270
API_HASH = 'f2d5b9d5c89471989432ef1c2ee22993'

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print("SESSION_STRING =", client.session.save())
