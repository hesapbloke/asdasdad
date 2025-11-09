from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json, time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.vodafone.com.tr/faturaya-ek/iPhone-13/p/telefonlar"
driver.get(url)
time.sleep(5)

elements = driver.find_elements(By.XPATH, "//*[contains(text(),'₺') or contains(text(),'TL')]")
prices = [el.text.strip() for el in elements if el.text.strip()]

driver.quit()

# fiyatları kaydet
with open("fiyat.json", "w", encoding="utf-8") as f:
    json.dump(prices, f, ensure_ascii=False, indent=2)

print("✅ fiyat.json dosyası oluşturuldu!")
