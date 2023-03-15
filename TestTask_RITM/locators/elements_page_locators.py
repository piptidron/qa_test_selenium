from selenium.webdriver.common.by import By


class FormPageLocators:
    ELEMENT_BTN_MAIN = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]')
    CHECK_BOX_MENU = (By.XPATH, '//*[@id="item-1"]')
    HOME_DIRT = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')
    DOWNLOAD_DIRT = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button')
    CHECK_BOX_WF = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]')
    RESPONSE = (By.XPATH, '//*[@id="result"]/span[2]')
