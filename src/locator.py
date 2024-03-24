from dataclasses import dataclass
from typing import ClassVar, Tuple

@dataclass
class Locator:
    ENG_LANG_BUTTON: ClassVar[Tuple[str,str]] = ('ID','langSelect-EN')
    COOKIE_BUTTON: ClassVar[Tuple[str, str]] = ('ID', 'bigCookie')
    COOKIE_COUNT_FIELD : ClassVar[Tuple[str,str]] = ('ID','cookies')
    PRODUCT_LIST: ClassVar[Tuple[str,str]] = ('XPATH',"//div[starts-with(@class, 'product locked disabled')]")

    @classmethod
    def get_product_element(cls, product_no: str) -> Tuple[str,str]:
        return ('ID',f"product{product_no}")
    
    @classmethod
    def get_product_price_element(cls, product_no: str) -> Tuple[str,str]:
        return ('ID',f"productPrice{product_no}")