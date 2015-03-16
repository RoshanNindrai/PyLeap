__author__ = 'Roshan'

import sys
sys.path.insert(0, "../")
from application.listeners.handlistener import HandListener
from library import Leap


def main():
    # Create a sample listener and controller
    listener = HandListener(Leap.Controller())

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()