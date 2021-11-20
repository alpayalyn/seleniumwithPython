from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")


driver.get("https://www.lcwaikiki.com/tr-TR/TR")

class LCW:
    CATEGORY_PAGE_1 = (By.CSS_SELECTOR, '.sf-with-ul')
    CHOOSE_SIZE = (By.CSS_SELECTOR, '//a[@size='M']') # [0] sıfırı alması lazım ama almadi SS kontrol https://prnt.sc/203kf75
    PRODUCT_PAGE = (By.CSS_SELECTOR, '.product-item-wrapper')
    ADD_TO_CART = (By.CSS_SELECTOR, '.col-xl-12')
    CART_PAGE = (By.CSS_SELECTOR, '.header-cart')
    MAIN_PAGE = (By.CSS_SELECTOR, '.header-logo.img-logo')

    HEADER_CONTAINER = (By.CSS_SELECTOR, '.div-header-container') #check for first page
    MOST_SOLD = (By.CSS_SELECTOR, '.uzun.visible-lg.visible-md') #check for second page
    ADD_TO_CART_CHECK = (By.CSS_SELECTOR, '.col-xs-12"') #check for add to cart
    MEN_BREADCRUMB = (By.xp, "//a[@href='/tr-TR/TR/urun-grubu/erkek']") # $x("//a[@href='/tr-TR/TR/urun-grubu/erkek']")[2]
    CART_PAGE_CHECK = (By.CSS_SELECTOR, '.cart-square-link')

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.wait = WebDriverWait(self.driver, 15)

    def test_navigate(self):
        assert self.wait.until(ec.element_to_be_clickable(self.HEADER_CONTAINER))[0].is_displayed() "En üstteki header yoktur bu da anasayfada olmadığımızı belirtir." #We are trying to be sure about are we on main page or not
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE_1))[1].click()
        assert self.wait.until(ec.element_to_be_clickable(self.MEN_BREADCRUMB))[2].is_displayed() "There is no 'Men' section in breadcrumb" #We are trying to be sure about are we on product page or not
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[1].click() # click the item
        assert self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART_CHECK))[10].is_displayed() "check for add to cart and there is none." #We are trying to be sure about are we on product page or not
        self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE_PAGE))[0].click()
        # ürün eklendi ancak sonrasındaki kontrol nasıl yapılaiblir onu düşün. sepete git çıkıyor karşına ondan yürüyebilirsin.
        self.wait.until(ec.presence_of_all_elements_located(self.CART_PAGE))[0].click()
        assert self.wait.until(ec.element_to_be_clickable(self.CART_PAGE_CHECK)).is_displayed() "Ödeme sayfasına geçiniz kısmı yoktur butonu yoktur." #We are trying to be sure about are we on product page or not
        self.wait.until(ec.presence_of_all_elements_located(self.MAIN_PAGE))[0].click()
        assert self.wait.until(ec.element_to_be_clickable(self.HEADER_CONTAINER)).is_displayed() "En üstteki header yoktur bu da anasayfada olmadığımızı belirtir." #We are trying to be sure about are we on main page or not

