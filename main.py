from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException
import time

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.get("http://sdetchallenge.fetch.com/")
    return driver

def reset_bowls(driver):
    reset_button = driver.find_element(By.ID, "reset")
    reset_button.click()
    time.sleep(5)

    # Verify bowls are empty
    left_bowl_items = driver.find_elements(By.CSS_SELECTOR, "#left_bowl li")
    right_bowl_items = driver.find_elements(By.CSS_SELECTOR, "#right_bowl li")
    assert len(left_bowl_items) == 0 and len(right_bowl_items) == 0, "Bowls are not empty after reset"
    print("Bowls have been reset and are empty.")

def weigh(driver, left_bowls, right_bowls):
    # Clear the input fields for both bowls
    for i in range(9):
        left_input = driver.find_element(By.ID, f"left_{i}")
        right_input = driver.find_element(By.ID, f"right_{i}")
        left_input.clear()
        right_input.clear()

    # Set the values for the current weighing
    for num in left_bowls:
        left_input = driver.find_element(By.ID, f"left_{num}")
        left_input.send_keys(num)
    for num in right_bowls:
        right_input = driver.find_element(By.ID, f"right_{num}")
        right_input.send_keys(num)

    # Perform the weighing
    weigh_button = driver.find_element(By.ID, "weigh")
    weigh_button.click()
    time.sleep(2)



def get_weighing_result(driver):
    try:
        # Check if there's an unexpected alert first
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        print(f"Unexpected Alert Present: {alert_text}")
        return alert_text
    except NoAlertPresentException:
        pass

    # Now proceed to get the weighing result as usual
    wait = WebDriverWait(driver, 10)
    result_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".game-info ol")))
    result = result_element.text.strip()
    return result

def click_fake_bar(driver, fake_bar_index):
    fake_bar_button = driver.find_element(By.ID, f"coin_{fake_bar_index}")
    fake_bar_button.click()
    try:
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
    except UnexpectedAlertPresentException:
        # Handle the unexpected alert if present
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
    return alert_text

def main():
    driver = setup_driver()
    weighings = []

    try:
        # Initial weighing
        reset_bowls(driver)
        left_bowls = [0, 1, 2]
        right_bowls = [3, 4, 5]
        weigh(driver, left_bowls, right_bowls)
        result = get_weighing_result(driver)
        weighings.append(result)

        if ">" in result:
            lighter_group = right_bowls
        elif "<" in result:
            lighter_group = left_bowls
        else:
            lighter_group = [6, 7, 8]

        # Second weighing
        if len(lighter_group) == 3:
            reset_bowls(driver)
            # Reassign lists with new values for the second weighing
            left_bowls = [lighter_group[0]]
            right_bowls = [lighter_group[1]]
            # Perform the weighing
            weigh(driver, left_bowls, right_bowls)
            result = get_weighing_result(driver)
            weighings.append(result)

            if ">" in result:
                fake_bar = right_bowls[0]
            elif "<" in result:
                fake_bar = left_bowls[0]
            else:
                fake_bar = lighter_group[2]

        # Click the identified fake bar
        alert_message = click_fake_bar(driver, fake_bar)
        print(f"Identified fake bar: {fake_bar}")
        print(f"Alert message: {alert_message}")

        # Print all weighings
        print("Weighings:")
        for weighing in weighings:
            print(weighing)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
