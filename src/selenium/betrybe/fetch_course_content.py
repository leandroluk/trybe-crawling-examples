import os
import time
import typing

import dotenv
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src._shared.decorators import step
from src.selenium._shared.selenium import Selenium


class FetchCourseContent(Selenium):
    """
    this crawler accesses the betrybe course by logging in, captures the links 
    to access the contents and returns a list with these links
    """

    def __init__(self, trybe_user: str, trybe_pass: str) -> None:
        super().__init__()
        self.trybe_user = trybe_user
        self.trybe_pass = trybe_pass

    @step
    def navigate_to_login_page(self) -> None:
        """
        navigate to login page and wait page is fully loaded
        """
        self.browser.get('https://app.betrybe.com/login')

        for _ in range(10):
            if self.check_if_page_has_loaded():
               return
            time.sleep(3)

        raise Exception("cant't load login page")

    @step
    def do_login(self) -> None:
        """
        do login using trybe_user and trybe_pass
        """
        last_error = None
        
        for attempts in range(3):
            try:
                # find email input and write user
                input_user: WebElement = self.browser \
                    .find_element_by_id('email')
                input_user.clear()
                input_user.send_keys(self.trybe_user)

                # find password input and write pass
                input_pass: WebElement = self.browser \
                    .find_element_by_id('password')
                input_pass.clear()
                input_pass.send_keys(self.trybe_pass)

                # find submit button of form and click them
                button_submit: WebElement = self.browser \
                    .find_element_by_css_selector('[type="submit"]')
                button_submit.click()

                # wait navigation to course page
                WebDriverWait(self.browser, 10).until(EC.url_changes)

                # wait render content
                for _ in range(10):
                    try:
                        self.browser\
                            .find_element_by_class_name('home-section__title') 
                    except:
                        time.sleep(3)

                # return when finish
                return
            except Exception as e:
                last_error = e
                self.browser.refresh()

        raise Exception(
            f"there were {attempts} unsuccessful login "
            f"attempts. last error: {str(last_error)}"
        )

    @step
    def extract_content_links(self) -> typing.List[str]:
        """
        with course page is loaded, find all content link's and extract this
        """
        last_error = None

        for _ in range(3):
            try:
                items: typing.List[WebElement] = self.browser\
                    .find_elements_by_css_selector('a.ada-card')
                links = [i.get_attribute('href') for i in items]

                return links
            except Exception as e:
                last_error = e

        raise Exception(f"can't extract links. last_error: {str(last_error)}")
                

    @step
    def run(self) -> typing.List[str]:
        """
        the magic is here 😎
        """
        self.navigate_to_login_page()
        self.do_login()
        links = self.extract_content_links()

        return links


if __name__ == '__main__':
    # load environment variables of file "<rootPath>/.env"
    dotenv.load_dotenv()

    # get environment values
    TRYBE_USER = os.getenv('TRYBE_USER')
    TRYBE_PASS = os.getenv('TRYBE_PASS')

    # open closure with crawler instance, closing browser on finish
    with FetchCourseContent(TRYBE_USER, TRYBE_PASS) as crawler:
        # call crawler
        result = crawler.run()

    # pretty print result of crawling
    print("\n Link's found:\n")
    [print(f"- {link}") for link in result]
