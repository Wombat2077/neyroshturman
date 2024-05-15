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
chats_with_memory = {
    2 : "0cedc47f-86ac-4fe9-835d-ecab0eb26a53",
}



async def get_answer(text: str, chat_id=None):
    char = 'nSgypqXQwOgl1PmBs2AFcCKUezG1Lgjb23i66vOtFdM'

    client = aiocai.Client(os.getenv("TOKEN"))

    me = await client.get_me()
    
    async with await client.connect() as chat:
        if(chat_id == None):
            new, answer = await chat.new_chat(
            char, me.id
            )
            return message.text    
        chat_id = chat_id
        message = await chat.send_message(
            char, chat_id, text
        )
    return message.text
async def send_message(message: VkBotMessageEvent) -> None:
    global chats_with_memory
    answer: str = await get_answer(message.message['text'], chats_with_memory.get(message.chat_id))
    if message.from_chat:
        bot.method(
            "messages.send", 
            {
                "chat_id" : message.chat_id,
                "message" : answer,
                "random_id" : rd.randint(0, 10000000),
                "forward" : json.dumps({
                    "peer_id" : message.message["peer_id"],
                    "conversation_message_ids " : [message.message["conversation_message_id"]],
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
                "forward" : json.dumps({
                    "peer_id" : message.message["peer_id"],
                    "conversation_message_ids " : [message.message["conversation_message_id"]],
                    "is_reply" : 1
                })
            }
            )
    
async def main():
    while True:
        try:
            event: VkBotMessageEvent
            for event in longpoll.listen():
                if event.message['text'] != "":
                    await send_message(event)
                    logging.info("INFO:", event)
        except Exception as e:
            logging.error("Error", str(e), event)
            
        
print("starting")
asyncio.run(main())


