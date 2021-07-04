from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import sys
from sys import platform

# Folder pesan dan no telp
pathMessage = "/home/pandu/Documents/eksperimen/python/sendMessage/whatsapp-bulk-messenger-primary/assets/message.txt"
pathNumberPhone = "/home/pandu/Documents/eksperimen/python/sendMessage/whatsapp-bulk-messenger-primary/assets/numbers.txt"



try:
	# Buka file Pesan
	f = open(pathMessage, "r")
	message = f.read()
	f.close()

	# Buka file Nomor Telp
	numbers = []
	f = open(pathNumberPhone, "r")
	for line in f.read().splitlines():
		if line != "":
			numbers.append(line)
	f.close()
	total_number = len(numbers)
	print("Total No Telp terbaca : {}".format(total_number))

except OSError as e:
	print("Lokasi atau File mungkin salah anda, Pesan Error : {}".format(e))
	sys.exit(1)

delay = 30

driver = webdriver.Chrome(ChromeDriverManager().install())
print('Ketika browser terbuka silakan Scan barcode dan tunggu hingga masuk')
driver.get('https://web.whatsapp.com')
input("Jika tampilan chat sudah terlihat silakan tekan tombol ENTER ")
for idx, number in enumerate(numbers):
	number = number.strip()
	if number == "":
		continue
	print('{}/{} => Mengirim Pesan kepada {}.'.format((idx+1), total_number, number))
	try:
		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
		sent = False
		for i in range(3):
			if not sent:
				driver.get(url)
				try:
					click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME , '_1E0Oz')))
				except Exception as e:
					print(f"Terjadi kesalahan..\n Kesalahan mengirim ke Nomor: {number}, Mencoba ulang ({i+1}/3)")
					print("Pastikan Ponsel dan Komputer anda .")
					input("tekan tombol ENTER untuk melanjutkan")
				else:
					sleep(1)
					click_btn.click()
					sent=True
					sleep(3)
					print('Pesan dikirimkan Ke : ' + number)
	except Exception as e:
		print('Gagal mengirim Pesan ke ' + number + str(e))
