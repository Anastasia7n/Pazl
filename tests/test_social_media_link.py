import pytest
<<<<<<< HEAD
from pages.login_page import LoginPage
from pages.locators import InventoryPageLocators
from pages.locators import LoginPageLocators
=======
import time

from pages.inventory_page import InventoryPage
from pages.locators import InventoryPageLocators
>>>>>>> main

link = "https://www.saucedemo.com/"

regular_user = "standard_user"
password = "secret_sauce"


<<<<<<< HEAD

@pytest.mark.TC_003_05
# @pytest.mark.xfail
def test_open_facebook_page(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    parentHandle = browser.current_window_handle
    # print("Parent Handle: " + parentHandle)
    driver.click_element(*InventoryPageLocators.FACEBOOK_IMAGE_LINK)
    handles = browser.window_handles
    # print("List of handles: ", handles)
    # time.sleep(3)
    for handle in handles:
        if handle not in parentHandle:
            browser.switch_to.window(handle)
    driver.should_be_current_page("https://www.facebook.com/saucelabs")


@pytest.mark.TC_003_04
def test_open_twitter_page(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    parentHandle = browser.current_window_handle
    driver.click_element(*InventoryPageLocators.TWITTER_IMAGE_LINK)
    handles = browser.window_handles
    for handle in handles:
        if handle not in parentHandle:
            browser.switch_to.window(handle)
    driver.should_be_current_page("https://twitter.com/saucelabs")


@pytest.mark.TC_003_06
def test_open_linkedin_page(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    parentHandle = browser.current_window_handle
    driver.click_element(*InventoryPageLocators.LINKEDIN_IMAGE_LINK)
    handles = browser.window_handles
    for handle in handles:
        if handle not in parentHandle:
            browser.switch_to.window(handle)
    driver.should_be_current_page("https://www.linkedin.com/company/sauce-labs/")



=======
@pytest.mark.TC_002_05
def test_about_link(browser):
    driver = InventoryPage(browser, link)
    driver.login_success(browser)
    driver.click_element(*InventoryPageLocators.OPEN_MENU_BUTTON)
    time.sleep(1)
    driver.click_element(*InventoryPageLocators.ABOUT_MENU_ITEM)
    driver.should_be_current_page("https://saucelabs.com/")
>>>>>>> main
