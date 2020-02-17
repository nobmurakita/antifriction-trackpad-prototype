#!/usr/bin/env python

from corefoundation import *
from coregraphics import *
from multitouch import *
from collections import deque
from math import sqrt
from time import time, sleep

class App:
    def __init__(self):
        self.history = deque(maxlen=2)
        self.is_touched = False
        self.vx = 0
        self.vy = 0
    
    def start(self):
        self.devices = self.get_devices()
        callback = MTContactCallbackFunction(self.callback)
        try:
            self.start_devices(callback)
            self.main_loop()
        except KeyboardInterrupt:
            pass
        finally:
            self.stop_devices(callback)

    def main_loop(self):
        t1 = time()
        while True:
            sleep(0.01)
            t2 = time()
            dt = t2 - t1
            t1 = t2
            if self.vx != 0 or self.vy != 0:
                self.move_mouse(self.vx * dt, self.vy * dt)
                self.decelerate_mouse(5 * dt)

    def get_devices(self):
        devices = MTDeviceCreateList()
        n = CFArrayGetCount(devices)
        return [CFArrayGetValueAtIndex(devices, i) for i in xrange(n)]

    def start_devices(self, callback):
        for device in self.devices:
            MTRegisterContactFrameCallback(device, callback)
            MTDeviceStart(device, 0)

    def stop_devices(self, callback):
        for device in self.devices:
            MTDeviceStop(device, 0)
            MTUnregisterContactFrameCallback(device, callback)

    def callback(self, device, data, data_num, timestamp, frame):
        is_touched = False
        for i in xrange(data_num):
            if data[i].state == 4:
                is_touched = True
                break

        if is_touched:
            pos = self.get_mouse_location()
            self.history.append((pos.x, pos.y, timestamp))
            self.vx = 0
            self.vy = 0

        if self.is_touched and not is_touched:
            if len(self.history) >= 2:
                (ex, ey, et) = self.history.pop()
                (sx, sy, st) = self.history.pop()
                self.vx = (ex - sx) / (et - st)
                self.vy = (ey - sy) / (et - st)
            self.history.clear()

        self.is_touched = is_touched

        return 0

    def decelerate_mouse(self, r):
        self.vx *= 1 - r
        self.vy *= 1 - r
        if sqrt(self.vx ** 2 + self.vy ** 2) < 10:
            self.vx = 0
            self.vy = 0

    def get_mouse_location(self):
        event = CGEventCreate(None)
        pos = CGEventGetLocation(event)
        CFRelease(event)
        return pos

    def set_mouse_location(self, pos):
        event = CGEventCreateMouseEvent(None, kCGEventMouseMoved, pos, 0)
        CGEventPost(kCGHIDEventTap, event)
        CFRelease(event)

    def move_mouse(self, dx, dy):
        pos = self.get_mouse_location()
        pos.x += dx
        pos.y += dy
        self.set_mouse_location(pos)

if __name__ == "__main__":
    app = App()
    app.start()
