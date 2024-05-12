from aiogram import Dispatcher,Bot,types,executor
import script_code
Token='enter your bot token'
bot=Bot(token=Token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer('enter the link')

@dp.message_handler(content_types=['text'])
async def audio(message:types.Message):
    try:
        script_code.begin(message.text).convert()
        await bot.send_video(message.chat.id,video=open(str(script_code.begin(message.text).name()),'rb'))
    except Exception as ex:
        await message.answer(str(script_code.begin(message.text).name()))

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
