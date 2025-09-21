import time

import pyautogui

from ZoneFinder import human_scroll_wheel


def scrollTillYouFindImage(image_path, scrolls=12, scroll_amount=-300):
    time.sleep(1)  # Quick startup
    for i in range(scrolls):
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.85)
            if location:
                pyautogui.center(location)
                print(f"✅ Clicked Book Now button at {location}")
                return "success"
        except pyautogui.ImageNotFoundException:
            pass

        # Scroll and retry
        human_scroll_wheel(total_scroll=scroll_amount)

    print(f"❌ Book Now image '{image_path}' not found after scrolling.")
    return "not_found"

def scrollTillYouFindImageAndClick(image_path, scrolls=12, scroll_amount=-300):
    time.sleep(1)  # Quick startup
    for i in range(scrolls):
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.85)
            if location:
                pyautogui.click(pyautogui.center(location))
                print(f"✅ Clicked Book Now button at {location}")
                return "success"
        except pyautogui.ImageNotFoundException:
            pass

        # Scroll and retry
        human_scroll_wheel(total_scroll=scroll_amount)

    print(f"❌ Book Now image '{image_path}' not found after scrolling.")
    return "not_found"