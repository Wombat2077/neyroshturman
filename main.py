import dotenv
from characterai import aiocai, types
import random as rd
import os
import vk_api
import asyncio
import vk_api.bot_longpoll as lp
from vk_api.bot_longpoll import VkBotMessageEvent
import logging
import json



dotenv.load_dotenv(".env")
bot = vk_api.VkApi(token=os.getenv("VK_TOKEN"))
longpoll = lp.VkBotLongPoll(vk=bot, group_id="214416249")
logging.basicConfig(filename='logs.log', level=logging.DEBUG)

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
async def send_message(message: VkBotMessageEvent) -> None:
    answer: str = await get_answer(message.message['text'])
    if message.from_chat:
        bot.method(
            "messages.send", 
            {
                "chat_id" : message.chat_id,
                "message" : answer,
                "random_id" : rd.randint(0, 10000000),
                "forward" : json.dump({
                    "peer_id" : message["peer_id"],
                    "conversation_message_ids " : [message["conversation_message_id"]],
                    "is_reply" : 1
                })
            }
            )
    else:
        bot.method(
            "messages.send", 
            {
                "user_id" : message.chat_id,
                "message" : answer,
                "random_id" : rd.randint(0, 10000000),
                "forward" : json.dump({
                    "peer_id" : message["peer_id"],
                    "conversation_message_ids " : [message["conversation_message_id"]],
                    "is_reply" : 1
                })
            }
            )
    
async def main():
    while True:
        try:
            event: VkBotMessageEvent
            for event in longpoll.listen():
                if event.message['text'] != 0:
                    await send_message(event)
                    logging.info()
        except Exception as e:
            logging.error("Error", str(e), event)
            
        
print("starting")
asyncio.run(main())


