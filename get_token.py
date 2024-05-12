import dotenv
import os
from characterai import pycai, sendCode, authUser
import asyncio

dotenv.load_dotenv(".env")

async def main():
    email = os.getenv("EMAIL")
    #code = sendCode(email)
    #link = input('CODE IN MAIL: ')
    token = "240f5bb373413d1b255f9b293238b3ff03420f27"
    print(token)
    info = await pycai.get_me(token=token)
    print(info)
async def get_chat():
    a = aiocai(token=os.getenv("TOKEN"))
    char = await a.connect.get("nSgypqXQwOgl1PmBs2AFcCKUezG1Lgjb23i66vOtFdM")
    return char
print(asyncio.run(main()))