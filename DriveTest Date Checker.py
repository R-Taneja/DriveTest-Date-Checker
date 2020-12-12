from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

browser  = webdriver.Chrome(ChromeDriverManager().install())

# Go to the intial page
browser.get('https://drivetest.ca/book-a-road-test/booking.html#/verify-driver')

# Enter the license number and expiry date
license_number = input('Enter your driver\'s license number, exactly as it appears on your license: ')
license_expiry_date = input('Enter your driver\'s license expiry date, exactly as it appears on your license: ')
browser.find_element_by_name('licenceNumber').send_keys(license_number)
browser.find_element_by_name('licenceExpiryDate').send_keys(license_expiry_date)

# Advance to the next page
browser.find_element_by_id('regSubmitBtn').click();

# Wait for the page to load
try:
    wait = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="7266086"]/div/div/div[2]/div/span[2]/button')))
except TimeoutException:
    print ("Loading took too much time.")

# Scroll down so the reschedule button comes into view
browser.execute_script("window.scrollTo(0, 250)") 

# Click the reschedule button
browser.find_element_by_xpath('//*[@id="7266086"]/div/div/div[2]/div/span[2]/button').click();

# Wait for the page to load
try:
    wait = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page_book_a_road_test_booking"]/div[4]/div/div/div/div/div/div[4]/button[1]')))
except TimeoutException:
    print ("Loading took too much time.")

# Click the reschedule button on the popup
browser.find_element_by_xpath('//*[@id="page_book_a_road_test_booking"]/div[4]/div/div/div/div/div/div[4]/button[1]').click();

# Wait for the page to load
try:
    wait = WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.XPATH, '//*[@id="booking-location"]/div/div/form/div[1]/div/div[1]/h1[1]')))
except TimeoutException:
    print ("Loading took too much time.")

# Click on the location and view available dates
browser.find_element_by_xpath('//*[@id="9580"]').click();
browser.find_element_by_xpath('//*[@id="booking-location"]/div/div/form/div[2]/div[2]/button').click();
try:
    wait = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="driver-info"]/div[1]/div[1]/div[1]/a[2]')))
except TimeoutException:
    print ("Loading took too much time.")

# Go through every date in the availability calendar and see if it has an opening based on its CSS class
dates = ['//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[1]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[3]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[4]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[5]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[6]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[1]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[2]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[3]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[4]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[5]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[6]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[1]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[2]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[3]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[4]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[5]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[6]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[1]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[2]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[3]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[4]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[5]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[6]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[6]/td[1]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[6]/td[2]/div/div/div/a']
unavailable_count = 0
for i in dates:
    date = browser.find_element_by_xpath(i)
    availability = str(date.get_attribute("class"))
    if availability == "date-link disabled" or availability == "date-link disabled todays-date":
        unavailable_count += 1
        continue
    else:
        print(str(date.get_attribute("title")))

if unavailable_count == 31:
    print("No available dates.")

# browser.quit()