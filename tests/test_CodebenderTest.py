from . import BaseTestCase

from CodebenderTest import CodebenderTest

from tests.cb_common import *


class TestCodebendertest(BaseTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(start_url)

    def tearDown(self):
        self.driver.close()

    def test_something(self):
        login(self.driver)
