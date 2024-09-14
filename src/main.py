#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from lib.log import *
from high_stakes.events import *

open_log("red_winpoint.csv")


def driver_function():
    pass


def autonomous_function():
    intake_1st_stage.set_velocity(100, PERCENT)
    intake_2nd_stage.set_velocity(100, PERCENT)
    pid_driver.drive(-1000)
    clamp.set(True)
    intake_1st_stage.spin(REVERSE)
    intake_2nd_stage.spin(FORWARD)
    pid_turner.turn(50, FRAME_HEADING_RELATIVE)
    intake_retract.set(True)
    pid_driver.drive(550)
    intake_retract.set(False)

    pass


init_event_handling()

# register the competition functions
competition = Competition(driver_function, autonomous_function)
