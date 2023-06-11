# %%
from IPython import get_ipython
if get_ipython() is not None:
    get_ipython().run_line_magic("load_ext", "autoreload")
    get_ipython().run_line_magic("autoreload", "2")

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import pandas as pd

from congresstweets import twitter, locs
from congresstweets.twitter import fake_tweets
import glob
files=glob.glob(f"{locs.DATA_LOC}/senators/*") + glob.glob(f"{locs.DATA_LOC}/representatives/*") 

# %%
tweets = twitter.tweets.TweetsTable(files=files, loc=locs.DATA_LOC)
tweets.df




# Assume you have a DataFrame `df` with 'text' and 'label' columns
df = pd.read_csv('your_data.csv') 

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], random_state=42)

# Create a pipeline that vectorizes the text, applies TF-IDF, and then applies Multinomial Naive Bayes
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB()),
])

# Train the classifier
text_clf.fit(X_train, y_train)

# Predict the test set results
y_pred = text_clf.predict(X_test)

# Evaluate performance
print(classification_report(y_test, y_pred))
