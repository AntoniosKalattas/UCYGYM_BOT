import schedule
import time
import subprocess
from datetime import datetime, timedelta


##########################################################################
#time options: 1    2    3     4     5     6     7     8                 #
#              7:45 9:30 11:15 13:00 14:45 16:45 18:30 20:15             #
              time_option = 7                                            #
##########################################################################


# Function to run the main script
def run_main_script():
    today = datetime.now()
    future_date = today + timedelta(days=5)
    next5day = future_date.day
    print("Running run.py...")
    subprocess.run(["python3", "autoReservation.py", str(time_option), str(next5day)])  # Call autoReservation.py using subprocess

# Schedule the script to run every day at 8:00 AM
schedule.every().day.at("23:37").do(run_main_script)

# Keep the script running
print("Scheduler started. Waiting for the scheduled time...")
while True:
    schedule.run_pending()
    time.sleep(1)
