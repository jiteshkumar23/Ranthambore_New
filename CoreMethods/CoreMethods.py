import datetime
import os
import random
import string
import time
import tkinter as tk
from datetime import datetime
from tkinter import simpledialog
import cv2
import keyboard
import numpy as np
import pyautogui
from autoit import autoit
import datetime
import pyperclip

from pyautogui import moveTo

from config import delay_correct, delay_error, paxOfPerson1, machine, nameOfPerson1, \
    idTypeOfPerson1, idNumberOfPerson1, genderOfPerson1, paxOfPerson2, nameOfPerson2, idTypeOfPerson2, \
    idNumberOfPerson2, genderOfPerson2, paxOfPerson3, nameOfPerson3, idTypeOfPerson3, \
    idNumberOfPerson3, genderOfPerson3, paxOfPerson4, nameOfPerson4, idTypeOfPerson4, \
    idNumberOfPerson4, genderOfPerson4, paxOfPerson5, nameOfPerson5, idTypeOfPerson5, \
    idNumberOfPerson5, genderOfPerson5, paxOfPerson6, nameOfPerson6, idTypeOfPerson6, \
    idNumberOfPerson6, genderOfPerson6, paxOfPerson7, nameOfPerson7, idTypeOfPerson7, \
    idNumberOfPerson7, genderOfPerson7, paxOfPerson8, nameOfPerson8, idTypeOfPerson8, \
    idNumberOfPerson8, genderOfPerson8, paxOfPerson9, nameOfPerson9, idTypeOfPerson9, \
    idNumberOfPerson9, genderOfPerson9, paxOfPerson10, nameOfPerson10, idTypeOfPerson10, \
    idNumberOfPerson10, genderOfPerson10, genderOfPerson20, idNumberOfPerson20, idTypeOfPerson20, \
    nameOfPerson20, paxOfPerson20, genderOfPerson19, idNumberOfPerson19, idTypeOfPerson19, \
    nameOfPerson19, paxOfPerson19, genderOfPerson18, idNumberOfPerson18, idTypeOfPerson18, \
    nameOfPerson18, paxOfPerson18, genderOfPerson17, idNumberOfPerson17, idTypeOfPerson17, \
    nameOfPerson17, paxOfPerson17, genderOfPerson16, idNumberOfPerson16, idTypeOfPerson16, \
    nameOfPerson16, paxOfPerson16, genderOfPerson15, idNumberOfPerson15, idTypeOfPerson15, \
    nameOfPerson15, paxOfPerson15, genderOfPerson14, idNumberOfPerson14, idTypeOfPerson14, \
    nameOfPerson14, paxOfPerson14, genderOfPerson13, idNumberOfPerson13, idTypeOfPerson13, \
    nameOfPerson13, paxOfPerson13, genderOfPerson12, idNumberOfPerson12, idTypeOfPerson12, \
    nameOfPerson12, paxOfPerson12, genderOfPerson11, idNumberOfPerson11, idTypeOfPerson11, \
    nameOfPerson11, paxOfPerson11, speed, timer, zone, slot, indian_count, \
    non_indian_count, \
    ageOfPerson1, ageOfPerson2, ageOfPerson3, ageOfPerson4, ageOfPerson5, ageOfPerson6, ageOfPerson7, ageOfPerson8, \
    ageOfPerson9, ageOfPerson10, ageOfPerson11, ageOfPerson12, ageOfPerson13, ageOfPerson14, ageOfPerson15, \
    ageOfPerson16, ageOfPerson17, ageOfPerson18, ageOfPerson19, ageOfPerson20, \
    attachmentNameOfPerson1, attachmentNameOfPerson2, attachmentNameOfPerson3, attachmentNameOfPerson4, \
    attachmentNameOfPerson5, attachmentNameOfPerson6, attachmentNameOfPerson7, attachmentNameOfPerson8, \
    attachmentNameOfPerson9, attachmentNameOfPerson10, attachmentNameOfPerson11, attachmentNameOfPerson12, \
    attachmentNameOfPerson13, attachmentNameOfPerson14, attachmentNameOfPerson15, attachmentNameOfPerson16, \
    attachmentNameOfPerson17, attachmentNameOfPerson18, attachmentNameOfPerson19, attachmentNameOfPerson20, \
    mobileNumber, paymentMethod, UPI_ADDRESS, usePluginForVisitorDetails

global image_directory, MorningGypsy_image_path,PleaseSelect_image_path, \
    MorningCanter_image_path,minus_image_path,PayButton_image_path,instructions_image_path,agree_image_path,\
    Visitor1_image_path,OK_image_path,ContinueGreen_image_path,mobile_image_path,PayAfterMobile_image_path,\
    SelectPaymentOption_image_path,UPI_image_path, \
    PayNow_image_path, email_image_path, \
    continue_image_path, contactdetails_image_path, showQR_image_path, \
    recommended_image_path, creditcard_image_path, payViaCard_image_path, \
    addANewCard_image_path, rooms_image_path, PaymentOptions_image_path, proceedAfterTiger_image_path, \
    UPIQR_AfterTiger_image_path, \
    showQR_AfterTiger_image_path, UPI_ID_image_path, UPI_ID_Image2_image_path, gender_dropdown_image_path, \
    id_details_image_path, age_image_path, fullname_image_path, \
    id_proof_not_selected_image_path, emailAddress_image_path, emailAddress_2_image_path, \
    UPIOnRazorPay_image_path,FileNamePopup_image_path

