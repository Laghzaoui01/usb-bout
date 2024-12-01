import pyautogui
import time
import subprocess

# L-function li kay9dm t7ammil u t7ell tswira fi fullscreen
def download_and_open_image():
    # Dkhil win+r bach t7ell Run Dialog
    pyautogui.hotkey('win', 'r')
    time.sleep(1)

    # Katktb 'cmd' u katdwi Enter
    pyautogui.typewrite('cmd')
    pyautogui.press('enter')
    time.sleep(1)

    # L-command li kayt7ammel tswira
    curl_command = 'curl -o "C:\\Users\\SETUP GAME\\Desktop\\image\\hak2.jpg" "https://imgs.search.brave.com/_DlCVLaWPBoVSebTfC4z6wyLf7TxN_JZVtdgEil7CAw/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNTAy/ODYwNDMwL3Bob3Rv/L2hhY2tlci5qcGc_/cz02MTJ4NjEyJnc9/MCZrPTIwJmM9MWJt/VDdaMGxmYlRLZzFp/ZHZFQ1V2VnZuY0Zu/bktJd3EwT21Qclll/SG9Edz0"'

    # Execute l-command bach t7ammel tswira
    pyautogui.typewrite(curl_command)
    pyautogui.press('enter')
    time.sleep(5)  # Stanna chwiya l7it kayn t7amilt tswira

    # Dkhil command li kay7ell tswira
    pyautogui.typewrite('start "" "C:\\Users\\SETUP GAME\\Desktop\\image\\hak2.jpg"')
    pyautogui.press('enter')
    time.sleep(2)  # Stanna l7it l-image t7ell

    # Dkhil Alt+Enter bach t7ell l-image f fullscreen
    pyautogui.hotkey('alt', 'enter')

# Run l-function
download_and_open_image()
