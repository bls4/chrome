import pyautogui, sys, os
from time import sleep


chrome_run='/usr/bin/google-chrome-stable %U https://www.youtube.com/create_channel --no-sandbox --disable-dev-shm-usage --disable-gpu &'
os.system(chrome_run)
sleep(4)
pyautogui.click(x=1415, y=126)

sleep(2)
pyautogui.click(x=710, y=439)

file = open('mail', 'r')
usermail = file.read()
file.close()

file = open('pass', 'r')
passwd = file.read()
file.close()

file = open('device', 'r')
device = file.read()
file.close()

file = open('token', 'r')
token = file.read()
file.close()

# Login gmail
sleep(3)
pyautogui.write(usermail) 
sleep(1)   
pyautogui.press('enter') 
sleep(4)
pyautogui.write(passwd) 
sleep(1)   
pyautogui.press('enter')


# I understand
sleep(4)
pyautogui.click(x=722, y=630)

# click addon
sleep(30)
pyautogui.click(x=1290, y=57)

#click token
sleep(5)
pyautogui.click(x=984, y=293)


#write token
sleep(1)
pyautogui.write(token) 

 
#click device name
sleep(1)
pyautogui.click(x=975, y=380)

#write device name
sleep(1)
pyautogui.write(device) 

#click done
sleep(3)
pyautogui.click(x=1097, y=453)

#click no proxy
sleep(35)
pyautogui.click(x=1091, y=504)

#click make money
sleep(15)
pyautogui.click(x=506, y=584)
