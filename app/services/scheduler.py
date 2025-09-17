import time
from app.services.gee_fetcher import save_latest_data

# Run every 24 hours
while True:
    print("Fetching latest SPEI data...")
    save_latest_data()
    time.sleep(86400)  # 24h
