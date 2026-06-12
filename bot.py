import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Токен вставлен напрямую (будьте осторожны, не выкладывайте этот файл в публичные репозитории!)
TOKEN = "8977416270:AAFXF3GT_W_fgUJMzGJhXs0_UoccTp2A7OQ"
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создание Reply-клавиатуры
def get_main_kb():
    kb = [
        [KeyboardButton(text="О нас"), KeyboardButton(text="Направления")],
        [KeyboardButton(text="Контакты")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Сәлеметсіз бе! Молодежный ресурсный центр қош келдіңіз. "
        "Мен сізге көмектесуге дайынмын!",
        reply_markup=get_main_kb()
    )

# Обработчики кнопок
@dp.message(F.text == "О нас")
async def about_us(message: types.Message):
    await message.answer("Молодежный ресурсный центр — это пространство для самореализации молодежи, поддержки инициатив и развития талантов.")

@dp.message(F.text == "Направления")
async def directions(message: types.Message):
    await message.answer("Наши направления: \n1. Волонтерство\n2. Трудоустройство\n3. Творческое развитие\n4. Психологическая помощь")

@dp.message(F.text == "Контакты")
async def contacts(message: types.Message):
    await message.answer("Наши контакты:\n📍 Адрес: г. Актобе, ул. Молодежная, 1\n📞 Телефон: +7 (7132) 00-00-00\n🌐 Instagram: @mrc_aktobe")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())