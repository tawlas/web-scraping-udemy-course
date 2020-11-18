from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from shutil import which
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")

# chrome_path = which("chromedriver")
chrome_path = "./chromedriver"

driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
driver.get("https://duckduckgo.com")
# search_input = driver.find_element_by_xpath(
#     "(//input[contains(@class, 'js-search-input')])[1]")
search_input = driver.find_element_by_id("search_form_input_homepage")
search_input.send_keys("My user agent")

# search_btn = driver.find_element_by_id("search_button_homepage")
# search_btn.click()

search_input.send_keys(Keys.ENTER)


# driver.close()
