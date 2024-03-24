import os
from chrome_driver import ChromeDriver
from cookie_clicker_bot import CookieClickerBot

def set_webdriver_path() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    webdriver_path = os.path.join(parent_dir, 'bootstrap', 'chromedriver')
    return webdriver_path

if __name__ == "__main__":
    
    WEBDRIVER_PATH = set_webdriver_path()
    driver = ChromeDriver(driver_path=WEBDRIVER_PATH)

    bot = CookieClickerBot(driver)
    bot.load_website("https://orteil.dashnet.org/cookieclicker/")
    bot.set_eng_language()

    products_count = bot.total_products()
    while True:
        bot.click_cookie()
        total_cookies = bot.cookie_count()
        for product_no in range(0,products_count):
            product_price = bot.get_product_price(str(product_no))
            if product_price is not None and total_cookies >= product_price:
                bot.click_product(str(product_no))