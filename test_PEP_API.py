from unittest import TestCase, mock
from PEP_API import search_pep

# these unittests check the functions in PEP_API.py and check if the functions work correctly in different situations
# the tests are mocking the interaction between the API and the database
class TestSearchPEPAPI(TestCase):

    # this tests if an existing PEP can be found and if the correct result is printed as the output
    @mock.patch('PEP_API.requests.post')
    @mock.patch('builtins.print')
    def test_find_pep(self, mock_print, mock_post):
        mock_response = mock.Mock()
        mock_response.json.return_value = {
            "responses": {
                "q1": {
                    "results": [
                        {
                            "properties": {
                                "name": ["Frank Dishonest"],
                                "topics": ["Armed robbery"]
                            },
                            "score": 0.9
                        }
                    ]
                }
            }
        }
        mock_post.return_value = mock_response
        search_pep("Frank Dishonest")

        expected_calls = [
            ("Found matches for 'Frank Dishonest':",),
            ("Name: Frank Dishonest",),
            ("Score: 0.9",),
            ("Topics: Armed robbery",)
        ]

        for expected in expected_calls:
            result = mock_print.call_args_list
            self.assertIn(mock.call(*expected), result)

    # this tests if the function identifies that the name is missing, and displays the correct error message
    @mock.patch('builtins.print')
    def test_no_name(self, mock_print):
        search_pep("")
        # checking if the error message works
        expected = "Error: Name is required!"
        search_pep("")
        result = mock_print.call_args[0][0]
        self.assertEqual(expected, result)

    # this mocks a situation when there is no match
    # the test checks whether the correct error message is displayed in this case
    @mock.patch('PEP_API.requests.post')
    @mock.patch('builtins.print')
    def test_no_matches(self, mock_print, mock_post):
        mock_response = mock.Mock()
        mock_response.json.return_value = {
            "responses": {
                "q1": {
                    "results": []
                }
            }
        }

        mock_post.return_value = mock_response
        search_pep("unknown person")
        expected = "No matches found."
        result = mock_print.call_args[0][0]
        self.assertEqual(expected, result)

    # this mocks an API connection error and checks if the correct error message is displayed
    @mock.patch('PEP_API.requests.post')
    @mock.patch('builtins.print')
    def test_api_connection_error(self, mock_print, mock_post):
        mock_post.side_effect = Exception("Connection error")
        search_pep("Frank Dishonest")
        self.assertTrue(mock_print.called, "Print was not called.")
        expected = "Error connecting to OpenSanctions API: Connection error"
        result = mock_print.call_args[0][0]
        self.assertEqual(expected, result)

