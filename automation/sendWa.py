from selenium import webdriver

driver = webdriver.Chrome('/home/pandu/Documents/eksperimen/automation/driver/chromedriver')
driver.get('http://web.whatsapp.com')

name = "Koweks"
msg = "cek"
count = 4

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_2_1wd')

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('_1E0Oz').click()
