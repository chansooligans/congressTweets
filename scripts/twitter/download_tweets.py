# %%
from IPython import get_ipython
if get_ipython() is not None:
    get_ipython().run_line_magic("load_ext", "autoreload")
    get_ipython().run_line_magic("autoreload", "2")
import pandas as pd
import tqdm
import time
import glob
from ideoquant.twitter.api import TwitterAPI
from ideoquant import config
secrets = config.setup()

# %% [markdown]
"""
# Senators 
"""

# %%
senators = pd.read_csv("../../data/senator_handles.csv")
senators = senators["Link"].str.split("/").str[-1]

# %%
# Create an instance of TwitterAPI
twitter_api = TwitterAPI(secrets)

# %%
downloaded = glob.glob("../../data/senators/*")
for senator in tqdm.tqdm(senators):
    print(senator)
    fp_out = f"../../data/senators/{senator}.csv"
    if fp_out in downloaded:
        continue
    if not senator:
        continue
    tweets = twitter_api.get_tweets(senator, tweet_count_min=1000)
    df = pd.DataFrame(tweets)
    df.to_csv(fp_out, index=False)
    time.sleep(30)

# %% [markdown]
"""
# Representatives
"""

# %%
representatives = pd.read_csv("../../data/rep_handles.csv")
representatives = representatives["Link"].str.split("/").str[-1]

# %%
# Create an instance of TwitterAPI
twitter_api = TwitterAPI(secrets)

# %%
downloaded = glob.glob("../../data/representatives/*")
for representative in tqdm.tqdm(representatives):
    print(representative)
    fp_out = f"../../data/representatives/{representative}.csv"
    if fp_out in downloaded:
        continue
    if not representative:
        continue
    tweets = twitter_api.get_tweets(representative, tweet_count_min=1000)
    df = pd.DataFrame(tweets)
    df.to_csv(fp_out, index=False)
    time.sleep(30)

# %%
representatives

