import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

BOT_TOKEN = "8981342640:AAEmrylkeXZd9CYfwWdALV_9qiFerm2zmoA"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я твой первый бот.\n\n"
        "/start - приветствие\n"
        "/help - список команд\n"
        "/about - информация о боте"
    )


@dp.message(Command("about"))
async def cmd_about(message: Message):
    await message.answer(
        "🤖 Информация о боте\n\n"
        "Этоого ботяру сделал алиш с aiogram.\n"
        "Версия: 666"
    )


@dp.message(F.text == "Группа")
async def group_handler(message: Message):
    await message.answer("Привет, группа!")


@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")


async def main():
    print("Бот запущен...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)

TOKEN = "YOUR_BOT_TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

# Подключаем Router
dp.include_router(router)

# -------------------- Reply клавиатура --------------------

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Python"),
            KeyboardButton(text="JS"),
            KeyboardButton(text="C#"),
        ]
    ],
    resize_keyboard=True,
)

# -------------------- Inline клавиатура --------------------

help_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Python Docs",
                url="https://docs.python.org/3/"
            )
        ],
        [
            InlineKeyboardButton(
                text="JavaScript Docs",
                url="https://developer.mozilla.org/en-US/docs/Web/JavaScript"
            )
        ],
        [
            InlineKeyboardButton(
                text="C# Docs",
                url="https://learn.microsoft.com/dotnet/csharp/"
            )
        ],
        [
            InlineKeyboardButton(
                text="Начать обучение",
                callback_data="study"
            )
        ],
    ]
)

# -------------------- Команда /start --------------------

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Добро пожаловать!\n\nВыберите язык программирования:",
        reply_markup=reply_keyboard,
    )


@router.message(F.text == "Python")
async def python_info(message: Message):
    await message.answer(
        "🐍 Python — простой и мощный язык программирования. "
        "Используется для создания сайтов, Telegram-ботов, анализа данных, "
        "искусственного интеллекта и автоматизации."
    )


@router.message(F.text == "JS")
async def js_info(message: Message):
    await message.answer(
        "🌐 JavaScript — язык программирования для создания "
        "интерактивных веб-сайтов и веб-приложений."
    )


@router.message(F.text == "C#")
async def csharp_info(message: Message):
    await message.answer(
        "💻 C# — язык программирования компании Microsoft. "
        "Используется для разработки игр на Unity, "
        "настольных программ и веб-приложений."
    )


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "📚 Полезные ссылки:",
        reply_markup=help_keyboard,
    )


@router.callback_query(F.data == "study")
async def start_learning(callback: CallbackQuery):
    await callback.answer(
        "🚀 Начинаем обучение!",
        show_alert=True,
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())