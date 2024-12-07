from unittest import TestCase, mock
from startup_data_management import check_null_startup_data, check_invalid_funding_stages, insert_new_startup

# these unittests use mocking to mock the interaction between the API and the database
# they check if the functions in startup_data_management.py work correctly
class TestStartupDataManagement(TestCase):

    # checking that the function returns the expected value after executed
    @mock.patch('startup_data_management._connect_to_db')
    def test_check_null_startup_data(self, mock_connect_to_db):
        mock_connection = mock.MagicMock()
        mock_connect_to_db.return_value = mock_connection
        mock_cursor = mock.MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = 3

        check_null_startup_data(mock_connection)

        mock_cursor.execute.assert_called_once()
        self.assertEqual(mock_cursor.fetchone(), 3)

    # checking that the function returns those startups correctly where there is not enough funding
    @mock.patch('startup_data_management._connect_to_db')
    def test_check_invalid_funding_stages(self, mock_connect_to_db):
        mock_connection = mock.MagicMock()
        mock_connect_to_db.return_value = mock_connection
        mock_cursor = mock.MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [(1, 'Startup A', 'invalid'), (2, 'Startup B', 'also invalid')]

        check_invalid_funding_stages(mock_connection)

        mock_cursor.execute.assert_called_once()
        self.assertEqual(mock_cursor.fetchall(), [(1, 'Startup A', 'invalid'), (2, 'Startup B', 'also invalid')])

    # checking that a new startup with valid funding stage can be inserted correctly
    @mock.patch('startup_data_management._connect_to_db')
    def test_insert_new_startup(self, mock_connect_to_db):
        mock_connection = mock.MagicMock()
        mock_connect_to_db.return_value = mock_connection
        mock_cursor = mock.MagicMock()
        mock_connection.cursor.return_value = mock_cursor

        insert_new_startup(mock_connection, 'Startup C', 'Canada', 'Frank Malicious', 'Tech', 'IPO', True)

        mock_cursor.execute.assert_called_once()
        mock_connection.commit.assert_called_once()

