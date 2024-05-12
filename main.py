import dotenv
from characterai import aiocai, types
import random as rd
import os
import vk_api
import asyncio
import vk_api.bot_longpoll as lp
from vk_api.bot_longpoll import VkBotMessageEvent
dotenv.load_dotenv(".env")
bot = vk_api.VkApi(token=os.getenv("VK_TOKEN"))
#policy = asyncio.WindowsSelectorEventLoopPolicy()
#asyncio.set_event_loop_policy(policy)
longpoll = lp.VkBotLongPoll(vk=bot, group_id="214416249")

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

        return message.text

async def main():
    while True:
        try:
            event: VkBotMessageEvent
            for event in longpoll.listen():
                answer = await get_answer(event.message['text'])
                bot.method("messages.send", {"chat_id" : event.chat_id, "message" : answer, "random_id" : rd.randint(0, 10000000)})
        except Exception as e:
            print(e)
        
print("starting")
asyncio.run(main())


