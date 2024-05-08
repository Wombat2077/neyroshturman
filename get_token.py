import dotenv
import os
from characterai import aiocai, sendCode, authUser
import asyncio

dotenv.load_dotenv(".env")

async def main():
    email = os.getenv("EMAIL")
    code = sendCode(email)
    link = input('CODE IN MAIL: ')
    token = authUser(link, email)
    print(token)
    info = await aiocai.get_me(token=token)
    print(info)
async def get_chat():
    a = aiocai(token=os.getenv("TOKEN"))
    char = await a.connect.get("nSgypqXQwOgl1PmBs2AFcCKUezG1Lgjb23i66vOtFdM")
    return char
print(asyncio.run(get_chat()))