timeStart1, timeEnd1, timer1 = '0:0:0.0', '0:0:0.0', timer
timeStart2, timeEnd2, timer2 = '0:0:0.0', '0:0:0.0', timer
timeStart3, timeEnd3, timer3 = '0:0:0.0', '0:0:0.0', timer
timeStart4, timeEnd4, timer4 = '0:0:0.0', '0:0:0.0', timer
timeStart5, timeEnd5, timer5 = '0:0:0.0', '0:0:0.0', timer
timeStart6, timeEnd6, timer6 = '0:0:0.0', '0:0:0.0', timer
timeStart7, timeEnd7, timer7 = '0:0:0.0', '0:0:0.0', timer
timeStart8, timeEnd8, timer8 = '0:0:0.0', '0:0:0.0', timer
timeStart9, timeEnd9, timer9 = '0:0:0.0', '0:0:0.0', timer
timeStart10, timeEnd10, timer10 = '0:0:0.0', '0:0:0.0', timer
timeStart11, timeEnd11, timer11 = '0:0:0.0', '0:0:0.0', timer
timeStart12, timeEnd12, timer12 = '0:0:0.0', '0:0:0.0', timer
timeStart13, timeEnd13, timer13 = '0:0:0.0', '0:0:0.0', timer
timeStart14, timeEnd14, timer14 = '0:0:0.0', '0:0:0.0', timer
timeStart15, timeEnd15, timer15 = '0:0:0.0', '0:0:0.0', timer
timeStart16, timeEnd16, timer16 = '0:0:0.0', '0:0:0.0', timer
timeStart17, timeEnd17, timer17 = '0:0:0.0', '0:0:0.0', timer
timeStart18, timeEnd18, timer18 = '0:0:0.0', '0:0:0.0', timer
timeStart19, timeEnd19, timer19 = '0:0:0.0', '0:0:0.0', timer
timeStart20, timeEnd20, timer20 = '0:0:0.0', '0:0:0.0', timer

countOfPersons = indian_count + non_indian_count


def fillPage1():
    print("Hello, this is Page 1")
    autoit.send("!i")
    time.sleep(0.5)
    multiplePressUsingPyAutoGUI('pagedown', 1)
    time.sleep(0.5)
    find_image_on_screen_using_opencv(BookNow_image_path, 10)
    if zone == "Zone 6":
        autoit.send("!o")  # Alt + O
    elif zone == "Zone 7":
        autoit.send("+1")  # Shift + 1 → "!"
    elif zone == "Zone 8":
        autoit.send("+[")  # Shift + [ → depends on layout
    elif zone == "Zone 9":
        autoit.send("+3")  # Shift + 3 → "#"
    elif zone == "Zone 10":
        autoit.send("+4")  # Shift + 4 → "$"
    elif zone == "Zone 1":
        autoit.send("+5")  # Shift + 5 → "%"
    elif zone == "Zone 2":
        autoit.send("+6")  # Shift + 6 → "^"
    elif zone == "Zone 3":
        autoit.send("+7")  # Shift + 7 → "&"
    elif zone == "Zone 4":
        autoit.send("+8")  # Shift + 8 → "*"
    elif zone == "Zone 5":
        autoit.send("+9")  # Shift + 9 → "("

def fillPage2():
    print("Hello, this is Page 2")
    find_image_on_screen_using_opencv(PleaseSelect_image_path, 20)
    if slot.lower() == "morning gypsy":
        autoit.send("+0")  # Shift + 0 → ")"
    elif slot.lower() == "afternoon gypsy":
        autoit.send("+]")  # Shift + ] → Depending on layout, often "}"
    elif slot.lower() == "morning canter":
        autoit.send("+w")  # Shift + W → "W"
    elif slot.lower() == "afternoon canter":
        autoit.send("!p")  # Alt + P

    find_image_on_screen_using_opencv(minus_image_path, 6)
    time.sleep(0.5)
    multiplePressUsingPyAutoGUI('tab',3)
    if indian_count > 0:
        multiplePressUsingPyAutoGUI('backspace', 1)
        time.sleep(0.2)
        pyautogui.typewrite(str(indian_count))
    multiplePressUsingPyAutoGUI('tab', 1)
    if non_indian_count > 0:
        multiplePressUsingPyAutoGUI('backspace', 1)
        time.sleep(0.2)
        pyautogui.typewrite(str(non_indian_count))

    time.sleep(0.5)
    pyautogui.click(find_image_on_screen_using_opencv(OK_image_path, 6))


def Payment():
    pyautogui.click(find_image_on_screen_using_opencv(PayButton_image_path, 6))
    time.sleep(0.2)

    find_image_on_screen_using_opencv(instructions_image_path, 6)
    time.sleep(0.2)
    autoit.send("!q")  # Alt + Q

    multiplePressUsingPyAutoGUI('pagedown', 1)
    time.sleep(0.1)
    # pyautogui.click(find_image_on_screen_using_opencv(agree_image_path, 6))
    autoit.send("!r")  # Alt + R


