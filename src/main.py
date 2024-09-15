#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from lib.log import *
from high_stakes.events import *

open_log("red-win-point.csv")


def driver_function():
    pass


def autonomous_function():
    intake_1st_stage.set_velocity(525, RPM)
    intake_2nd_stage.set_velocity(525, RPM)
    pid_driver.drive(-1000, True)
    clamp.set(True)
    intake_1st_stage.spin(REVERSE)
    intake_2nd_stage.spin(FORWARD)
    wait(1000, MSEC)
    pid_turner.turn(35, FRAME_HEADING_RELATIVE)
    intake_retract.set(True)
    pid_driver.drive(650)
    intake_retract.set(False)
    pid_turner.turn(-145, FRAME_HEADING_RELATIVE)
    wait(100, MSEC)
    pid_driver.drive(800, True)
    pid_turner.turn(40, FRAME_HEADING_RELATIVE)
    wait(100, MSEC)
    pid_driver.drive(-885, True)


init_event_handling()

# register the competition functions
competition = Competition(driver_function, autonomous_function)
