__author__ = "Ric Rodriguez"
__email__ = "therickyross2@gmail.com"
__project__ = "SEADSTestbed"

import RPi.GPIO as GPIO


class PinControl(object):
    """
    General class for controlling pins on the raspberry pi
    To specify which pins you want to control, pass a list of ints to the constructor
    We will be using the GPIO.BOARD convention, where the physical numbering is the pin number
    Reference here https://i.stack.imgur.com/gaU6t.png
    Its recommended you alias the pins on the calling function for easier usage
    i.e PIN_LIGHTBULB = 1, PIN_STOVE = 4
    Then make a list of them, my_pins = [PIN_LIGHTBULB, PIN_STOVE]
    Finally calling the constructor PinControl(my_pins)
    """
    pins = {}

    def __init__(self, pin_list, start_state=0):
        """
        Contructor for PinController
        Note default is all pins off
        :param pin_list: List of pins<int> which are the pins you want to control
        :param start_state: Which state you want your pins to begin in 0=off 1=on
        """

        for pin in pin_list:
            self.pins[pin] = bool(start_state)

        GPIO.setmode(GPIO.BOARD)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT, initial=start_state)

    def set_pin_high(self, pin):
        """
        Turn pin on
        :param pin: pin you want to turn on
        :return: None
        """
        GPIO.output(pin, GPIO.HIGH)
        self.pins[pin] = True

    def set_pin_low(self, pin):
        """
        Turn pin off
        :param pin: pin you want to turn off
        :return: None
        """
        GPIO.output(pin, GPIO.LOW)
        self.pins[pin] = False

    def get_pin_state(self, pin):
        """
        Checks whether pin is on or off
        :param pin: pin you want to check
        :return: False if off True if on
        """
        return self.pins[pin]
