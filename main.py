from selenium.webdriver import Firefox
import schedule
from datetime import date, timedelta
import time 

def job():
	print("I'm Working...")
	driver = Firefox()
	driver.get("https://my.basic-fit.com/login")
	time.sleep(3) 
	datas = []
	f = open('variables.txt', "r")
	for i, line in enumerate(f):
		datas.append(line)

	count = 0    
	email = driver.find_elements_by_name("email") 
	password = driver.find_elements_by_name("password") 
	for value in email: 
		value.send_keys(datas[0])
	for value in password: 
		value.send_keys(datas[1])    
	submit = driver.find_element_by_id("loginBtn") 
	submit.click() 
	time.sleep(3)
	gymbooking = driver.find_element_by_id("gymTimeBookingMenuId") 
	gymbooking.click()
	time.sleep(1)
	idreserveBookingId = driver.find_element_by_id("reserveBookingId")
	idreserveBookingId.click()
	time.sleep(1)
	day = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div/div[13]/p")
	day.click()
	time.sleep(1)
	ideveningSlotsId = driver.find_element_by_id("eveningSlotsId")
	ideveningSlotsId.click()
	time.sleep(1)
	heure = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div/div["+datas[2]+"]/div[1]/p")
	heure.click()
	time.sleep(1)
	nextBtnId = driver.find_element_by_id("nextBtnId")
	nextBtnId.click()
	time.sleep(1)
	duration = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div/div["+datas[3]+"]/p")
	duration.click()
	time.sleep(1)
	checkbox = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div/div[22]/div[1]")
	checkbox.click()
	time.sleep(1)
	nextBtnId = driver.find_element_by_id("nextBtnId")
	nextBtnId.click()
	time.sleep(3)
	driver.close()

schedule.every(24).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(60)