#!/usr/bin/python3
from shownum import show_number
from accelerometer import auto_orient
from sense_hat import SenseHat
from entur import get_departures
import time
import math
from dateutil.parser import parse
from datetime import datetime, timedelta
from dot_timer import display_secs

UPDATE_INTERVAL = 2 # in minutes
DEBUG = False

# You don't want to spam the API,
# so we're storing the data from the last call
last_update = None
departures = None

def fetch_data():
    # Calls the EnTur API from the entur-script and gets the next departure
    global departures
    global last_update
    if DEBUG:
        print("API CALL")
    departures = get_departures()
    last_update = datetime.now()


def get_next_departure():
    # This function determines if we need to update
    # the data based on the UPDATE_INTERVAL
    # and returns the timestamp of the next departure
    global departures
    global last_update

    if last_update == None:
        fetch_data()
    else:
        elapsed_time = datetime.now() - last_update
        if elapsed_time.seconds / 60 > UPDATE_INTERVAL:
            fetch_data()

    # strips out the timestamp
    next_departure = parse(departures[0]['expectedArrivalTime'])
    return next_departure


def get_time():
    # This function returns the minutes and seconds until the next departure
    next_departure = get_next_departure()
    time_to_departure = next_departure.replace(tzinfo=None) - datetime.now()
    mins = time_to_departure.seconds // 60
    secs = time_to_departure.seconds % 60

    # Some times after a departure has left we get some odd numbers,
    # and we need to call the on the API again to get the next departure
    # This number is usually around 1400 minutes, but just to be safe
    # we update if the departure time is over 9 hours
    # Just be careful to not use this script with a Quay or Stop-Place that
    # usually has busses leaving that infrequent.
    if mins > 540:
        if DEBUG:
            print(f"mins: {mins}, waiting 5 seconds until next api-call")
        time.sleep(5) # usually takes a few seconds to update
        fetch_data()
        return get_time()

    return mins, secs


def main():
    global sense
    sense = SenseHat()
    sense.clear()
    auto_orient(sense)

    c = [200, 255, 0]
    last_min = 0

    while True:
        mins, secs = get_time()
        if mins > 99: # can't display more than two digits with show_number()
            hours = mins // 60
            mins = mins % 60
            sense.show_message(f"{hours}t {mins}min", text_colour=c)

        else:
            if mins != last_min:
                sense.clear()
                last_min = mins
                show_number(mins, c[0], c[1], c[2], sense)

        display_secs(sense, secs, c)
        time.sleep(0.5)
        auto_orient(sense)


if __name__ == '__main__':
    import argparse as argp

    parser = argp.ArgumentParser(description="Shows the next departure outside my house :)")
    parser.add_argument('-r', '--refresh', type=int, default=2, 
                        help="refresh interval in minutes")
    parser.add_argument('-d', '--debug', action="store_true", 
                        help="prints out some info to the terminal while running")    
    args = parser.parse_args()

    UPDATE_INTERVAL = args.refresh
    DEBUG = args.debug
    main()
