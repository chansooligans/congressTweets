# %%
from IPython import get_ipython
if get_ipython() is not None:
    get_ipython().run_line_magic("load_ext", "autoreload")
    get_ipython().run_line_magic("autoreload", "2")

from congresstweets.model import pipeline
from congresstweets import twitter, locs
from congresstweets.twitter import fake_tweets
import glob
import pandas as pd
import seaborn as sns
sns.set(rc={'figure.figsize':(9,4)})
files=glob.glob(f"{locs.DATA_LOC}/senators/*") + glob.glob(f"{locs.DATA_LOC}/representatives/*") 

# %%
fake = fake_tweets.FakeDF(fake_tweets.STOLEN_ELECTIONS).df
tweets = twitter.tweets.TweetsTable(files=files, loc=locs.DATA_LOC)
df = tweets.df

# %%
sample = tweets.df.sample(100)
df = pd.concat([
    fake.assign(label=1), 
    sample[["id", "text"]].assign(label=0)
])

# %%
pipe = pipeline.Pipe()
pipe.fit(df["text"], df["label"])


# %%
pipe.search.best_estimator_

# %%
# Predict the test set results
# tweets.df["label"] = text_clf.search.predict(tweets.df["text"])
tweets.df["p"] = pipe.search.predict_proba(tweets.df["text"])[:,1]

# %%
tweets.df.sort_values("p", ascending=False)["text"].head(20).values

# %%
