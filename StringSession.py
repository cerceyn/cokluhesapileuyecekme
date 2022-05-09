import asyncio
from pyrogram import Client


Clients=[]
satir = ""
stringq = ""

API_ID = ""
API_HASH = ""

async def session_olustur():
    API_ID = input("Telegram API ID: ")
    API_HASH = input("Telegram API HASH: ")
    async with Client("userbot", api_id=API_ID, api_hash=API_HASH) as app:
        print('\n\n')
        stringq = await app.export_session_string()
        print(stringq)
        print('\n')
    satir = API_ID + "|" + API_HASH + "|" + stringq

if __name__ == "__main__":
    while True:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(session_olustur())
        with open("hesaplar.txt","w") as file:
            file.write(satir)
        ss = input("\n\n\n[!] Başka bir hesap için string almak ister misiniz ? (y/n)\n> ")
        if not ss in ["y","Y"]:
            print("Güle güle!")
            break
