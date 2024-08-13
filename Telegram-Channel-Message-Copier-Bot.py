
### SCRIPT:
```python
from telegram import Update, error as telegram_error
from telegram.ext import MessageHandler, ApplicationBuilder, filters, ContextTypes
import logging
import os
from dotenv import load_dotenv

# Logging Setup
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger('telegram').setLevel(logging.WARNING)
logging.getLogger('httpx').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Load Environment Variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
LINK = os.getenv("AUTO_MESSAGE_LINK")

# Parse the CHANNELS string
channels_str = os.getenv("CHANNELS")
CHANNELS = dict(item.split(":") for item in channels_str.split(",") if item)

# Convert channel IDs to integers
CHANNELS = {k: int(v) for k, v in CHANNELS.items()}

# Auto-message Function
async def callback_minute(context: ContextTypes.DEFAULT_TYPE):
    for channel_id in CHANNELS.values():
        try:
            await context.bot.send_message(chat_id=channel_id, text=LINK)
        except telegram_error.TelegramError as e:
            logger.error(f"Error sending message to {channel_id}: {e}")

# Copy Messages Function
async def copy_message(update: Update, context):
    if update.channel_post:
        source_channel = update.channel_post.chat_id
        message_id = update.channel_post.message_id

        # Get the 'source_channel_main' channel ID for comparison
        source_channel_main_id = CHANNELS.get("source_channel_main", None)  # Using .get to avoid KeyError

        # Determine target channels
        if source_channel == source_channel_main_id:
            # If the source is 'source_channel_main', copy to all other channels
            target_channels = [cid for cid in CHANNELS.values() if cid != source_channel]
        else:
            # For all other channels, copy to all except 'source_channel_main'
            target_channels = [cid for cid in CHANNELS.values() if cid != source_channel and cid != source_channel_main_id]

        logger.info(f"Copying message from {source_channel} to {target_channels}")

        for channel_id in target_channels:
            try:
                await context.bot.copy_message(chat_id=channel_id, from_chat_id=source_channel, message_id=message_id)
                logger.info(f"Successfully copied message to {channel_id}")
            except telegram_error.TelegramError as e:
                channel_name = next((name for name, id in CHANNELS.items() if id == channel_id), 'Unknown')
                logger.error(f"Error copying message to {channel_name} ({channel_id}): {e}")

# Main Execution
if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()
    message_handler = MessageHandler(filters.ALL, copy_message)
    application.add_handler(message_handler)

    job_queue = application.job_queue
    job_minute = job_queue.run_repeating(callback_minute, interval=75600, first=10)

    application.run_polling()
