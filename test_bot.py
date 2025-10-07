# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes
# from telegram.request import HTTPXRequest

# BOT_TOKEN = "8161441063:AAEOlvzIHOV1UQQ3BqOrEvXvsIBJfihpCwk"  # Replace with BotFather token

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("✅ Bot is working and connected!")

# def main():
#     # Add timeout settings
#     request = HTTPXRequest(connect_timeout=30.0, read_timeout=30.0)

#     # Build application with custom request
#     app = Application.builder().token(BOT_TOKEN).request(request).build()

#     # Register /start command
#     app.add_handler(CommandHandler("start", start))

#     print("Bot is running... Send /start to your bot in Telegram")
#     app.run_polling()

# if __name__ == "__main__":
#     main()
