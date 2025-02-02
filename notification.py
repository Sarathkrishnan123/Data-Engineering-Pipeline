import asyncio
from telegram import Bot
import time

async def send_notification(bot_token, chat_id, message, initial_delay=1, max_retries=5):
    """
    Send a notification message via Telegram bot with a backoff mechanism.
    
    Args:
        bot_token (str): The bot token provided by BotFather.
        chat_id (str): The ID of the chat where the message will be sent.
        message (str): The message to be sent.
        initial_delay (int): Initial delay before the first retry, in seconds.
        max_retries (int): Maximum number of retries.
    """
    retry_delay = initial_delay
    for attempt in range(max_retries):
        try:
            bot = Bot(token=bot_token)
            await bot.send_message(chat_id=chat_id, text=message)
            print("Notification sent successfully.")
            return  # Notification sent successfully, exit the function
        except Exception as e:
            print(f"Failed to send notification: {str(e)}")
            print(f"Retrying in {retry_delay} seconds...")
            await asyncio.sleep(retry_delay)
            retry_delay *= 2  # Exponential backoff

    print("Maximum retries reached. Notification could not be sent.")
