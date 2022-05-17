import schedule
from app import notification
import time

schedule.every().day.at("09:00").do(notification)
schedule.every().day.at("14:00").do(notification)

while True:
    schedule.run_pending()
    time.sleep(1)