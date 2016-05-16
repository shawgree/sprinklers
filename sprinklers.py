from datetime import datetime
from datetime import timedelta
import json
#import serial
import sys
import time

#ser = serial.Serial(
#    port=sys.argv[1],
#    baudrate=9600
#)

# How frequently we'll check to see if it's time to run.
update_rate = timedelta(seconds=30)

# Suck up the json and load its values.
schedule = json.loads(open('test_schedule.json').read())
print(schedule)

# Convert the time in the schedule to a time today.
schedule_time = datetime.strptime(schedule["time"], '%I:%M%p')
start_time = datetime.combine(datetime.today(), schedule_time.time())

# If the current time falls within this range we'll start the sprinklers.
# Double the update_rate to ensure we don't miss the window.
start_time_range = start_time
start_time_range += 2* update_rate

print("Entering loop, sprinklers will run when time is between: " + str(start_time) + " and " + str(start_time_range))

#exit = False
#while(not exit):
#    current_time = datetime.now()
#    print(current_time)
#
#    if (current_time > start_time and current_time < start_time_range):
#        print("Starting schedule: " + schedule['name'])
#        exit = True
#    else:
#        print("Sleeping...")
#        time.sleep(update_rate.seconds)

for entry in schedule['schedule']:
    station = entry['station']
    time_in_minutes = int(entry['runtime'])

    print("Starting station: " + station + ", will run for " + str(time_in_minutes) + " minutes")
#    ser.write(station.encode('utf-8'))
#    time.sleep(10*60)


#print("Starting zone 1")
#ser.write('1'.encode('utf-8'))
#
#print("Starting zone 2")
#ser.write('2'.encode('utf-8'))
#time.sleep(10*60)
#
#print("Starting zone 3")
#ser.write('3'.encode('utf-8'))
#time.sleep(10*60)
#
#print("Starting zone 4")
#ser.write('4'.encode('utf-8'))
#time.sleep(15*60)
#
#print("Starting zone 5")
#ser.write('5'.encode('utf-8'))
#time.sleep(15*60)
#
#print("Starting zone 6")
#ser.write('6'.encode('utf-8'))
#time.sleep(15*60)
#
#print("Starting zone 7")
#ser.write('7'.encode('utf-8'))
#time.sleep(15*60)
#
#ser.write('0'.encode('utf-8'))
#ser.close()