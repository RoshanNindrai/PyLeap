################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################


import sys
sys.path.insert(0, "../../")
print sys.path
from library import Leap


class BaseListener(object):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def __init__(self, controller):
        """
        stores the property of pitch, yaw, roll
        :return:
        """
        self.controller = controller
        self.pitch  = None
        self.yaw    = None
        self.roll   = None
        if self.controller.is_connected:
            self.prepare_gestures()
            self.start()

    def prepare_gestures(self):
        print "Enabling gestures"

        # Enable gestures
        self.controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        self.controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        self.controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
        self.controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

    def start(self):
        # Get the most recent frame and report some basic information
        while True:
            try:
                frame = self.controller.frame()

                for hand in frame.hands:

                    normal = hand.palm_normal
                    direction = hand.direction
                    # Calculate the hand's pitch, roll, and yaw angles
                    self.pitch = direction.pitch * Leap.RAD_TO_DEG
                    self.roll  = normal.roll * Leap.RAD_TO_DEG
                    self.yaw   = direction.yaw * Leap.RAD_TO_DEG

                    self.handle_frame(frame)
            except KeyboardInterrupt:
                self.on_exit()

    def on_exit(self):
        """
        cleanup
        :return:
        """
        self.controller = None


    def handle_frame(self, frame):
        """
        Needs to be overridden
        :param frame:
        :return:
        """
        raise RuntimeError("This Method has to be overridden")

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"




