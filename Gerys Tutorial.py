from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import subprocess as sub
from cStringIO import StringIO
import win32clipboard
from PIL import Image
import sys

pt = raw_input('Enter Ticket ID: ')
# nt_id = raw_input('Enter NT ID: ')
#nt_id = os.environ.get("USERNAME")
msisdn = raw_input('Enter MSISDN: ')
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1600x800')
filepath = 'C:\Users\jcalder56\Downloads\login.png'

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

#deletes prior screenshot
try:
	os.chdir('C:\Users\jcalder56\Downloads')
	sub.call('del login.png', shell=True)
except:
	pass

#creating webdriver 
driver = webdriver.Chrome()#(chrome_options=options)
driver.get('https://grandcentral.t-mobile.com/')

#Enter MSISDN and search in GC
# search = driver.find_element_by_id('mobile_number')
search = wait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'mobile_number')))
search.send_keys(msisdn)
search.send_keys(Keys.ENTER)
time.sleep(8)

# # Close PopUp
try:
	pop = wait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, 'wm-close-button')))
	pop.click()
	##time.sleep(5)
except:
	pass

# # Verify Customer

verify = wait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, 'bypass-dropdown-arrow')))
time.sleep(3)
verify.click()

verify1 = wait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, 'bypass-verification')))
time.sleep(3)
verify1.click()


# # Get to Account Info
account_info = wait(driver, 15).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Account')))
account_info.click()

tmo_id = wait(driver, 15).until(EC.element_to_be_clickable((By.LINK_TEXT, 'T-Mobile ID')))
tmo_id.click()
#time.sleep(5)
driver.save_screenshot('C:\Users\jcalder56\Downloads\login.png')
#time.sleep(2)
lock = driver.find_element_by_class_name('lock-message')
if lock.is_displayed():
	print 'Failed'

#sends screenshot to clipboard
image = Image.open(filepath)
output = StringIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()
send_to_clipboard(win32clipboard.CF_DIB, data)

#opens up pier to paste screenshot
driver2 = webdriver.Chrome()#(chrome_options=options)
driver2.get('https://technology.services.t-mobile.com/pier/#Home')
#time.sleep(3)
driver2.get('https://technology.services.t-mobile.com/pier/#Ticket?ticket_id='+pt)
#time.sleep(5)
wlog = wait(driver2, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, 'worklogbody')))
#time.sleep(3)
wlog.click()
#time.sleep(3) 
wlog.send_keys(Keys.CONTROL, 'v')
#time.sleep(2)
save = driver2.find_element_by_class_name('fa-floppy-o')
save.click()

#deletes prior screenshot
os.chdir('C:\Users\jcalder56\Downloads')
sub.call('del login.png', shell=True)
#time.sleep(2)

# # Login to Customer Account

login = wait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-icon')))
login.click()
#time.sleep(8)
old_tab = driver.window_handles[0]
new_tab = driver.window_handles[1]
driver.switch_to_window(new_tab)
# src = driver.page_source
#time.sleep(10)
driver.save_screenshot('C:\Users\jcalder56\Downloads\login.png')
#time.sleep(3)
driver.close()

 #sends screenshot to clipboard
image = Image.open(filepath)
output = StringIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()
send_to_clipboard(win32clipboard.CF_DIB, data)

#opens up pier to paste screenshot
driver2 = webdriver.Chrome()#(chrome_options=options)
driver2.get('https://technology.services.t-mobile.com/pier/#Home')
time.sleep(3)
driver2.get('https://technology.services.t-mobile.com/pier#Ticket#'+pt)
wlog = wait(driver2, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, 'worklogbody')))
wlog.click()
wlog.send_keys(Keys.CONTROL, 'v')
#time.sleep(2)
save = driver2.find_element_by_class_name('fa-floppy-o')
save.click()

#deletes prior screenshot
os.chdir('C:\Users\jcalder56\Downloads')
sub.call('del login.png', shell=True)

driver.close()
driver2.close()
