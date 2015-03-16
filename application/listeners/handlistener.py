__author__ = 'Roshan'

#This class listen to all the hand
from application.listeners.baselistener import BaseListener


class HandListener(BaseListener):
    """
    This class listens to all the hand movements
    """
    def __init__(self, controller):
        """
        prepares to listen to the controller frame
        :param controller:
        :return:
        """
        super(HandListener, self).__init__(controller)

    def handle_frame(self, frame):
        """
        handle frames sent from leap
        :param frame:
        :return:
        """
        print "pitch:", self.pitch
        print "roll:", self.roll
        print "yaw:", self.yaw