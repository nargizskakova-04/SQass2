from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_search():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        driver.get("https://www.amazon.com")
        
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        
        search_box.clear()
        search_box.send_keys("laptop")
        
        search_button = driver.find_element(By.ID, "nav-search-submit-button")
        search_button.click()
        
        search_results = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-result-list"))
        )
        
        assert search_results.is_displayed(), "Search results not displayed"
        
        print("Search test completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise
    
    finally:
        driver.quit()

if __name__ == "__main__":
    print("Running Search Test...")
    test_search()