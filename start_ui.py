from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Chromedriver options
options = webdriver.ChromeOptions()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome("driver/chromedriver", chrome_options=options)
driver.set_page_load_timeout(25)

# Variables
ip = "10.204.217.60"
username = "admin"
password = "c0ntrail123"
domain = "admin_domain"
command_server_ip = "https://" + ip + ":8079"
driver.get(command_server_ip)

def login():
    driver.find_element_by_id("userName").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("domain").send_keys(domain)
    driver.find_element_by_xpath('//*[@id="form-submit"]/span').click()
    # time.sleep(15)

def create_vn():
    
    import pdb;pdb.set_trace()
    driver.find_element_by_class_name('jws-hamburger').click()
    menu = driver.find_element_by_xpath("//span[@class='sidebar-category overlay ant-dropdown-trigger']")
    menu.click()
    time.sleep(2)
    submenu = driver.find_element_by_class_name('overlay-virtual_networks')
    ActionChains(driver).move_to_element(menu).click(submenu).perform()

    CREATE = "//span[text()='Create']"
    driver.find_element_by_xpath(CREATE).click()
    VN_NAME = 'input[label="Name"]'
    driver.find_element_by_css_selector(VN_NAME).send_keys("vn1")
    ADD = "//span[text()='+ Add']/parent::button"
    driver.find_element_by_xpath(ADD).send_keys(Keys.ENTER)
    IPAM = "//div[text()='Select IPAM']"
    time.sleep(5)
    driver.find_element_by_xpath(IPAM).click()
    DEFAULT_DOMAIN = "//span[text()='default-domain:default-project:default-network-ipam']"
    time.sleep(5)
    driver.find_element_by_xpath(DEFAULT_DOMAIN).click()
    CIDR = 'input[label="CIDR"]'
    driver.find_element_by_css_selector(CIDR).send_keys("1.0.0.0/24")
    driver.find_element_by_xpath(CREATE).click()

def create_instance():
    driver.find_element_by_class_name('jws-hamburger').click()
    menu = driver.find_element_by_xpath("//span[@class='sidebar-category workloads ant-dropdown-trigger']")
    menu.click()
    time.sleep(2)
    submenu = driver.find_element_by_class_name('workloads-instances')
    ActionChains(driver).move_to_element(menu).click(submenu).perform()

    CREATE = "//span[text()='Create']"
    driver.find_element_by_xpath(CREATE).click()
    INSTANCE_NAME = 'input[label="Instance Name"]'
    driver.find_element_by_css_selector(INSTANCE_NAME).send_keys("vm1")
    IMAGE = "(//div[text()='Image']/parent::div)[2]"
    time.sleep(5)
    driver.find_element_by_xpath(IMAGE).click()
    CIRROS = "//li[@title='cirros2']"
    time.sleep(5)
    driver.find_element_by_xpath(CIRROS).click()
    FLAVOR = "//div[text()='Flavor']"
    time.sleep(5)
    driver.find_element_by_xpath(FLAVOR).click()
    F1 = "//li[@title='f1']"
    time.sleep(5)
    driver.find_element_by_xpath(F1).click()



if __name__ == '__main__':
    login()
    create_vn()
