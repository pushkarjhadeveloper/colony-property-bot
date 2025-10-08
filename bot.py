from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.request import HTTPXRequest
import re
import os

# Get token and form links from environment variables
BOT_TOKEN = "8161441063:AAEOlvzIHOV1UQQ3BqOrEvXvsIBJfihpCwk"  # replace with your actual token
print(f"DEBUG: BOT_TOKEN value -> {BOT_TOKEN}")  # Ensure to set this environment variable securely

BUY_FORM_LINK = "https://l1nq.com/sKilM"
RENT_FORM_LINK = "https://sl1nk.com/3WLBB"
SELL_FORM_LINK = "https://l1nq.com/gD8S5"

# --- Command Handlers ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Colony Property Hub 🏠\n\n"
        "Use these commands:\n"
        "/buy - Buy property\n"
        "/rent - Rent property\n"
        "/sell - Sell property"
    )

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🏡 Buy Property Form:\n{BUY_FORM_LINK}")

async def rent(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🏘️ Rent Property Form:\n{RENT_FORM_LINK}")

async def sell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🏢 Sell Property Form:\n{SELL_FORM_LINK}")

# --- Fallback / Catch-All for Hi & Hello ---

async def handle_greetings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text in ["hi", "hello"]:
        await update.message.reply_text(
            "👋 Hello there! Use one of these commands to get started:\n"
            "/buy - Buy property\n"
            "/rent - Rent property\n"
            "/sell - Sell property"
        )

# --- Optional catch-all for other messages ---
async def handle_unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚠️ Sorry, I didn’t understand that.\n"
        "Please use /buy, /rent, or /sell."
    )

# --- Main Function ---
def main():
    request = HTTPXRequest(connect_timeout=30.0, read_timeout=30.0)
    app = Application.builder().token(BOT_TOKEN).request(request).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(CommandHandler("rent", rent))
    app.add_handler(CommandHandler("sell", sell))

    # Greeting handler
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex(r'(?i)^(hi|hello)$'), handle_greetings))

    # Unknown message fallback
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_unknown))

    print("🤖 Bot is running on Render...")
    app.run_polling()

if __name__ == "__main__":
    main()
