from django.test import TestCase

# Create your tests here.


class BaseAPITestCase(TestCase):
    # TODO: Implement base test case creation and deletion to remove code duplication
    @classmethod
    def setUpTestData(cls):
        # set up test database
        pass

    @classmethod
    def tearDownTestData(cls):
        # drop test database
        pass