def fillVisitorDetails():
    global flag
    print(usePluginForVisitorDetails)
    print("Hello, this is Visitor Details")
    print("Execution Started At: ", getDateTime())
    pyautogui.click(find_image_on_screen_using_opencv(Visitor1_image_path, 10))
    multiplePressUsingPyAutoGUI('tab',2)
    persons_list = get_persons_list()
    if usePluginForVisitorDetails.lower() == "yes":
        flag = True
    else:
        flag = False
    if flag:
        autoit.send("!k")  # Alt + K
        time.sleep(1)

        for i in range(int(countOfPersons)):
            person = persons_list[i]
            speed_for_first_page(speed)

            print('about to press alt+m')
            autoit.send("!m")  # Alt + M

            find_image_on_screen_using_opencv_color(FileNamePopup_image_path, 5)
            time.sleep(0.2)

            pyperclip.copy(person['attachmentName'])
            autoit.send("^v")  # Ctrl + V
            autoit.send("{ENTER}")  # Press Enter
            time.sleep(2)

    else:
        for i in range(int(countOfPersons)):
            person = persons_list[i]
            # Set time Start here
            speed_for_first_page(speed)
            # human_typing(person['name'].strip())

            pyperclip.copy(person['name'].strip())
            autoit.send("^v")
            speed_for_first_page(speed)
            autoit.send("{TAB}")
            speed_for_first_page(speed)

            selectGenderDropdown(person['gender'])
            speed_for_first_page(speed)
            autoit.send("{TAB}")

            selectPaxDropdown(person['pax'])
            speed_for_first_page(speed)
            autoit.send("{TAB}")
            speed_for_first_page(speed)

            selectIdentityProofDropdown(person['idType'])
            speed_for_first_page(speed)
            autoit.send("{TAB}")
            speed_for_first_page(speed)
            # human_typing(person['idNumber'].strip())

            pyperclip.copy(person['idNumber'].strip())
            autoit.send("^v")
            speed_for_first_page(speed)
            autoit.send("{TAB}")
            speed_for_first_page(speed)
            # human_typing(person['age'].strip())

            pyperclip.copy(person['age'].strip())
            autoit.send("^v")
            speed_for_first_page(speed)
            time.sleep(0.25)
            speed_for_first_page(speed)
            autoit.send("{TAB}")
            autoit.send("{ENTER}")
            find_image_on_screen_using_opencv_color(FileNamePopup_image_path, 5)
            time.sleep(0.2)
            # pyautogui.typewrite(person['attachmentName'])
            # autoit.send((person['attachmentName']))
            pyperclip.copy(person['attachmentName'])
            autoit.send("^v")
            autoit.send("{ENTER}")
            time.sleep(2)
            if i == int(countOfPersons) - 1:
                print("No Tabs")
            else:
                autoit.send("{TAB}")
                autoit.send("{TAB}")

   # performFunctionUntilImageIsFound(mobile_image_path,60)
    multiplePressUsingPyAutoGUI('pagedown', 10)
    pyautogui.click(find_image_on_screen_using_opencv(ContinueGreen_image_path, 60,0.95))
    print("Execution Ended (form filling)  At: ", getDateTime())

def mobile():
    pyautogui.click(find_image_on_screen_using_opencv(mobile_image_path, 10))
    autoit.send(mobileNumber)
    # pyautogui.click(find_image_on_screen_using_opencv_color(PayAfterMobile_image_path, 60,0.95))


def paymentFinal():
    location = find_image_on_screen_using_opencv(SelectPaymentOption_image_path, 300)
    pyautogui.click(location)
    if paymentMethod == "upi" or paymentMethod == "upi_id":
        location2 = find_image_on_screen_using_opencv(UPI_image_path, 30)
        pyautogui.click(location2)
        print("clicked on UPI")
        # location3 = find_image_on_screen_using_opencv(PayNow_image_path, 60)
        # pyautogui.click(location3)
        time.sleep(0.1)
        autoit.send("{TAB}")
        time.sleep(0.1)
        autoit.send("{ENTER}")
        print("clicked on Pay Now button")
        find_image_on_screen_using_opencv_color(PaymentOptions_image_path, 60)
        time.sleep(0.5)
        pyautogui.click(find_image_on_screen_using_opencv_color(UPIOnRazorPay_image_path, 60, 0.95))
        if paymentMethod == "upi":
            time.sleep(0.2)
            location6 = find_image_on_screen_using_opencv(showQR_image_path, 10)
            print("show QR was displayed")
            pyautogui.click(location6)
        elif paymentMethod == "upi_id":
            location6 = find_image_on_screen_using_opencv(UPI_ID_image_path, 10)
            print("UPI_ID was displayed")
            pyautogui.click(location6)
            time.sleep(0.1)
            pyperclip.copy(UPI_ADDRESS)
            autoit.send("^v")
            time.sleep(0.25)
            autoit.send("{TAB}")
            time.sleep(0.1)
            autoit.send("{ENTER}")



def printDateTime():
    print(f"Time: {datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]}")


def getDateTime():
    return datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]


