from characterai import aiocai
import asyncio
import dotenv
import os
dotenv.load_dotenv(".env")

async def get_answer(text: str, chat_id=None):
    char = 'nSgypqXQwOgl1PmBs2AFcCKUezG1Lgjb23i66vOtFdM'

    client = aiocai.Client(os.getenv("TOKEN"))

    me = await client.get_me()
    
    async with await client.connect() as chat:
        if(chat_id == None):
            new, answer = await chat.new_chat(
            char, me.id
            )
            return answer.text    
        message = await chat.send_message(
            char, chat_id, text
        )
    return message.text

asyncio.run(get_answer("проснись, я взываю к тебе"))