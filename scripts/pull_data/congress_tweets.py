# %%
from congresstweets.twitter import api
from congresstweets import locs
from congresstweets import config
import pandas as pd
secrets = config.setup()

# %%
senators = pd.read_csv(f"{locs.DATA_LOC}/senator_handles.csv")
reps = pd.read_csv(f"{locs.DATA_LOC}/rep_handles.csv")

# %%
twitter = api.TwitterAPI(secrets=secrets)

# %%
twitter.get_tweets()
# %%
# %%