def getTimeDiff(timeStart2, timeStart):
    # Calculate the difference
    fmt = "%H:%M:%S.%f"
    start_dt = datetime.datetime.strptime(timeStart, fmt)
    end_dt = datetime.datetime.strptime(timeStart2, fmt)
    diff = end_dt - start_dt
    print("Difference is : ", diff)
    return diff


def multiplePressUsingPyAutoGUI(key, times):
    print("pressing " + " " + key + " " + str(times))
    pyautogui.press(key, presses=times)


def speed_for_first_page(speed):
    time.sleep(speed)

def wait_for_image_and_click(image_path, timeout_duration=60, check_interval=0.001):
    timeout_end = time.time() + timeout_duration

    print(f"Waiting for {image_path} to appear on the screen...")

    while time.time() < timeout_end:
        try:
            # Locate the image on the screen
            location = pyautogui.locateCenterOnScreen(image_path, grayscale=True)

            # If the image is found, click on it and break the loop
            if location is not None:
                print(f"Image found at {location}, clicking on it...")
                pyautogui.click(location)
                break
        except pyautogui.ImageNotFoundException:
            # Handle the case where the image is not found
            print(f"Image not found: {image_path}")

        # Wait for the specified interval before checking again
        time.sleep(check_interval)
    else:
        print("Timeout reached. Image not found.")

    print("Task completed.")
    return location


def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    user_input = None

    while user_input != "1":
        user_input = simpledialog.askstring("Input", "Enter 1 to continue:")
        if user_input is None:  # User closed the dialog
            print("User cancelled the input.")
            root.destroy()
            exit()

    root.destroy()  # Close the popup


