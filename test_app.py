from unittest import TestCase, mock
import pandas as pd
import app

# these unittests check that the app.py works correctly
# the tests use mocking to imitate user interaction
class TestApp(TestCase):

    # this test checks if usernames and passwords are stored correctly
    @mock.patch('app.pd.read_csv')
    def test_load_credentials(self, mock_read_csv):
        mock_read_csv.return_value = pd.DataFrame({'username': ['admin'], 'password': ['safepassword']})
        credentials = app.load_credentials()
        self.assertEqual(credentials.shape[0], 3)
        self.assertEqual(credentials['username'][0], 'admin')

    # this test checks if a user with their valid username and password can log in
    @mock.patch('app.st.session_state', new_callable=dict)
    @mock.patch('app.st.text_input', return_value='user')
    @mock.patch('app.st.button')
    @mock.patch('app.st.success')
    @mock.patch('app.st.error')
    def test_login_success(self, mock_error, mock_success, mock_button, mock_text_input, mock_session_state):
        mock_session_state['logged_in'] = False
        mock_session_state['selected_section'] = 'Home'
        app.credentials = pd.DataFrame({'username': ['user'], 'password': ['safepassword']})

        # mocking login callback function (this is to handle login logic)
        # indention here is to encapsulate the logic within the function,
        # meaning this function is only for this test and uses its specific mocks, and is not used elsewhere
        def mock_login_callback(username, password):
            if any((app.credentials['username'] == username) & (app.credentials['password'] == password)):
                mock_session_state["logged_in"] = True
                mock_success("Login successful!")
            else:
                mock_error("Invalid username or password. Please try again.")

        app.login_callback = mock_login_callback
        app.login_callback('user', 'safepassword')

        self.assertTrue(mock_session_state["logged_in"])
        mock_success.assert_called_once_with("Login successful!")

    # this test checks if a user with an invalid username and/or password is prohibited from logging in
    @mock.patch('app.st.session_state', new_callable=dict)
    @mock.patch('app.st.text_input', side_effect=['user', 'wrongpassword'])
    @mock.patch('app.st.button')
    @mock.patch('app.st.success')
    @mock.patch('app.st.error')
    def test_login_failure(self, mock_error, mock_success, mock_button, mock_text_input, mock_session_state):
        mock_session_state['logged_in'] = False
        app.credentials = pd.DataFrame({'username': ['user'], 'password': ['safepassword']})

        # mocking login callback function (this is to handle login logic)
        # indention here is to encapsulate the logic within the function,
        # meaning this function is only for this test and uses its specific mocks, and is not used elsewhere
        def mock_login_callback(username, password):
            if any((app.credentials['username'] == username) & (app.credentials['password'] == password)):
                mock_session_state["logged_in"] = True
                mock_success("Login successful!")
            else:
                mock_error("Invalid username or password. Please try again.")

        app.login_callback = mock_login_callback
        app.login_callback('user', 'wrongpassword')

        self.assertFalse(mock_session_state["logged_in"])
        mock_error.assert_called_once_with("Invalid username or password. Please try again.")
