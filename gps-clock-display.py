import gpsd
import os
from pprint import pprint
import sys
import time

class gclkdsp():
    def __init__(self, host="localhost", port=2947):
        gpsd.connect(host=host, port=port)

    def start(self):
        self.looper = True
    
    def loop(self):
        while(self.looper):
            self.packet = gpsd.get_current()

    def format_data(self, screen, tz="UTC"):
        line = []
        if screen == 0:
            '''
            |0123456789ABCDEF
            |    00:00:00 UTC
            |000: 00 MON YEAR
            '''
        if screen == 1:
            '''
            |0123456789ABCDEF
            |SAT 12/14 3D FIX
            |
            '''
        if screen == 2:
            '''
            |0123456789ABCDEF
            |LAT  -40.00000
            |LON -101.00000
            '''
        if screen == 3:
            '''
            |0123456789ABCDEF
            |ALT -300.000 m
            |CLM  100.000 m/s
            '''
        if screen == 4:
            '''
            |0123456789ABCDEF
            |HDN  234.22 deg
            |SPD  101.11 m/s
            '''
