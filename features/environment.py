from selenium import webdriver


def before_all(context):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    context.driver = driver


def after_all(context):
    context.driver.quit()
