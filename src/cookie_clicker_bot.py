from dataclasses import dataclass
from locator import Locator
from selenium.common.exceptions import StaleElementReferenceException
from chrome_driver import ChromeDriver

@dataclass
class CookieClickerBot:
    driver: ChromeDriver

    def load_website(self, url):
        self.driver.get_url(url)

    def set_eng_language(self):
        eng_lang_button = self.driver.get_element(*Locator.ENG_LANG_BUTTON)
        if eng_lang_button is not None:
            eng_lang_button.click()

    def click_cookie(self):
        try:
            cookie_button = self.driver.get_element(*Locator.COOKIE_BUTTON)
            if cookie_button is not None:
                cookie_button.click()
        except StaleElementReferenceException:
            print('cookie button not present')

    def cookie_count(self):
        cookie_count_field = self.driver.get_element(*Locator.COOKIE_COUNT_FIELD)
        if cookie_count_field is not None:
            cookie_count_text = (cookie_count_field.text.split(' ')[0]).replace(',','')
            return int(cookie_count_text)

    def click_product(self, product_no: str):
        try:
            product_element = self.driver.get_element(*Locator.get_product_element(product_no))
            if product_element is not None:
                product_element.click()
        except StaleElementReferenceException:
            print('product element not present')

    def get_product_price(self,product_no: str):
        product_price_field = self.driver.get_element(*Locator.get_product_price_element(product_no))
        
        if product_price_field is not None:
            product_price_text = product_price_field.text.replace(',','')
            suffix_multipliers = {
            'million': 10**6,
            'billion': 10**9,
            'trillion': 10**12,
            'quadrillion': 10**15,
            'quintillion': 10**18,
            'septillion': 10**24
            }
            
            if product_price_text:
                for suffix, multiplier in suffix_multipliers.items():
                    if suffix in product_price_text:
                        product_price = (float(product_price_text.split(' ')[0])) * multiplier
                        return int(product_price)
                
                return int(product_price_text)

    def total_products(self):
        product_list = self.driver.get_elements(*Locator.PRODUCT_LIST)
        return len(product_list)