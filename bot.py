import os
from aiogram import Bot, Dispatcher, types
from llama_cpp import Llama

bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
dp = Dispatcher()

# Загрузка модели из папки model/
model = Llama(model_path="model/tinyllama-1.1b.Q4.gguf")

@dp.message()
async def reply(message: types.Message):
    response = model.create_chat_completion(messages=[{"role": "user", "content": message.text}])
    await message.reply(response['choices'][0]['message']['content'])

dp.run_polling(bot)
