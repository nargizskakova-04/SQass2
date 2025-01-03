# test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_logout():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        driver.get("https://www.saucedemo.com")
        
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        password = driver.find_element(By.ID, "password")
        
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        
        products_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "title"))
        )
        assert products_title.text == "Products", "Login failed"
        
        menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()
        
        logout_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_link.click()
        
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )
        assert login_button.is_displayed(), "Logout failed"
        
        print("Login/Logout test completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise
    
    finally:
        driver.quit()

if __name__ == "__main__":
    print("\nRunning Login/Logout Test...")
    test_login_logout()
