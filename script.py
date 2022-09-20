import pyautogui              # Library for automating mouse and keyboard clicks.
from PIL import ImageGrab     # Library for screenshot taking and comparing.
from PIL import Image         # Library for screenshot taking and comparing.
import numpy as np            # Library for screenshot comparing.
import time                   # Library for time needed for while loop.
import ctypes                 # Library for pop up window.
import winsound               # Library for Windows sound.

#-------------------------------------------------------------------------------
# CONSTANTS
#-------------------------------------------------------------------------------
MAX_TIME       = 60    # Maximum time in minutes for a script to run
BEEP_DURATION  = 1500  # milliseconds
BEEP_FREQUENCY = 440   # Hz
X_BUY           = 1000; Y_BUY           = 300         # X,Y coordinates of BUY button
X_SELECT        = 1450; Y_SELECT        = 380         # X,Y coordinates of SELECT button
X_CUSTOMER      = 1000; Y_CUSTOMER      = 320         # X,Y coordinates of CUSTOMER button
X_CONTINUE      = 1850; Y_CONTINUE      = 1140        # X,Y coordinates of CONTINUE button
STADIUM_PLAN_X1 = 280; STADIUM_PLAN_Y1  = 400         # X,Y coordinates of UPPER LEFT CORNER OF STADIUM PLAN
STADIUM_PLAN_X2 = 1220; STADIUM_PLAN_Y2 = 1100        # X,Y coordinates of LOWER RIGHT CORNER OF STADIUM PLAN
REFRESH_BUTTON  = "f5"

#-------------------------------------------------------------------------------
# Function for comparing screenshots - it compares reference screenshot (without available seats)
# with a new screenshot, to find any differences (for example, available seat in section)
#-------------------------------------------------------------------------------
def image_compare(reference_screenshot, new_screenshot):
    arr1 = np.array(reference_screenshot)
    arr2 = np.array(new_screenshot)
    if arr1.shape != arr2.shape:
        return False
    maxdiff = np.max(np.abs(arr1 - arr2))
    return maxdiff == 0

#-------------------------------------------------------------------------------
# Function for opening and then comparing screenshots - it calls image_compare function
#-------------------------------------------------------------------------------
def image_compare_file(filename_reference, filename_new):
    im1 = Image.open(filename_reference)
    im2 = Image.open(filename_new)
    return image_compare(im1, im2)

#-------------------------------------------------------------------------------
# Start searching function
#-------------------------------------------------------------------------------
def start_search():
    t_end = time.time() + 60 * MAX_TIME

    while time.time() < t_end:

        # Start clicking all the way to stadium plan
        time.sleep(2.5)
        pyautogui.click(X_BUY, Y_BUY, duration=3)
        pyautogui.click(X_SELECT, Y_SELECT, duration=3)
        pyautogui.click(X_CUSTOMER, Y_CUSTOMER, duration=3)
        pyautogui.click(X_CONTINUE, Y_CONTINUE, duration=1)
        time.sleep(3)

        # Take a screenshot of stadium plan
        image_grabbed = ImageGrab.grab(bbox=(STADIUM_PLAN_X1, STADIUM_PLAN_Y1,
                                             STADIUM_PLAN_X2, STADIUM_PLAN_Y2))
        image_grabbed.save("new_screenshot.png")  # Save newly taken screenshot of stadium plan

        # Compare a screenshot of stadium plan to the reference screenshot
        if image_compare_file("reference.png", "new_screenshot.png"):
            print("Ticket not found")  # Screenshots are identical / ticket not found
        else:
            print("TICKET FOUND")  # Screenshots are not identical / ticket found
            winsound.Beep(BEEP_FREQUENCY, BEEP_DURATION)  # Make a sound
            ctypes.windll.user32.MessageBoxW(0, "TICKET FOUND", "TICKET FOUND", 1)  # Create a popup window
            break

        time.sleep(4.5)
        pyautogui.press(REFRESH_BUTTON)

# Start a program
if __name__ == "__main__":
    start_search()
    print("Your Screen",pyautogui.size())

