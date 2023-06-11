# %%
from congresstweets.twitter import api
from congresstweets import locs, config, utils
import pandas as pd
secrets = config.setup()

senators = utils.get_handles(f"{locs.DATA_LOC}/senator_handles.csv")
reps = utils.get_handles(f"{locs.DATA_LOC}/rep_handles.csv")

# usage example to download tweets:
twitter = api.TwitterAPI(secrets=secrets)
tweets = twitter.get_tweets(twitter_handle=senators[0])

