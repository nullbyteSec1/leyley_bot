from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes



async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("./media/text/menu.txt", "r", encoding="utf-8") as f:
        ascii_menu = f.read()

    if update.callback_query:
        message = update.callback_query.message
        query = update.callback_query
    else:
        message = update.message
        query = None

    try:
        await message.reply_photo(
            photo="./media/imagens/icon.jpg",
            caption=ascii_menu,
        )
    except Exception as e:
        print(f"Erro ao enviar menu: {e}")
        if query:
            await query.answer("Erro ao carregar o menu 😔", show_alert=True)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔱 MENU 🔱", callback_data="btn_menu")],
    ]

    with open("./media/text/start.txt", "r", encoding="utf-8") as f:
        starting_bot_text = f.read()

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        starting_bot_text,
        reply_markup=reply_markup,
        reply_to_message_id=update.message.message_id
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "btn_menu":
        await menu(update, context)

