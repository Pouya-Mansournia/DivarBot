import requests
import time
from bs4 import BeautifulSoup

# 🔹 Divar URL to check
DIVAR_URL = "Type Your Divar Filter"                                            

# 🔹 Your Telegram bot token and chat ID
BOT_TOKEN = "YOUR_BOT_TOKEN"  # Replace with your bot token                     // Add it
CHAT_ID = "@your_channel"      # Replace with your channel username or ID     // Add it

# 🔹 Keep track of seen listings
seen_ads = set()

# 🔹 Timer to track last status update
last_status_time = time.time()

def get_new_listings():
    """Fetch listings from Divar."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(DIVAR_URL, headers=headers)

    if response.status_code != 200:
        print(f"⚠️ Error fetching Divar: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    ads = set()

    # Extract unique ad IDs from the page
    for ad in soup.find_all("a", href=True):
        if "/v/" in ad["href"]:  # Check for valid listing URLs
            ad_id = ad["href"].split("/")[-1]
            ads.add(ad_id)

    new_ads = ads - seen_ads
    seen_ads.update(new_ads)  # Update seen ads list
    return new_ads

def send_telegram_message(message):
    """Send a message to Telegram."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}

    response = requests.post(url, data=data)
    return response.json()

def main():
    """Main loop to check Divar and send new listings to Telegram."""
    global last_status_time
    print("🚀 Divar to Telegram bot started!")

    while True:
        print("🔎 Checking for new listings...")
        new_listings = get_new_listings()

        if new_listings:
            for ad in new_listings:
                message = f"📢 *New Listing Found!*\n🔗 [View Listing](https://divar.ir/v/{ad})"
                send_telegram_message(message)
                print(f"✅ Sent: {message}")
            last_status_time = time.time()  # Reset status timer when new ads are found
        else:
            print("❌ No new listings found.")

            # Send a status update every 10 minutes
            if time.time() - last_status_time >= 600:  # 600 seconds = 10 minutes
                send_telegram_message("⏳ No new listings found yet. Bot is still running...")
                print("🔄 Sent status update to Telegram.")
                last_status_time = time.time()  # Reset timer

        time.sleep(120)  # Wait 2 minutes before checking again

if __name__ == "__main__":
    main()
