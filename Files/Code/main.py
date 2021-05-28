#pip install selenium
#pip install keyboard
from selenium import webdriver
#Download Chrome Driver With Respect To Your Chrome Browser's Version For Checking the version of chrome.go to the following site chrome://version
from time import sleep
from selenium.webdriver.common.keys import Keys
import keyboard
driver = webdriver.Chrome("#Path Of The Chromedriver")
driver.get("https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3A1e10afed606ab28c%2C10%3A1622115835%2C16%3A4fd48bbee178515d%2Ca8a48ab5363d05a7b8d1430d3fc4e222fad429b6fd3847d13f1444f9d092fb71%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22fbe67d41c240458e9ae21024ca96307b%22%7D&response_type=code&flowName=GeneralOAuthFlow")#For Security Purpose Google Does Not Allow Selenium To Sign Account So We Need To Sign In With Stack OverFlow
sleep(2)
gmail = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
email = open("email.txt", "r").read()#Enter your gmail id in the email.txt file
gmail.send_keys(email)
gmail.send_keys(Keys.ENTER)
sleep(3)
pas = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
passwd = open("Password.txt", "r").read()#enter your password in password.txt file
pas.send_keys(passwd)
pas.send_keys(Keys.ENTER)
sleep(3)
driver.get("https://meet.google.com")
link = driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[2]/div[1]/label/input")
code = input("Enter Your Meeting Code(within 10sec): ")
sleep(10)        
link.send_keys(code)
link.send_keys(Keys.ENTER)
sleep(4)
dis_btn = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")
dis_btn.click()
sleep(5)
keyboard.send("tab", do_press=True, do_release=True)
keyboard.send("tab", do_press=True, do_release=True)
keyboard.send("tab", do_press=True, do_release=True)
keyboard.send("tab", do_press=True, do_release=True)
keyboard.send("enter", do_press=True, do_release=True)
sleep(2)
keyboard.send("tab", do_press=True, do_release=True)
keyboard.send("tab", do_press=True, do_release=True)
keyboard.send("enter", do_press=True, do_release=True)
#if your cam is off as default skip the following parts(cam_off and mic_off)
sleep(3)
cam_off = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div")
cam_off.click()
sleep(2)
mic_off = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div")
mic_off.click()
sleep(3)
join_btn = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span")
join_btn.click()
sleep(60)#You Are Unable To Send The Following Attendance If The Host Does Not Allow You So Increase The Sleep Time As much As Possible
mess_box = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[3]/span/span")
mess_box.click()
sleep(3)
chat_box = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea")
chat_box.send_keys("Your Name Present Sir/Mam")
chat_box.send_keys(Keys.ENTER)
sleep(2)
close = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[1]/div[2]/div/span/button/i")
close.click()
#https://meet.google.com/hyu-hbzv-uei
#if you face any error try increasing the sleep time or inspecting the particular element again
