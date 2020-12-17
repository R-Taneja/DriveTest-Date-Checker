from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

license_number = input('Enter your driver\'s license number, exactly as it appears on your license: ')
license_expiry_date = input('Enter your driver\'s license expiry date, exactly as it appears on your license: ')

locations = ['//*[@id="9556"]', '//*[@id="9557"]', '//*[@id="9559"]', '//*[@id="9567"]', '//*[@id="9597"]', '//*[@id="9574"]', '//*[@id="12448"]', '//*[@id="9552"]', '//*[@id="9580"]', '//*[@id="9581"]', '//*[@id="9596"]', '//*[@id="9602"]', '//*[@id="9565"]', '//*[@id="9579"]', '//*[@id="9592"]']
location_number = 0

for location in locations:
    location_number += 1
    browser  = webdriver.Chrome(ChromeDriverManager().install())

    # Go to the intial page
    browser.get('https://drivetest.ca/book-a-road-test/booking.html#/verify-driver')

    # Enter the license number and expiry date
    browser.find_element_by_name('licenceNumber').send_keys(license_number)
    browser.find_element_by_name('licenceExpiryDate').send_keys(license_expiry_date)

    # Advance to the next page
    browser.find_element_by_id('regSubmitBtn').click();

    # Wait for the page to load
    try:
        wait = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="booking-dashboard"]/div/div/div/div[2]/div/div[5]/p/a')))
    except TimeoutException:
        print ("Loading took too much time.")

    # Click the book a road test button
    browser.find_element_by_xpath('//*[@id="booking-dashboard"]/div/div/div/div[2]/div/div[5]/p/a').click();

    # Wait for the page to load
    try:
        wait = WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.XPATH, '//*[@id="lic_G2"]')))
    except TimeoutException:
        print ("Loading took too much time.")
    
    # Click the G2 button
    browser.find_element_by_xpath('//*[@id="G2btn"]').click();

    # Click the continue buttons
    browser.find_element_by_xpath('//*[@id="booking-licence"]/div/form/div/div[4]/button').click();

    # Wait for the page to load
    try:
        wait = WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.XPATH, '//*[@id="9607"]')))
    except TimeoutException:
        print ("Loading took too much time.")

    # Click on the location and view available dates
    browser.find_element_by_xpath(location).click();
    try:
        wait = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="booking-location"]/div/div/form/div[2]/div[2]/button')))
    except TimeoutException:
        print ("Loading took too much time.")
    browser.find_element_by_xpath('//*[@id="booking-location"]/div/div/form/div[2]/div[2]/button').click();
    try:
        wait = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="driver-info"]/div[1]/div[1]/div[1]/a[2]')))
    except TimeoutException:
        print ("Loading took too much time.")

    # Go through every date in the availability calendar and see if it has an opening based on its CSS class
    dates = ['//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[3]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[4]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[5]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[6]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[1]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[2]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[3]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[4]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[5]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[6]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[1]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[2]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[3]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[4]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[5]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[6]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[1]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[2]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[3]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[4]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[5]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[6]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[6]/td[1]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[6]/td[2]/div/div/div/a']
    available_dates = []
    for i in dates:
        date = browser.find_element_by_xpath(i)
        availability = str(date.get_attribute("class"))
        if availability != "date-link disabled" and availability != "date-link disabled todays-date" and availability != "date-link disabled selected":
            available_dates.append(str(date.get_attribute("title")))

    if location_number == 1:
        print("Brampton:")
    if location_number == 2:
        print("Brantford:")
    if location_number == 3:
        print("Burlington:")
    if location_number == 4:
        print("Guelph:")
    if location_number == 5:
        print("Hamilton:")
    if location_number == 6:
        print("Kitchener:")
    if location_number == 7:
        print("Mississauga:")
    if location_number == 8:
        print("Newmarket:")
    if location_number == 9:
        print("Oakville:")
    if location_number == 10:
        print("Orangeville:")
    if location_number == 11:
        print("St Catharines:")
    if location_number == 12:
        print("Toronto Downsview:")
    if location_number == 13:
        print("Toronto Etobicoke:")
    if location_number == 14:
        print("Toronto Metro East:")
    if location_number == 15:
        print("Toronto Port Union:")

    if not available_dates:
        print("No available dates")
    else:
        for i in available_dates:
            print(str(i))
