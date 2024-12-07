import unittest.mock
from unittest import TestCase, mock
from data_value_check import validate_data, check_invalid_date_rages, ensure_not_null, check_null_values, insert_pep, check_eu_countries_blacklist

# these unittests test the functions in data_value_check.py
# the tests check whether different data types are validated correctly
# and whether valid and invalid data are distinguished correctly
class TestDataValueCheck(TestCase):
    def test_validate_data_valid_string(self):
        expected = True
        result = validate_data("name", "Frank Malicious", str)
        self.assertEqual(expected, result)

    def test_validate_data_invalid_string(self):
        expected = ValueError
        with self.assertRaises(expected):
            validate_data("name", "Frankie001", str)

    def test_validate_data_valid_value(self):
        expected = True
        result = validate_data("age", 30, "value")
        self.assertEqual(expected, result)

    def test_validate_data_invalid_value(self):
        expected = ValueError
        with self.assertRaises(expected):
            validate_data("age", "thirty", "value")

    def test_validate_data_valid_date(self):
        expected = True
        result = validate_data("date_of_birth", "1973-05-13", "date")
        self.assertEqual(expected, result)

    def test_validate_data_invalid_date(self):
        expected = ValueError
        with self.assertRaises(expected):
            validate_data("date_of_birth", "1973-13-05", "date")

    @mock.patch('data_value_check.connection')
    def test_check_invalid_date_ranges(self, mock_connection):
        mock_cursor = mock.MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            (1, "Frank Malicious", "1899-05-13"),
            (2, "Paige Notfound", "2025-06-06")
        ]

        check_invalid_date_rages(mock_connection)

        mock_cursor.execute.assert_called_with(
            """SELECT id, full_name, date_of_birth 
            FROM PEP_Identification.pep_individuals 
            WHERE pep_individuals.date_of_birth < '1900-01-01' 
            OR date_of_birth < CURRENT_DATE()"""
        )

    def test_ensure_not_null_valid_value(self):
        expected = True
        result = ensure_not_null("name", "Frank Malicious")
        self.assertEqual(expected, result)

    def test_ensure_not_null_null_value(self):
        expected = ValueError
        with self.assertRaises(expected):
            ensure_not_null("name", None)

    def test_ensure_not_null_empty_value(self):
        expected = ValueError
        with self.assertRaises(expected):
            ensure_not_null("name", "")

    @mock.patch('data_value_check.connection')
    def test_check_null_values(self, mock_connection):
        mock_cursor = mock.MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = 3

        check_null_values("startups", "name")

        mock_cursor.execute.assert_called_with(
            """SELECT COUNT(*) 
            FROM startups 
            WHERE name IS NULL"""
        )

    @mock.patch('data_value_check.connection')
    def test_insert_pep(self, mock_connection):
        mock_cursor = mock.MagicMock()
        mock_connection.cursor.return_value = mock_cursor

        insert_pep(mock_connection, "Frank Malicious", "CEO", "Canada", "1973-08-24")

        mock_cursor.execute.assert_called_with(
            """INSERT INTO PEP_Identification.pep_individuals 
            (full_name, job_title, country, date_of_birth) 
            VALUES (%s, %s, %s, %s),
            ("Frank Malicious", "CEO", "Canada", "1973-08-24")"""
        )
        mock_connection.commit.assert_called_once()

    @mock.patch('data_value_check.connection')
    def test_check_eu_countries_blacklist(self, mock_connection):
        mock_cursor = mock.MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = "Russia"

        check_eu_countries_blacklist(mock_connection, "Russia")

        mock_cursor.execute.assert_called_with(
            """SELECT * 
            FROM eu_countries_blacklist 
            WHERE country_name = "Russia"""
        )