def click_on_image_in_region(left, top, width, height, image):
    time.sleep(1)
    # Define the region of interest (left, top, width, height)
    region = (left, top, width, height)
    # Print debug information
    print(f"Capturing screenshot of region: {region}")

    # Capture a screenshot of the region
    screenshot = pyautogui.screenshot(region=region)

    # Print debug information
    print("Searching for image 'indian_flag.png' within the captured region...")

    try:
        # Locate the image 'indian_flag.png' within the specified region on the screen
        image_location = pyautogui.locateOnScreen(image, region=region)

        if image_location is not None:
            # Click in the center of the image location
            center = pyautogui.center(image_location)
            pyautogui.click(center)
            print("Image found and clicked.")
        else:
            print("Image not found in the specified region.")
    except pyautogui.ImageNotFoundException:
        print("Image not found on the screen.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def human_typing(text):
    for char in text:
        autoit.send(char)
        time.sleep(delay_correct)


def human_typing_age(text):
    for char in text:
        autoit.send(char)
        time.sleep(delay_correct + 0.1)


def autoit_slow_type_with_error(text):
    # Choose a random position to make a typing error
    error_position = random.randint(0, len(text) - 1)
    # Choose a random alphabet as the incorrect character
    wrong_character = random.choice(string.ascii_lowercase)

    for i, character in enumerate(text):
        if i == error_position:
            # Type the wrong random character
            autoit.send(wrong_character)
            # Backspace to delete the wrong character
            time.sleep(delay_error)
            autoit.send("{BACKSPACE}")
            time.sleep(delay_correct)
        # Type the correct character
        autoit.send(character)
        time.sleep(delay_correct)


def autoit_slow_type_numbers_with_error(numbers):
    if not numbers:  # Check if numbers is None or empty
        return
    # Choose a random position to make a typing error
    error_position = random.randint(0, len(numbers) - 1)
    # Choose a random digit as the incorrect character
    wrong_character = random.choice(string.digits)

    for i, character in enumerate(numbers):
        if i == error_position:
            # Type the wrong random character
            autoit.send(wrong_character)
            # Backspace to delete the wrong character
            time.sleep(delay_error)
            autoit.send("{BACKSPACE}")
            time.sleep(delay_correct)
            # Additional delay for the correction
        # Type the correct character
        autoit.send(character)
        time.sleep(delay_correct)


def custom_hotkey():
    # Define your desired hotkey combination
    return keyboard.is_pressed("ctrl+alt+x")  # Example: Ctrl+Alt+X


def debounce_key(key):
    # Wait for key release
    while keyboard.is_pressed(key):
        pass


def find_image_on_screen_using_opencv(template_path1, timeout, threshold=0.7):
    template = cv2.imread(template_path1, 0)
    w, h = template.shape[::-1]
    start_time = time.time()

    while True:
        # Capture a screenshot
        screenshot = pyautogui.screenshot()

        # Convert screenshot to numpy array and then to grayscale
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

        # Perform template matching
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Check if the match value is above the threshold
        if max_val >= threshold:
            # Return the location of the matched region
            print("Image found ->"+template_path1)
            return max_loc[0], max_loc[1], w, h

        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            return None
        print("Image Searching for "+template_path1)
        time.sleep(0.01)


def performFunctionUntilImageIsFound(template_path1, timeout, threshold=0.7):
    template = cv2.imread(template_path1, 0)
    w, h = template.shape[::-1]
    start_time = time.time()

    while True:
        # Capture a screenshot
        screenshot = pyautogui.screenshot()

        # Convert screenshot to numpy array and then to grayscale
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

        # Perform template matching
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Check if the match value is above the threshold
        if max_val >= threshold:
            # Return the location of the matched region
            print("Image found ->"+template_path1)
            return max_loc[0], max_loc[1], w, h

        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            return None
        print("Image Searching for "+template_path1)
        time.sleep(0.5)
        clickContinueButton()

def clickContinueButton():
    autoit.send("!s")  # Sends Alt + S


def setImagePath():
    global image_directory
    if machine == "laptop" or machine == "pradeeplaptop":
        image_directory = os.getcwd() + '\\images_laptop'
    elif machine == "desktop" or machine == "rohit":
        image_directory = os.getcwd() + '\\images_desktop'

    global RanthamboreTigerReserve_image_path
    RanthamboreTigerReserve_image_path = os.path.join(image_directory, 'RanthamboreTigerReserve.png')

    global selectTouristType_image_path
    selectTouristType_image_path = os.path.join(image_directory, 'selectTouristType.png')

    global agreeToCancellation_image_path
    agreeToCancellation_image_path = os.path.join(image_directory, 'agreeToCancellation.png')

    global agreeToTermsConditions_image_path
    agreeToTermsConditions_image_path = os.path.join(image_directory, 'agreeToTermsConditions.png')

    global MemberDetails_image_path
    MemberDetails_image_path = os.path.join(image_directory, 'MemberDetails.png')

    global UploadDocument_image_path
    UploadDocument_image_path = os.path.join(image_directory, 'UploadDocument.png')

    global MorningGypsy_image_path
    MorningGypsy_image_path = os.path.join(image_directory, 'MorningGypsy.png')

    global MorningCanter_image_path
    MorningCanter_image_path = os.path.join(image_directory, 'MorningCanter.png')

    global minus_image_path
    minus_image_path = os.path.join(image_directory, 'minus.png')

    global PayButton_image_path
    PayButton_image_path = os.path.join(image_directory, 'PayButton.png')

    global instructions_image_path
    instructions_image_path = os.path.join(image_directory, 'instructions.png')

    global agree_image_path
    agree_image_path = os.path.join(image_directory, 'agree.png')

    global Visitor1_image_path
    Visitor1_image_path = os.path.join(image_directory, 'Visitor1.png')

    global OK_image_path
    OK_image_path = os.path.join(image_directory, 'OK.png')

    global BookNow_image_path
    BookNow_image_path = os.path.join(image_directory, 'BookNow.png')

    global ContinueGreen_image_path
    ContinueGreen_image_path = os.path.join(image_directory, 'ContinueGreen.png')

    global mobile_image_path
    mobile_image_path = os.path.join(image_directory, 'mobile.png')

    global PayAfterMobile_image_path
    PayAfterMobile_image_path = os.path.join(image_directory, 'PayAfterMobile.png')

    global SelectPaymentOption_image_path
    SelectPaymentOption_image_path = os.path.join(image_directory, 'SelectPaymentOption.png')

    global UPI_image_path
    UPI_image_path = os.path.join(image_directory, 'UPI.png')

    global PayNow_image_path
    PayNow_image_path = os.path.join(image_directory, 'PayNow.png')

    global email_image_path
    email_image_path = os.path.join(image_directory, 'email.png')

    global continue_image_path
    continue_image_path = os.path.join(image_directory, 'continue.png')

    global contactdetails_image_path
    contactdetails_image_path = os.path.join(image_directory, 'contactdetails.png')

    global showQR_image_path
    showQR_image_path = os.path.join(image_directory, 'showQR.png')

    global recommended_image_path
    recommended_image_path = os.path.join(image_directory, 'recommended.png')

    global creditcard_image_path
    creditcard_image_path = os.path.join(image_directory, 'credit_debit_card.png')

    global payViaCard_image_path
    payViaCard_image_path = os.path.join(image_directory, 'payViaCard.png')

    global addANewCard_image_path
    addANewCard_image_path = os.path.join(image_directory, 'addANewCard.png')

    global rooms_image_path
    rooms_image_path = os.path.join(image_directory, 'rooms.png')

    global PaymentOptions_image_path
    PaymentOptions_image_path = os.path.join(image_directory, 'PaymentOptions.png')

    global proceedAfterTiger_image_path
    proceedAfterTiger_image_path = os.path.join(image_directory, 'proceedAfterTiger.png')

    global UPIQR_AfterTiger_image_path
    UPIQR_AfterTiger_image_path = os.path.join(image_directory, 'UPIQR_AfterTiger.png')

    global showQR_AfterTiger_image_path
    showQR_AfterTiger_image_path = os.path.join(image_directory, 'showQR_AfterTiger.png')

    global UPI_ID_image_path
    UPI_ID_image_path = os.path.join(image_directory, 'UPI_ID.png')

    global UPI_ID_Image2_image_path
    UPI_ID_Image2_image_path = os.path.join(image_directory, 'UPI_ID_Image2.png')

    global UPI_Number_FirstImage_image_path
    UPI_Number_FirstImage_image_path = os.path.join(image_directory, 'UPI_Number_FirstImage.png')

    global gender_dropdown_image_path
    gender_dropdown_image_path = os.path.join(image_directory, 'gender_dropdown.png')

    global id_details_image_path
    id_details_image_path = os.path.join(image_directory, 'id_details.png')

    global age_image_path
    age_image_path = os.path.join(image_directory, 'age.png')

    global fullname_image_path
    fullname_image_path = os.path.join(image_directory, 'fullname.png')

    global id_proof_not_selected_image_path
    id_proof_not_selected_image_path = os.path.join(image_directory, 'id_proof_not_selected.png')

    global emailAddress_image_path
    emailAddress_image_path = os.path.join(image_directory, 'emailAddress.png')

    global emailAddress_2_image_path
    emailAddress_2_image_path = os.path.join(image_directory, 'emailAddress_2.png')

    global UPIOnRazorPay_image_path
    UPIOnRazorPay_image_path = os.path.join(image_directory, 'UPIOnRazorPay.png')

    global PleaseSelect_image_path
    PleaseSelect_image_path = os.path.join(image_directory, 'PleaseSelect.png')

    global FileNamePopup_image_path
    FileNamePopup_image_path = os.path.join(image_directory, 'FileNamePopup.png')



def days_difference_with_checkInDate(checkOutDate1):
    # Define the dates
    current_date = datetime.now()
    compare_date = datetime(2024, 11, 15)

    # Get the higher date
    higher_date = max(current_date, compare_date)

    # Parse checkOutDate
    checkOutDate1 = datetime.strptime(checkOutDate1, "%Y-%m-%d")

    # Calculate the difference in days
    difference_in_days = abs((checkOutDate1 - higher_date).days)
    return difference_in_days


def days_difference_with_checkInDate_checkOutDate(checkInDate1, checkOutDate1):
    # Convert strings to datetime objects if they aren't already
    if isinstance(checkInDate1, str):
        checkInDate1 = datetime.strptime(checkInDate1, "%Y-%m-%d")
    if isinstance(checkOutDate1, str):
        checkOutDate1 = datetime.strptime(checkOutDate1, "%Y-%m-%d")

    # Calculate the difference in days and ensure it's positive
    difference_in_days = abs((checkOutDate1 - checkInDate1).days) - 1
    return difference_in_days


def selectPaxDropdown(case_value):
    autoit.send("{ENTER}")
    if case_value.lower() == "indian":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("in")
        autoit.send("{ENTER}")
    elif case_value.lower() == "foreigner":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("fo")
        autoit.send("{ENTER}")


def selectIdentityProofDropdown(case_value):
    autoit.send("{ENTER}")
    val = case_value.lower()
    if val in ["aadhar card", "aadhaar card", "aadhar"]:
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("aad")
        autoit.send("{ENTER}")
    elif val == "passport":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("pas")
        autoit.send("{ENTER}")
    elif val in ["indian voter card", "indian voter id", "voter card", "voter id"]:
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("ind")
        autoit.send("{ENTER}")
    elif val == "pan card":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("pan")
        autoit.send("{ENTER}")

def selectGenderDropdown(case_value):
    autoit.send("{ENTER}")
    if case_value.lower() == "male":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("ma")
        autoit.send("{ENTER}")
    elif case_value.lower() == "female":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("fe")
        autoit.send("{ENTER}")


def get_persons_list():
    persons = []

    persons.append({
        "pax": paxOfPerson1,
        "name": nameOfPerson1,
        "idType": idTypeOfPerson1,
        "idNumber": idNumberOfPerson1,
        "gender": genderOfPerson1,
        "age": ageOfPerson1,
        "attachmentName": attachmentNameOfPerson1,
    })

    persons.append({
        "pax": paxOfPerson2,
        "name": nameOfPerson2,
        "idType": idTypeOfPerson2,
        "idNumber": idNumberOfPerson2,
        "gender": genderOfPerson2,
        "age": ageOfPerson2,
        "attachmentName": attachmentNameOfPerson2,
    })

    persons.append({
        "pax": paxOfPerson3,
        "name": nameOfPerson3,
        "idType": idTypeOfPerson3,
        "idNumber": idNumberOfPerson3,
        "gender": genderOfPerson3,
        "age": ageOfPerson3,
        "attachmentName": attachmentNameOfPerson3,
    })

    # Person 4
    persons.append({
        "pax": paxOfPerson4,
        "name": nameOfPerson4,
        "idType": idTypeOfPerson4,
        "idNumber": idNumberOfPerson4,
        "gender": genderOfPerson4,
        "age": ageOfPerson4,
        "attachmentName": attachmentNameOfPerson4,
    })

    # Person 5
    persons.append({
        "pax": paxOfPerson5,
        "name": nameOfPerson5,
        "idType": idTypeOfPerson5,
        "idNumber": idNumberOfPerson5,
        "gender": genderOfPerson5,
        "age": ageOfPerson5,
        "attachmentName": attachmentNameOfPerson5,
    })

    # Person 6
    persons.append({
        "pax": paxOfPerson6,
        "name": nameOfPerson6,
        "idType": idTypeOfPerson6,
        "idNumber": idNumberOfPerson6,
        "gender": genderOfPerson6,
        "age": ageOfPerson6,
        "attachmentName": attachmentNameOfPerson6,
    })

    # Person 7
    persons.append({
        "pax": paxOfPerson7,
        "name": nameOfPerson7,
        "idType": idTypeOfPerson7,
        "idNumber": idNumberOfPerson7,
        "gender": genderOfPerson7,
        "age": ageOfPerson7,
        "attachmentName": attachmentNameOfPerson7,
    })

    # Person 8
    persons.append({
        "pax": paxOfPerson8,
        "name": nameOfPerson8,
        "idType": idTypeOfPerson8,
        "idNumber": idNumberOfPerson8,
        "gender": genderOfPerson8,
        "age": ageOfPerson8,
        "attachmentName": attachmentNameOfPerson8,
    })

    # Person 9
    persons.append({
        "pax": paxOfPerson9,
        "name": nameOfPerson9,
        "idType": idTypeOfPerson9,
        "idNumber": idNumberOfPerson9,
        "gender": genderOfPerson9,
        "age": ageOfPerson9,
        "attachmentName": attachmentNameOfPerson9,
    })

    # Person 10
    persons.append({
        "pax": paxOfPerson10,
        "name": nameOfPerson10,
        "idType": idTypeOfPerson10,
        "idNumber": idNumberOfPerson10,
        "gender": genderOfPerson10,
        "age": ageOfPerson10,
        "attachmentName": attachmentNameOfPerson10,
    })

    # Person 11
    persons.append({
        "pax": paxOfPerson11,
        "name": nameOfPerson11,
        "idType": idTypeOfPerson11,
        "idNumber": idNumberOfPerson11,
        "gender": genderOfPerson11,
        "age": ageOfPerson11,
        "attachmentName": attachmentNameOfPerson11,
    })

    # Person 12
    persons.append({
        "pax": paxOfPerson12,
        "name": nameOfPerson12,
        "idType": idTypeOfPerson12,
        "idNumber": idNumberOfPerson12,
        "gender": genderOfPerson12,
        "age": ageOfPerson12,
        "attachmentName": attachmentNameOfPerson12,
    })

    # Person 13
    persons.append({
        "pax": paxOfPerson13,
        "name": nameOfPerson13,
        "idType": idTypeOfPerson13,
        "idNumber": idNumberOfPerson13,
        "gender": genderOfPerson13,
        "age": ageOfPerson13,
        "attachmentName": attachmentNameOfPerson13,
    })

    # Person 14
    persons.append({
        "pax": paxOfPerson14,
        "name": nameOfPerson14,
        "idType": idTypeOfPerson14,
        "idNumber": idNumberOfPerson14,
        "gender": genderOfPerson14,
        "age": ageOfPerson14,
        "attachmentName": attachmentNameOfPerson14,
    })

    # Person 15
    persons.append({
        "pax": paxOfPerson15,
        "name": nameOfPerson15,
        "idType": idTypeOfPerson15,
        "idNumber": idNumberOfPerson15,
        "gender": genderOfPerson15,
        "age": ageOfPerson15,
        "attachmentName": attachmentNameOfPerson15,
    })

    # Person 16
    persons.append({
        "pax": paxOfPerson16,
        "name": nameOfPerson16,
        "idType": idTypeOfPerson16,
        "idNumber": idNumberOfPerson16,
        "gender": genderOfPerson16,
        "age": ageOfPerson16,
        "attachmentName": attachmentNameOfPerson16,
    })

    # Person 17
    persons.append({
        "pax": paxOfPerson17,
        "name": nameOfPerson17,
        "idType": idTypeOfPerson17,
        "idNumber": idNumberOfPerson17,
        "gender": genderOfPerson17,
        "age": ageOfPerson17,
        "attachmentName": attachmentNameOfPerson17,
    })

    # Person 18
    persons.append({
        "pax": paxOfPerson18,
        "name": nameOfPerson18,
        "idType": idTypeOfPerson18,
        "idNumber": idNumberOfPerson18,
        "gender": genderOfPerson18,
        "age": ageOfPerson18,
        "attachmentName": attachmentNameOfPerson18,
    })

    # Person 19
    persons.append({
        "pax": paxOfPerson19,
        "name": nameOfPerson19,
        "idType": idTypeOfPerson19,
        "idNumber": idNumberOfPerson19,
        "gender": genderOfPerson19,
        "age": ageOfPerson19,
        "attachmentName": attachmentNameOfPerson19,
    })

    # Person 20
    persons.append({
        "pax": paxOfPerson20,
        "name": nameOfPerson20,
        "idType": idTypeOfPerson20,
        "idNumber": idNumberOfPerson20,
        "gender": genderOfPerson20,
        "age": ageOfPerson20,
        "attachmentName": attachmentNameOfPerson20,
    })
    return persons


def setTimeStart(i):
    print("value of i is: ", i)
    time_start_vars = {0: 'timeStart1', 1: 'timeStart2', 2: 'timeStart3', 3: 'timeStart4', 4: 'timeStart5',
                       5: 'timeStart6', 6: 'timeStart7', 7: 'timeStart8', 8: 'timeStart9', 9: 'timeStart10',
                       10: 'timeStart11', 11: 'timeStart12', 12: 'timeStart13', 13: 'timeStart14', 14: 'timeStart15',
                       15: 'timeStart16', 16: 'timeStart17', 17: 'timeStart18', 18: 'timeStart19', 19: 'timeStart20'}
    global_vars = globals()
    if i in time_start_vars:
        global_vars[time_start_vars[i]] = getDateTime()
        print(f"Start time for Person {i} is: ", global_vars[time_start_vars[i]])


def setTimeEndAndWaitForTimer(i):
    print("value of i is: ", i)
    time_vars = {
        0: 'timeEnd1', 1: 'timeEnd2', 2: 'timeEnd3', 3: 'timeEnd4', 4: 'timeEnd5',
        5: 'timeEnd6', 6: 'timeEnd7', 7: 'timeEnd8', 8: 'timeEnd9', 9: 'timeEnd10',
        10: 'timeEnd11', 11: 'timeEnd12', 12: 'timeEnd13', 13: 'timeEnd14', 14: 'timeEnd15',
        15: 'timeEnd16', 16: 'timeEnd17', 17: 'timeEnd18', 18: 'timeEnd19', 19: 'timeEnd20'
    }
    start_vars = {
        0: 'timeStart1', 1: 'timeStart2', 2: 'timeStart3', 3: 'timeStart4', 4: 'timeStart5',
        5: 'timeStart6', 6: 'timeStart7', 7: 'timeStart8', 8: 'timeStart9', 9: 'timeStart10',
        10: 'timeStart11', 11: 'timeStart12', 12: 'timeStart13', 13: 'timeStart14', 14: 'timeStart15',
        15: 'timeStart16', 16: 'timeStart17', 17: 'timeStart18', 18: 'timeStart19', 19: 'timeStart20'
    }
    global_vars = globals()

    if i in time_vars:
        global_vars[time_vars[i]] = getDateTime()
        print(f"End time for Person {i} is: ", global_vars[time_vars[i]])
        diff = getTimeDiff(global_vars[time_vars[i]], global_vars[start_vars[i]])
        if diff >= datetime.timedelta(seconds=timer):
            print(f"{timer} seconds have passed. Pressing ADD!")
        else:
            remaining_seconds = timer - diff.total_seconds()
            print(f"Waiting for an additional {remaining_seconds} seconds.")
            time.sleep(remaining_seconds)



def find_image_on_screen_using_opencv_color(template_path1, timeout, threshold=0.7):
    template = cv2.imread(template_path1)  # Read in color (BGR)
    h, w, _ = template.shape
    start_time = time.time()

    while True:
        # Capture a screenshot
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert to BGR

        # Perform template matching in color
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val >= threshold:
            print("Color image found ->" + template_path1)
            return max_loc[0], max_loc[1], w, h

        if time.time() - start_time > timeout:
            return None
        print("Color image searching for " + template_path1)
        time.sleep(0.01)

def find_any_of_two_images_on_screen_using_opencv(template_path1, template_path2, timeout, threshold=0.7):
    template1 = cv2.imread(template_path1, 0)
    template2 = cv2.imread(template_path2, 0)
    w1, h1 = template1.shape[::-1]
    w2, h2 = template2.shape[::-1]
    start_time = time.time()

    while True:
        # Capture a screenshot
        screenshot = pyautogui.screenshot()
        # Convert screenshot to numpy array and then to grayscale
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

        # Perform template matching for the first image
        res1 = cv2.matchTemplate(screenshot, template1, cv2.TM_CCOEFF_NORMED)
        min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)

        # Perform template matching for the second image
        res2 = cv2.matchTemplate(screenshot, template2, cv2.TM_CCOEFF_NORMED)
        min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(res2)

        # Check if the first image match value is above the threshold
        if max_val1 >= threshold:
            # Take action for the first image
            return ("Image 1", max_loc1[0], max_loc1[1], w1, h1)

        # Check if the second image match value is above the threshold
        if max_val2 >= threshold:
            # Take action for the second image
            return ("Image 2", max_loc2[0], max_loc2[1], w2, h2)

        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            return None

        time.sleep(0.1)

