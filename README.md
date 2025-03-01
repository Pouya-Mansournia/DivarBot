# DivarBot
Divar Listing Notifier Bot 🚀


This Python bot automatically monitors Divar for new property listings and sends instant notifications to Telegram and WhatsApp. It helps users stay updated with the latest rental or sale listings based on custom filters.

🔹 Features:
✅ Real-time Updates – Checks Divar for new listings every 10 minutes
✅ Telegram Notifications – Sends new property links directly to your Telegram
✅ WhatsApp Alerts – Optional integration for receiving updates via WhatsApp
✅ Custom Filters – Search based on price, location, size, and more
✅ Error Handling – Ensures smooth operation with retry mechanisms

🔹 How It Works:
The bot scrapes Divar.ir for new listings based on predefined search filters
It checks for new property ads and compares them with previously seen listings
If a new listing is found, the bot sends a message to Telegram & WhatsApp
If no new ads are found, the bot sends a "No new listings" message every 10 minutes to confirm it's running
🔹 Platforms Supported:
🔹 Telegram – Uses the Telegram Bot API for instant notifications
🔹 WhatsApp (Optional) – Can send updates via Twilio API or WhatsApp Web Automation




📌 How to Use the Divar to Telegram Bot 🚀
1️⃣ Install Python and Required Packages
First, make sure Python 3.10+ is installed on your system.
2️⃣ Set Up Your Telegram Bot
Open Telegram and search for @BotFather.
Send /newbot and follow the instructions to create a bot.
You will get a Bot Token (save it).
Add your bot to a Telegram channel/group as an Admin.
3️⃣ Configure the Bot
Open the script (divar_bot.py) and update these values:
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"
DIVAR_URL = "https://divar.ir/s/your-custom-search-url"
4️⃣ Run the Bot
python divar_bot.py


Made By GPT-AI
