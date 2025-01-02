from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class FlightBookingAutomation:
    def __init__(self):
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # Using a demo flight booking website
        self.base_url = "https://demo.guru99.com/test/newtours/"
        
    def open_website(self):
        """Navigate to the website and verify title"""
        self.driver.get(self.base_url)
        # Title checkpoint
        expected_title = "Welcome: Mercury Tours"
        actual_title = self.driver.title
        assert expected_title == actual_title, f"Title mismatch. Expected: {expected_title}, Got: {actual_title}"
        print("Title verification passed!")

    def login(self, username="tutorial", password="tutorial"):
        """Login to the website using CSS selectors"""
        # Using CSS selector for username field
        username_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='userName']")
        username_field.send_keys(username)
        
        # Using CSS selector for password field
        password_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_field.send_keys(password)
        
        # Using XPath for login button
        login_button = self.driver.find_element(By.XPATH, "//input[@name='submit']")
        login_button.click()

    def navigate_to_flights(self):
        """Navigate to the flights section using XPath"""
        # Using XPath to click on Flights link
        flights_link = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Flights')]")
        flights_link.click()

    def book_flight(self):
        """Fill in flight booking details using mixed locators"""
        # Wait for the flight finder form to be visible
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "findFlights"))
        )

        # Select trip type using CSS selector
        trip_type = self.driver.find_element(By.CSS_SELECTOR, "input[value='roundtrip']")
        trip_type.click()

        # Select passengers using basic locator
        passengers = Select(self.driver.find_element(By.NAME, "passCount"))
        passengers.select_by_value("2")

        # Select departure using XPath
        departing = Select(self.driver.find_element(By.XPATH, "//select[@name='fromPort']"))
        departing.select_by_value("London")

        # Select departure month using CSS selector
        depart_month = Select(self.driver.find_element(By.CSS_SELECTOR, "select[name='fromMonth']"))
        depart_month.select_by_visible_text("July")

        # Select departure date using basic locator
        depart_date = Select(self.driver.find_element(By.NAME, "fromDay"))
        depart_date.select_by_value("15")

        # Select arrival city using XPath
        arriving = Select(self.driver.find_element(By.XPATH, "//select[@name='toPort']"))
        arriving.select_by_value("New York")

        # Select service class using CSS selector
        service_class = self.driver.find_element(By.CSS_SELECTOR, "input[value='First']")
        service_class.click()

        # Select airline using XPath
        airline = Select(self.driver.find_element(By.XPATH, "//select[@name='airline']"))
        airline.select_by_visible_text("Unified Airlines")

        # Click continue using basic locator
        continue_button = self.driver.find_element(By.NAME, "findFlights")
        continue_button.click()

    def verify_booking(self):
        """Verify successful booking"""
        # Wait for and verify the success message using XPath
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//font[contains(text(), 'After flight finder - No Seats Available')]"))
        )
        assert success_message.is_displayed(), "Booking verification failed!"
        print("Flight booking verification passed!")

    def cleanup(self):
        """Close the browser"""
        self.driver.quit()

    def run_booking_flow(self):
        """Execute the complete booking flow"""
        try:
            self.open_website()
            self.login()
            self.navigate_to_flights()
            self.book_flight()
            self.verify_booking()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            self.cleanup()

if __name__ == "__main__":
    # Create unique instance name using your identifier
    print("\nRunning booking Test...")
    booking_bot = FlightBookingAutomation()
    booking_bot.run_booking_flow()