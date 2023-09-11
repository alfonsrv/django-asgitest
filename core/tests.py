from unittest import TestCase

from channels.db import database_sync_to_async
from channels.testing import ChannelsLiveServerTestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from selenium import webdriver
from selenium.webdriver.common.by import By

User = get_user_model()


class TestRegular(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_something_that_will_pass(self):
        user_staff = User.objects.create(
            email='foo@bar.com',
            password=make_password('hunter42'),
            is_staff=True
        )


class ChatTests(ChannelsLiveServerTestCase):
    serve_static = True  # emulate StaticLiveServerTestCase

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        try:
            # NOTE: Requires "chromedriver" binary to be installed in $PATH
            cls.driver = webdriver.Chrome()
        except:
            super().tearDownClass()
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    async def test_when_chat_message_posted_then_seen_by_everyone_in_same_room(self):
        await self._enter_admin()
        import time; time.sleep(5)

    @database_sync_to_async
    def _enter_admin(self):
        self.driver.get(self.live_server_url + "/admin/")
        user_staff = User.objects.create(
            username='test',
            email='foo@bar.com',
            password=make_password('hunter42'),
            is_staff=True,
        )
        import time; time.sleep(5)
        self.driver.find_element('name', 'username').send_keys(user_staff.username)
        self.driver.find_element('name', 'password').send_keys('hunter42')
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        import pdb; pdb.set_trace()

    def _open_new_window(self):
        self.driver.execute_script('window.open("about:blank", "_blank");')
        self._switch_to_window(-1)
