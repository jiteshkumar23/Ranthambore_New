import pyautogui
import time
from pyautogui import ImageNotFoundException

from config import machine


# 🔍 Locate zone using arrow keys only
def find_zone_with_arrow_keys(image_path, max_attempts=60, direction='down', presses_per_attempt=2):
    for attempt in range(max_attempts):
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                print(f"✅ Found zone image at {location}")
                pyautogui.press('down', presses=3)
                print("i am after five downs")
                location2 = pyautogui.locateOnScreen(image_path, confidence=0.8)
                print("i am after location")
                return location2
        except ImageNotFoundException as e:
                print(f"⚠️ ImageNotFoundException: {e}")
        print(f"🔄 Attempt {attempt + 1}: Pressing {direction} {presses_per_attempt} times")
        pyautogui.press(direction, presses=presses_per_attempt)
        # time.sleep(0.1)  # Let UI settle

    print(f"❌ Zone image '{image_path}' not found after {max_attempts} arrow key attempts.")
    return None

# 🎯 Locate and click Book Now button near the zone
def clickOnBookNowForZone(Zone_image_path, BookNow_image_path):
    location = find_zone_with_arrow_keys(Zone_image_path, direction='down')

    if location:
        x, y, w, h = location

        if machine == 'laptop':
            search_region = (
                int(x),  # Slightly left of the zone block
                int(y),  # Extend upward to catch misaligned buttons
                200,  # Wider area to the right
                int(h + 200)  # Taller area below the zone block
            )
        elif machine == 'desktop':
            search_region = (
                int(x),  # Slightly left of the zone block
                int(y),  # Extend upward to catch misaligned buttons
                600,  # Wider area to the right
                int(h + 200)  # Taller area below the zone block
            )

        time.sleep(0.25)
        # pyautogui.screenshot(region=search_region).save("book_button_area.png")
        print(f"🔍 Searching for Book Now in region: {search_region}")

        try:
            book_button = pyautogui.locateOnScreen(BookNow_image_path, region=search_region, confidence=0.7)
            if book_button:
                pyautogui.click(pyautogui.center(book_button))
                print("✅ Clicked Book Now button.")
                return "success"
            else:
                print("❌ Book Now button not found in the defined region.")
        except ImageNotFoundException:
            print("⚠️ ImageNotFoundException: Book Now button not detected.")
            clickOnBookNowForZone(Zone_image_path, BookNow_image_path)
    else:
        print("⚠️ Zone image not found. Skipping button search.")

def multiplePressUsingPyAutoGUINew(key, times):
    print("pressing " + " " + key + " " + str(times))
    pyautogui.press(key, presses=times)