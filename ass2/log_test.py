from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_alem_login_logout():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://platform.alem.school/sign-in")
   
        wait.until(EC.presence_of_element_located((By.ID, ":r0:"))).send_keys("nargizskakova-04@mail.ru")
        driver.find_element(By.ID, ":r1:").send_keys("Qwerty_1")
        
        continue_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Continue')]")))
        continue_button.click()
        
        time.sleep(2)
        print("Login successful!")

        menu_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.MuiIconButton-root")))
        menu_button.click()

        logout_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(text(), 'Log out')]")))
        logout_button.click()

        time.sleep(2)
        
        current_url = driver.current_url
        assert "sign-in" in current_url, "Not redirected to login page"
        print("Logout successful!")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        driver.save_screenshot("error_screenshot.png")
        raise
    finally:
        driver.quit()

if __name__ == "__main__":
    test_alem_login_logout()