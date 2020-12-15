import time
from selenium import webdriver

# webdriver from Chrome
PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome = webdriver.Chrome(PATH)

# Link to the page
PAGE = "https://www.bestbuy.com/site/madden-nfl-21-playstation-4-playstation-5/6407594.p?skuId=6407594"
chrome.get(PAGE)

purchaseButton = False

while not purchaseButton:
    try:
        addToCart = addButton = chrome.find_element_by_class_name("btn-prim")

        print("Button is not ready at this time.")

        time.sleep(1)
        chrome.refresh()
    except:
        addToCart = addButton = chrome.find_element_by_class_name("fulfillment-add-to-cart-button")

        print("Button was clicked.")
        addToCart.click()
        purchaseButton = True
goToCart = addToCartButton = chrome.find_element_by_class_name("btn btn-secondary btn-sm btn-block ")
goToCart.click()
print("Go to Cart was clicked")
