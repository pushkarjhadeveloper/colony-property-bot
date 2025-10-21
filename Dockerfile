# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port (not really used by Telegram bot, but required by HF)
EXPOSE 7860

# Run the bot
CMD ["python", "bot.py"]
# Note: Ensure that 'bot.py' is the entry point of your Telegram bot application.