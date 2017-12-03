#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#定位元素的两种写法
# driver.find_element_by_id('kw')
# driver.find_element(By.ID,'kw')

class Page:
    '''
    基本类，用于所有页面的继承
    '''
    login_url = 'http://www.126.com'
    def __init__(self,selenium_driver,base_url=login_url,parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent
        self.tabs = {}

    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(),'Did not land on %s'% url

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self,src):
        return self.driver.execute_script(src)

    def send_keys(self,loc,value,clear_first=True,click_first=True):
        try:
            loc = getattr(self,'_%s'%loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print '%s page does not have "%s" locator'%(self.loc)

class LoginPage(Page):
    '''
    登录页面模型
    '''
    url = '/'

    #定位器
    account_login_loc = (By.ID,'lbNormal')
    type_iframe_loc = (By.XPATH,"//div[@id='loginDiv']/iframe")
    username_loc = (By.NAME,'email')
    password_loc = (By.NAME,'password')
    submit_loc = (By.ID,'dologin')
    success_username_loc = (By.ID,'spnUid')

    #Action
    def open(self):
        self._open(self.url)

    def account_login(self):
        self.find_element(*self.account_login_loc).click()

    def type_iframe(self):
        xf = self.find_element(*self.type_iframe_loc)
        self.driver.switch_to_frame(xf)

    def type_ifram_out(self):
        self.driver.switch_to_default_content()

    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()

    def success_username(self):
        text = self.find_element(*self.success_username_loc).text
        return text

def test_user_login(driver,username,password):
    '''
    测试获取的用户名密码，是否可以登录
    '''
    login_page = LoginPage(driver)
    login_page.open()
    login_page.account_login()
    login_page.type_iframe()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()
    login_page.type_ifram_out()
    sleep(8)

def main():
    try:
        #selenium
        driver = webdriver.Chrome()
        username = 'testingwtb'
        password = 'a123456'
        test_user_login(driver,username,password)
        login_page = LoginPage(driver)
        user = login_page.success_username()
        assert (user == 'testingwtb@126.com'),u'用户名称不匹配，登录失败！'
    finally:
        #关闭浏览器窗口
        driver.close()

if __name__ == '__main__':
    main()