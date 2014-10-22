from . import BaseTestCase

from CodebenderTest import CodebenderTest


class TestCodebendertest(BaseTestCase):

    def test_something(self):
        self.assertEquals(
            'Hello World!',
            CodebenderTest(),
        )
