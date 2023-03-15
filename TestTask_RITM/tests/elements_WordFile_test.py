from pages.elements_page import FormPage


class TestFormPage:

    def test_WordFile(self, driver):
        form_page = FormPage(driver,"https://demoqa.com")
        form_page.open()
        form_page.checkbox_WordFile()


