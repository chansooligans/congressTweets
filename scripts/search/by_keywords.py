# %%
from IPython import get_ipython
if get_ipython() is not None:
    get_ipython().run_line_magic("load_ext", "autoreload")
    get_ipython().run_line_magic("autoreload", "2")
from congresstweets import twitter, locs
import glob
files=glob.glob(f"{locs.DATA_LOC}/senators/*") + glob.glob(f"{locs.DATA_LOC}/representatives/*") 

# %%
tweets = twitter.tweets.TweetsTable(files=files, loc=locs.DATA_LOC)
tweets.df

# %%
tweets.df["text_clean"] = tweets.df["text"].str.lower()

# %%
tweets.df.loc[
    tweets.df["text_clean"].str.contains("health")
].sample(10)["text"].values

# %%
