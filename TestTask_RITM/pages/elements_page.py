from pages.base_page import BasePage
from locators.elements_page_locators import FormPageLocators as Locators

class FormPage(BasePage):

    def checkbox_WordFile(self):
        self.element_is_visible(Locators.ELEMENT_BTN_MAIN).click()
        self.element_is_visible(Locators.CHECK_BOX_MENU).click()
        self.element_is_visible(Locators.HOME_DIRT).click()
        self.element_is_visible(Locators.DOWNLOAD_DIRT).click()
        self.element_is_visible(Locators.CHECK_BOX_WF).click()
        if self.element_is_visible(Locators.RESPONSE).text == "wordFile":
            print("You have selected:wordFile")







