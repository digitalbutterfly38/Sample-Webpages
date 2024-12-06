import openpyxl
import time
import pyautogui

# Function to send an email with attachment
def send_email(To, Cc, subject, attachment_path):
    # Open Outlook (you may need to adjust the coordinates)
    pyautogui.hotkey("win", "s")
    time.sleep(1)
    pyautogui.write("Outlook")
    pyautogui.press("enter")
    time.sleep(5)  # Wait for Outlook to open

    # Compose a new email
    pyautogui.hotkey("ctrl", "n")
    time.sleep(2)

    # Set the To
    pyautogui.write(To)
    pyautogui.press("tab")

    # Set the To
    pyautogui.write(Cc)
    pyautogui.press("tab")

    # Set the subject
    pyautogui.write(subject)
    pyautogui.press("tab")

    # Attchnment
    pyautogui.press("alt+h+af+b")
    time.sleep(2)

    # Attach a file
    pyautogui.write(attachment_path)
    time.sleep(1)
    pyautogui.press("enter")

    # Send the email
    pyautogui.hotkey("ctrl", "enter")
    time.sleep(2)

# Load data from Excel file
workbook = openpyxl.load_workbook('C:\\Users\\Sheshagiri.KG\\Desktop\\Test Mailing\\email_data.xlsx')
sheet = workbook.active

# Loop through rows in the Excel file and send emails
for row in sheet.iter_rows(min_row=2, values_only=True):
    To, Cc, subject, attachment_path = row
    send_email(To, Cc, subject, attachment_path)

# Close Outlook (you may need to adjust the coordinates)
pyautogui.hotkey("alt", "f4")