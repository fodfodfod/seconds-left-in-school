"""


*******************
WARNING
when transfering to raspberry pi change the location of credentials.json

*******************




"""
from __future__ import print_function

import datetime
import os.path
import time

import sys



import json
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

"""will return false if there is no argument"""
try:
    one_output = bool(sys.argv[1])
except:
    one_output = False

school_timings = ""

def count_later_seconds(todays_day_type):
    seconds_remaining_today = 0

    for period in range(0, len(school_timings[todays_day_type])):
        school_timings[todays_day_type][period]["start"][0]
        start_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, school_timings[todays_day_type][period]["start"][0], school_timings[todays_day_type][period]["start"][1])
        end_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, school_timings[todays_day_type][period]["end"][0], school_timings[todays_day_type][period]["end"][1])
        seconds_remaining_today += time.mktime(end_time.timetuple()) - time.mktime(start_time.timetuple())
    return seconds_remaining_today



def count_today_seconds(todays_day_type):
    seconds_remaining_today = 0

    for period in range(0, len(school_timings[todays_day_type])):
        school_timings[todays_day_type][period]["start"][0]
        start_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, school_timings[todays_day_type][period]["start"][0], school_timings[todays_day_type][period]["start"][1])
        end_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, school_timings[todays_day_type][period]["end"][0], school_timings[todays_day_type][period]["end"][1])
        current_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second)
        
        if(current_time > start_time and not current_time > end_time):
            seconds_remaining_today += time.mktime(end_time.timetuple()) - time.mktime(current_time.timetuple())
        elif(not current_time > end_time):
            seconds_remaining_today += time.mktime(end_time.timetuple()) - time.mktime(start_time.timetuple())
    return seconds_remaining_today




def main():
    global school_timings
    file = open("school.json", "r")
    string = file.read()
    # print(string)
    school_timings = json.loads(string)
    file.close()

    file = open("Schedule.json", "r")
    schedule_string = file.read()
    schedule = json.loads(schedule_string)
    file.close()

    print(type(schedule))

    later_day_seconds = 0

    for event in schedule:
        if("Schedule" in event["summary"]):
            # if(event["start"]["date"] == str(datetime.date.today())):
            #     today_seconds += today_seconds(event["summary"][0])
            if(event["start"]["date"] > str(datetime.date.today()) and event["start"]["date"] < str(datetime.datetime(2022, 12, 12))):
                later_day_seconds += count_later_seconds(event["summary"][0])
    
    while True:
        todays_day_type = ""
        today_seconds = 0
        for event in schedule:
            if("Schedule" in event["summary"]):
                if(event["start"]["date"] == str(datetime.date.today())):
                    today_seconds += count_today_seconds(event["summary"][0])
                    todays_day_type = event["summary"][0]
                # elif(event["start"]["date"] > str(datetime.date.today())):
                #     later_day_seconds += later_seconds(event["summary"][0])
        total_seconds = later_day_seconds + today_seconds
        print(f"{total_seconds}s in this semester, {today_seconds}s in this {todays_day_type} day, and the time is " + datetime.datetime.now().strftime("%I:%M:%S %p"))
        if one_output:
            break
        time.sleep(1)






if __name__ == '__main__':
    main()