
import win32api as wapi, time
keyList = [
 "\x08"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)

    if "H" in keys:
        return "H"
    if "B" in keys:
        return "B"
    if "A" in keys:
        return "A"
    if "D" in keys:
        return "D"
    if " " in keys:
        return " "
    if "S" in keys:
        return "S"
    if "E" in keys:
        return "E"
    if "W" in keys:
        return "W"
    return "None"
