import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wildberries_search():
    driver = webdriver.Chrome()
    driver.get("https://www.wildberries.ru/")
    wait = WebDriverWait(driver, 10)
    
    try:
        search_box = wait.until(EC.presence_of_element_located((By.ID, "searchInput")))
        search_box.send_keys("laptop")
        
        driver.find_element(By.ID, "applySearchBtn").click()
        
        results = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-card__wrapper")))       
        assert results.is_displayed()
        print("Search successful!")
        time.sleep(2)
    finally:
        driver.quit()

if __name__ == "__main__":
    wildberries_search()