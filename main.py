import dotenv
from characterai import aiocai, types
import asyncio
import os
dotenv.load_dotenv(".env")
async def get_answer(text: str):
    char = 'nSgypqXQwOgl1PmBs2AFcCKUezG1Lgjb23i66vOtFdM'

    client = aiocai.Client(os.getenv("TOKEN"))

    me = await client.get_me()

    async with await client.connect() as chat:
        new, answer = await chat.new_chat(
            char, me.id
        )

        message = await chat.send_message(
            char, new.chat_id, text
        )

        return message

