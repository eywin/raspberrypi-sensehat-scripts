# Raspberry Pi Sense Hat scripts
Some scripts for the astro-pi sense hat.

## What does these scripts do??

### accelerometer.py
This script reads the orientation of the Pi and orients the output on the led-array accordingly. You can run it independently, but it makes more sense to import the auto-orient-function in other scripts that use the screen.

### display_next_departure.py
This scripts displays the next metro (T-bane) departure where I live. It uses EnTurs Journey Planner API to get the next departure. To change which stop it looks up you will have to find the Quay-Id on [EnTurs site](https://api.entur.io/journey-planner/v2/ide). Click the "Search for ID"-button in the menu-bar on the top and you should be able to find the correct Quay-ID. Note that you need to specify which quay and not just which stop. If you only use StopPlace you'll get the next departure from that stop, so if there are metros going both eastward and westward from that stop (for example Majorstuen), you'll won't know if the metro will go east og west, you'll simply get the next departure from the StopPlace in any direction. For more information on the EnTur JourneyPlanner, [click here](https://developer.entur.org/pages-journeyplanner-journeyplanner).

You will have to replace the Quay-ID in the entur.py-file with the right one for your stop. The quay-id is located inside the query-string
``` 
quay(id: "NSR:Quay:11449")
```

### dot_timer.py
This is a nice little timer that counts down seconds on a dot timer.

### entur.py
Contains the API-call to EnTur JourneyPlanner

### shownum.py
Handy script for displaying two digits at the same time on the SenseHat. 

## How to run the scripts
These scripts are made for and tested with Python 3.7 You might have issues with older versions.

You can run all the scripts for themselves, but ´display_next_departure.py´ is the oly script with a practical application

Running
```bash
$ python3 display_next_departure.py --help
```
will display a couple of extra options for running the script
