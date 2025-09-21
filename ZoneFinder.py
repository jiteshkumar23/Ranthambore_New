import pyautogui
import time
import sys
import random
import os
from pyautogui import ImageNotFoundException

zone_image_path = None

# ⚡ Turbo human-like scroll
def human_scroll_wheel(total_scroll=-300, min_step=-120, max_step=-80):
    scrolled = 0
    while abs(scrolled) < abs(total_scroll):
        step = random.randint(min_step, max_step)
        pyautogui.scroll(step)
        scrolled += step
        time.sleep(random.uniform(0.01, 0.03))  # Ultra-fast pause

# 🔍 Scroll and search for zone image
def find_zone_with_scroll(image_path, scrolls=12, scroll_amount=-300):
    location = None
    time.sleep(1)  # Quick startup
    for i in range(scrolls):
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.7)
            if location:
                print(f"✅ Found zone image at {location}")
                return location
        except ImageNotFoundException:
            pass

        human_scroll_wheel(total_scroll=scroll_amount)

    print(f"❌ Zone image '{image_path}' not found after scrolling.")
    return None

def clickOnBookNowForZone(Zone_image_path,BookNow_image_path):
    # 🚀 Step 1: Locate Zone 10
    location = find_zone_with_scroll(Zone_image_path,)

    # 🎯 Step 2: Define region to the right and search for Book Now
    if location:
        x, y, w, h = location

        # Define region to the right with vertical padding ±100px
        search_region = (
            int(x + w + 30),  # Right of label
            int(y - 100),  # 100px above
            int(800),  # Width of region
            int(h + 200)  # Height: ±100px
        )

        print(f"🔍 Searching for Book Now in region: {search_region}")

        try:
            book_button = pyautogui.locateOnScreen(BookNow_image_path, region=search_region, confidence=0.7)
            if book_button:
                pyautogui.click(pyautogui.center(book_button))
                print("✅ Clicked Book Now button.")
                return "success"  # Exit after successful click
            else:
                print("❌ Book Now button not found in the defined region.")
        except ImageNotFoundException:
            print("⚠️ ImageNotFoundException: Book Now button not detected.")
    else:
        print("⚠️ Zone image not found. Skipping button search.")
