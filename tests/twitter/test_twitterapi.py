import pytest
from unittest.mock import patch, Mock
from congresstweets.twitter.api import TwitterAPI

class TestTwitterAPI:

    @patch('requests.request')
    def test_get_tweets(self, mock_request):
        # Set up the mock request
        mock_request.return_value = Mock()
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {
            'data': {'id': '1', 'text': 'Hello, world!', 'created_at': '2020-01-01T00:00:00Z'},
            'meta': {}
        }

        # Set up the TwitterAPI object
        secrets = {'twitter': {'bearer': 'test_bearer_token'}}
        api = TwitterAPI(secrets)

        # Call the method under test
        tweets = api.get_tweets('test_handle')

        # Assert that the tweets were returned correctly
        expected_tweets = ["id", "text", "created_at"]
        assert tweets == expected_tweets
