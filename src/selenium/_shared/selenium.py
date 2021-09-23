import abc
import os
import platform

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Selenium(metaclass=abc.ABCMeta):
    """
    abstract base class to use selenium as crossplatform and maintain any common
    method
    """
    browser: WebDriver

    def __init__(self) -> None:
        script_dirname = os.path.dirname(__file__)
        system = platform.system()

        if system == 'Linux':
            file_name = 'chromedriver_linux'
        elif system == 'Darwin':
            file_name = 'chromedriver_macos'
        else:
            file_name = 'chromedriver_windows.exe'

        file_path = os.path.join(script_dirname, file_name)

        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')

        self.browser = webdriver.Chrome(file_path, options=options)

    def check_if_page_has_loaded(self) -> bool:
        """
        check if page is full loaded
        """
        page_state = self.browser.execute_script('return document.readyState;')
        return page_state == 'complete'

    @abc.abstractmethod
    def run(self):
        raise Exception('not implemented yet.')

    def __enter__(self):
        return self

    def __exit__(self, *args):
        """
        when finish crawler needs close browser to no dispend resources
        """
        try:
            self.browser.close()
        except:
            pass
