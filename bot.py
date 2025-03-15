from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with the token from BotFather
TOKEN = "7788170518:AAEbDYCNY4WVGlqNHpfKiz-x7sUsRETXAJk"

async def start(update: Update, context: CallbackContext) -> None:
    """Handles the /start command"""
    await update.message.reply_text("Welcome to MemeTradeBot! Use /help to see available commands.")

async def help_command(update: Update, context: CallbackContext) -> None:
    """Handles the /help command"""
    await update.message.reply_text("Available commands:\n/start - Start the bot\n/help - Get help")

def main():
    """Main function to run the bot"""
    app = Application.builder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