import cv2
import numpy as np
import pyautogui
import time

def is_button_enabled(image_path, expected_color_lower, expected_color_upper, sample_point_offset=(10, 10), timeout=60):
    """
    Checks if the button represented by image_path is enabled by verifying if a pixel color
    within the button region falls within the expected color range.

    :param image_path: Path to the button image template.
    :param expected_color_lower: Lower bound of BGR color range (tuple of 3 ints).
    :param expected_color_upper: Upper bound of BGR color range (tuple of 3 ints).
    :param sample_point_offset: (x, y) offset from top-left of detected button to sample color.
    :param timeout: Maximum time to wait for the button to appear.
    :return: True if button is enabled (color in range), False otherwise.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        # Take a screenshot
        screenshot = pyautogui.screenshot()
        screenshot_np = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Load template
        template = cv2.imread(image_path)
        if template is None:
            print(f"Template image not found: {image_path}")
            return False
        h, w, _ = template.shape

        # Template matching
        res = cv2.matchTemplate(screenshot_np, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        threshold = 0.7
        if max_val >= threshold:
            top_left = max_loc
            sample_x = top_left[0] + sample_point_offset[0]
            sample_y = top_left[1] + sample_point_offset[1]

            # Get pixel color at sample point
            pixel_color = screenshot_np[sample_y, sample_x]

            # Check if pixel color is within expected range
            if all(expected_color_lower[i] <= pixel_color[i] <= expected_color_upper[i] for i in range(3)):
                return True
            else:
                return False
        time.sleep(0.1)
    print("Button image not found within timeout.")
    return False