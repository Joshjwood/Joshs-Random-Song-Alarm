import os
import random
import datetime as dt
import time
from mutagen.mp3 import MP3
from func import minute

# This script is designed to run constantly, but the
# process would be better suited to being scheduled
# with cron or windows task scheduler.

# This directory should contain the MP3s you want in
# your playlist, and nothing else.
PATH = "D:\\AlarmSongs\\"
ALARM_TIME = 11     #24 hour time

files = os.listdir(PATH)
mp3s = []
for item in files:
    if ".mp3" in item:
        mp3s.append(item)

ALARM_TIME = 11

while True:
    now = dt.datetime.now()
    simplified_time = {"hour": now.hour, "minute": str(minute(now))}
    if simplified_time["hour"] == ALARM_TIME:
        # Picks a track at random, starts it, records and prints the track name, then removes it from the
        # playlist, then sleeps for the exact length of the song, so that the subsequent song comes in at the right time
        current_track = random.choice(mp3s)
        os.startfile(f"{PATH}{current_track}")
        current_track_details = MP3(f"{PATH}{current_track}")
        mp3s.remove(current_track)
        #print(mp3s)
        print(f"Current Track: {current_track[3:-4]}\nCurrent Time: {simplified_time['hour']}:{simplified_time['minute']}\n")
        time.sleep(int(current_track_details.info.length))

    else:
        time_difference = ALARM_TIME - simplified_time['hour']
        if time_difference < 0:
            time_difference += 24
        print(f"It's not time. Alarm begins in {time_difference} hours.")
        print(simplified_time)
        time.sleep(60)
