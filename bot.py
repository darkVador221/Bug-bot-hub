from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Liste des liens à afficher
LINKS = [
    ("Bug Bot 1", "https://www.mediafire.com/file/bo13frn7jnoem8b/𝐑𝐚𝐲𝐳𝐈𝐧𝐟𝐥𝐨𝐰+𝐕𝟔+𝐋𝐚𝐬𝐭+𝐕𝐞𝐫𝐬𝐢𝐨𝐧+(SixVvip).zip/file"),
    ("Bug Bot 2", "https://www.mediafire.com/file/dih6pjuc4b8walp/SC+CPANEL+++BUG+V1.3+NEW+UPDATE+TARZVGAI+🔪🩸.zip/file"),
    ("Panel hosting", "https://bot-hosting.net"),
    ("Panel solar", "https://solarhosting.cc")
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Voir les Liens", callback_data='links')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Bienvenue sur 『 BUG.BOT LINKS ⌁ PANEL HUB 』\n"
        "Le canal ultime du dark world des bugs & panels.\n"
        "Powered by Dark Gamer.",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'links':
        message = "Voici la liste des liens disponibles :\n"
        for name, url in LINKS:
            message += f"- {name} : {url}\n"
        await query.edit_message_text(message)

def main():
    import config
    app = ApplicationBuilder().token(config.TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot démarré...")
    app.run_polling()

if __name__ == '__main__':
    main()
