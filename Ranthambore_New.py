import os
import time

import keyboard

from CoreMethods.CoreMethods import (debounce_key, setImagePath, fillPage1, fillPage2, Payment,
                                     fillVisitorDetails, mobile, paymentFinal)


def exit_program():
    os._exit(0)  # Exit the current process


def main():
    setImagePath()
    print_instructions()

    # Add listener
    keyboard.add_hotkey('alt+w', exit_program)

    while True:
        if handle_key_press():
            print_instructions()
        time.sleep(0.1)



def print_instructions():
    print("Press - alt+1 - For filling first and second page")
    print("Press - alt+2 - For filling third and fourth page")
    print("Press - alt+3 - For filling fifth page")
    print("Press - alt+4 - For filling sixth page")
    print("Press - alt+q - For complete booking")
    print("Press - alt+w - For exiting the script")

def handle_key_press():
    if keyboard.is_pressed("alt+1"):
        print("Keys Pressed - alt+1 - Filling first page only")
        fillPage1()
        fillPage2()
        debounce_key("alt+1")  # Wait until the key is released
        return True
    elif keyboard.is_pressed("alt+2"):
        print("Keys Pressed - alt+2  - For clicking Pay and filling form")
        Payment()
        fillVisitorDetails()
        debounce_key("alt+2")  # Wait until the key is released
        return True
    elif keyboard.is_pressed("alt+3"):
        print("Keys Pressed - alt+4 - For filling fifth page")
        mobile()
        debounce_key("alt+3")  # Wait until the key is released
        return True
    elif keyboard.is_pressed("alt+4"):
        print("Keys Pressed - alt+5 - For filling sixth page")
        paymentFinal()
        debounce_key("alt+4")  # Wait until the key is released
        return True
    elif keyboard.is_pressed("alt+q"):
        print("Keys Pressed - alt+q - for complete booking")
        fillPage1()
        fillPage2()
        Payment()
        fillVisitorDetails()
        mobile()
        paymentFinal()
        debounce_key("alt+q")  # Wait until the key is released
        return True
    return False

if __name__ == "__main__":
    main()
