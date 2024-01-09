"""Chrome"""
from selenium import webdriver
from main import ReSolver
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
resolver = ReSolver(driver)
resolver.chrome_solve()
sleep(500)

"""FireFox"""
from selenium import webdriver
from main import ReSolver
from time import sleep
options = webdriver.FirefoxOptions()
options.add_argument("--log-level=3")
driver = webdriver.Firefox(options=options)
driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
resolver = ReSolver(driver)
resolver.firefox_solver()
sleep(500)