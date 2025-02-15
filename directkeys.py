# uncompyle6 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)]
# Embedded file name: c:\Users\ellio\Documents\Brawl_stars_AI\directkeys.py
# Compiled at: 2024-05-23 21:47:04
# Size of source mod 2**32: 2135 bytes
import ctypes, time
SendInput = ctypes.windll.user32.SendInput
W = 17
A = 30
S = 31
D = 32
M = 50
K = 37
SPACE = 87
F = 33
E = 18
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [
     (
      "wVk", ctypes.c_ushort),
     (
      "wScan", ctypes.c_ushort),
     (
      "dwFlags", ctypes.c_ulong),
     (
      "time", ctypes.c_ulong),
     (
      "dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [
     (
      "uMsg", ctypes.c_ulong),
     (
      "wParamL", ctypes.c_short),
     (
      "wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [
     (
      "dx", ctypes.c_long),
     (
      "dy", ctypes.c_long),
     (
      "mouseData", ctypes.c_ulong),
     (
      "dwFlags", ctypes.c_ulong),
     (
      "time", ctypes.c_ulong),
     (
      "dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [
     (
      "ki", KeyBdInput),
     (
      "mi", MouseInput),
     (
      "hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [
     (
      "type", ctypes.c_ulong),
     (
      "ii", Input_I)]


def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 8, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 10, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


if __name__ == "__main__":
    PressKey(17)
    time.sleep(1)
    ReleaseKey(17)
    time.sleep(1)
