source venv/bin/activateimport asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

BOT_TOKEN = "8981342640:AAEmrylkeXZd9CYfwWdALV_9qiFerm2zmoA"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

dp.include_router(router)

#КЛАВА

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


inline_keyboard = InlineKeyboardMarkup(
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
                callback_data="start_learning"
            )
        ]
    ]
)


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Выберите язык программирования:",
        reply_markup=reply_keyboard
    )

# ---------------- Reply-кнопки ----------------

@router.message(F.text == "Python")
async def python_info(message: Message):
    await message.answer(
        "Python — простой и универсальный язык программирования. "
        "Используется для создания сайтов, Telegram-ботов, анализа данных и искусственного интеллекта."
    )


@router.message(F.text == "JS")
async def js_info(message: Message):
    await message.answer(
        "JavaScript — язык программирования для создания интерактивных сайтов и веб-приложений."
    )


@router.message(F.text == "C#")
async def csharp_info(message: Message):
    await message.answer(
        "C# — язык программирования компании Microsoft. "
        "Используется для разработки игр, программ и веб-приложений."
    )


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Полезные ссылки:",
        reply_markup=inline_keyboard
    )


@router.callback_query(F.data == "start_learning")
async def start_learning(callback: CallbackQuery):
    await callback.answer(
        "Начинаем обучение!",
        show_alert=True
    )



async def main():
    print("Бот запущен...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())