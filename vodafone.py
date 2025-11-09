from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Tarayıcı ayarları
options = Options()
options.add_argument("--headless")  # Tarayıcıyı gizli aç
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Chrome başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Vodafone iPhone 13 sayfasını aç
url = "https://www.vodafone.com.tr/faturaya-ek/iPhone-13/p/telefonlar"
driver.get(url)

# Sayfanın yüklenmesini bekle
time.sleep(6)

# TL veya ₺ içeren tüm elementleri bul
elements = driver.find_elements(By.XPATH, "//*[contains(text(),'₺') or contains(text(),'TL')]")

# Bulunan fiyatları yazdır
for el in elements:
    text = el.text.strip()
    if text:
        print(text)

driver.quit()
