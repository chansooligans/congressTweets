import requests
import time

class TwitterAPI:
    def __init__(self, secrets):
        self.bearer_token = secrets["twitter"]["bearer"]
        self.headers = self.create_headers()
    
    def create_headers(self):
        headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "User-Agent": "v2UserTweetsPython"
        }
        return headers

    def connect_to_endpoint(self, url, params=None):
        response = requests.request("GET", url, headers=self.headers, params=params)
        
        if response.status_code == 429:  # Too Many Requests
            print("Rate limit exceeded. Sleeping for 10 minutes.")
            time.sleep(10*60)  # Pause for 10 minutes
            return self.connect_to_endpoint(url, params)  # Retry the request
        elif response.status_code != 200:
            raise Exception(f"Request returned an error: {response.status_code}, {response.text}")
        
        return response.json()

    def get_user_id(self, twitter_handle):
        url = f"https://api.twitter.com/2/users/by/username/{twitter_handle}"
        json_response = self.connect_to_endpoint(url)
        return json_response['data']['id']

    def get_tweets(self, twitter_handle, tweet_count_min=500):
        user_id = self.get_user_id(twitter_handle)
        url = f"https://api.twitter.com/2/users/{user_id}/tweets"
        all_tweets = []
        pagination_token = None

        while len(all_tweets) < tweet_count_min:
            params = {
                'tweet.fields': 'created_at',
                'max_results': 100
            }
            if pagination_token:
                params['pagination_token'] = pagination_token

            json_response = self.connect_to_endpoint(url, params)
            tweets = json_response['data']
            all_tweets.extend(tweets)

            if 'meta' in json_response and 'next_token' in json_response['meta']:
                pagination_token = json_response['meta']['next_token']
            else:
                break

        return all_tweets
