#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from lib.log import *
from high_stakes.events import *

open_log("red_winpoint.csv")


def driver_function():
    pass


def autonomous_function():
    pid_driver.drive(1000)
    pass


init_event_handling()

# register the competition functions
competition = Competition(driver_function, autonomous_function)
