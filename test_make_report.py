import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Locators
class Locators:
    email_field = (By.ID, "id_registration-email")
    pswd1 = (By.ID, "id_registration-password1")
    pswd2 = (By.ID, "id_registration-password2")
    register_submit = (By.NAME, "registration_submit")
    message = (By.CSS_SELECTOR, '#messages div div')

# Test data
registration_text = {
    'en-gb' : 'Thanks for registering!',
    'ru' : 'Спасибо за регистрацию!',
    'fr' : 'Merci de vous être enregistré !',
    'it' : 'Grazie per la registrazione!'
}
current_time = int(round(time.time() * 1000))
username = f"test1+{current_time}@gmail.com"
password = "R0ZPg2A6c"

def test_registration_en(browser):
    browser.implicitly_wait(15)
    browser.find_element(*Locators.email_field).send_keys(username)
    browser.find_element(*Locators.pswd1).send_keys(password)
    browser.find_element(*Locators.pswd2).send_keys(password)
    browser.find_element(*Locators.register_submit).click()
    success_message = browser.find_element(*Locators.message).text.strip()

    assert registration_text['en-gb'] == success_message, "Wrong registration massage!"

if __name__ == '__main__':
    test_registration_en()