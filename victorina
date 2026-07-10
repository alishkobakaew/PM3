import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)

BOT_TOKEN = "8981342640:AAEmrylkeXZd9CYfwWdALV_9qiFerm2zmoA"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


language_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Python"),
            KeyboardButton(text="JS"),
            KeyboardButton(text="C#"),
        ]
    ],
    resize_keyboard=True,
)

# START

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Добро пожаловать!\n\nВыберите язык программирования:",
        reply_markup=language_keyboard,
    )

# OTVETY

@dp.message(F.text == "Python")
async def python_info(message: Message):
    await message.answer(
        " Python — простой и популярный язык программирования. "
        "Используется для создания ботов, сайтов, программ, анализа данных и искусственного интеллекта."
    )


@dp.message(F.text == "JS")
async def js_info(message: Message):
    await message.answer(
        " JavaScript — язык программирования для создания интерактивных сайтов и веб-приложений."
    )


@dp.message(F.text == "C#")
async def csharp_info(message: Message):
    await message.answer(
        " C# — язык программирования от Microsoft. "
        "Используется для разработки игр на Unity, приложений Windows и веб-сервисов."
    )

# KOMANDA /HELP
@dp.message(Command("help"))
async def help_command(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📘 Python Docs",
                    url="https://docs.python.org/3/",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📗 JavaScript Docs",
                    url="https://developer.mozilla.org/ru/docs/Web/JavaScript",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📙 C# Docs",
                    url="https://learn.microsoft.com/dotnet/csharp/",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🚀 Начать обучение",
                    callback_data="start_learning",
                )
            ],
        ]
    )

    await message.answer(
        "Выберите действие:",
        reply_markup=keyboard,
    )

# ---------------- Alert ----------------

@dp.callback_query(F.data == "start_learning")
async def start_learning(callback: CallbackQuery):
    await callback.answer(
        "🚀 Начинаем обучение!",
        show_alert=True,
    )

# ---------------- Запуск бота ----------------

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())