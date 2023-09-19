from channels.testing import ChannelsLiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.by import By


class DatabaseTests(ChannelsLiveServerTestCase):
    serve_static = True  # emulate StaticLiveServerTestCase

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        try:
            User.objects.create(
                username='test0815',
                email='test0815@foo.com',
            )
            # NOTE: Requires "chromedriver" binary to be installed in $PATH
            cls.driver = webdriver.Chrome()
        except:
            super().tearDownClass()
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_user_model_creation(self):
        try:
            self._open_new_window()
            self.driver.get(self.live_server_url + "/chat/test/")
            self.assertTrue(
                self.driver.find_elements(
                    by=By.CSS_SELECTOR, value="#user-test0815"
                ),
                "User created in setup is not available in frontend",
            )
            import time; time.sleep(5)
        finally:
            self._close_all_new_windows()

    # === Utility ===

    def _open_new_window(self):
        self.driver.execute_script('window.open("about:blank", "_blank");')
        self._switch_to_window(-1)

    def _close_all_new_windows(self):
        while len(self.driver.window_handles) > 1:
            self._switch_to_window(-1)
            self.driver.execute_script("window.close();")
        if len(self.driver.window_handles) == 1:
            self._switch_to_window(0)

    def _switch_to_window(self, window_index):
        self.driver.switch_to.window(self.driver.window_handles[window_index])
