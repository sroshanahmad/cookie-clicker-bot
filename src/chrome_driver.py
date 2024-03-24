from dataclasses import dataclass
from typing import ClassVar, Optional, List
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException

@dataclass
class ChromeDriver:
    driver_path: str
    service: Optional[Service] = None
    options: webdriver.ChromeOptions = webdriver.ChromeOptions()
    driver: Optional[webdriver.Chrome] = None
    wait_time : ClassVar[int] = 5

    def __post_init__(self):
        self.service = Service(executable_path=self.driver_path)
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.service)

    def get_url(self, url: str) -> None:
        if self.driver is not None:
            self.driver.get(url)

    def get_element(self, identifier: str, value: str) -> Optional[WebElement]:
        if self.driver is not None:
            try:
                WebDriverWait(self.driver, self.wait_time).until(
                    EC.presence_of_element_located((getattr(By, identifier.upper()), value)))

                return self.driver.find_element(getattr(By, identifier.upper()), value)
            except TimeoutException:
                print("Not able to get element")
                raise
        else:
            return None

    def get_elements(self, identifier: str, value: str) -> Optional[List[WebElement]]:
        if self.driver is not None:
            try:
                return self.driver.find_elements(getattr(By, identifier.upper()), value)
            except TimeoutException:
                print("Not able to get element list")
                raise
        else:
            return None

    def quit_browser(self) -> None:
        if self.driver is not None:
            self.driver.quit()