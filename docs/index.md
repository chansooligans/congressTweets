# congressTweets documentation

This project aims to develop machine learning models for analyzing tweets from
U.S. Senators and Representatives, particularly by extracting and searching
based on topics.

## Dataset 

The input data for this project consists of approximately 500,000 tweets that
have been scraped for each U.S. senator and representative. These tweets form
the corpus on which our trained models are applied.


## Approach 1: Fake Data

To identify tweets about some specific topic, e.g. "broken US healthcare system", 
one approach is to construct fake training data:

To construct the training dataset, I manually created 20 representative 'fake'
tweets that accurately portray the sentiment and language used when discussing
broken U.S. healthcare. These tweets were labeled with a 1, signifying that the
tweet is about broken U.S. healthcare.

We also randomly sampled 20 tweets from the broader corpus that are not related
to broken U.S. healthcare, and labeled these tweets with a 0, signifying that
they do not pertain to broken U.S. healthcare.

In total, the training dataset comprises 40 labeled tweets.

These 40 labeled tweets are used to train various machine learning models, which
learn to differentiate between tweets about broken U.S. healthcare and those not
related to this topic. We apply a range of binary text classification models,
including Multinomial Naive Bayes, Support Vector Machine, Logistic Regression,
and others.

The trained models are then applied to the full corpus of tweets. The model
predictions can be evaluated for performance metrics such as precision, recall,
and F1-score.

From here, you can obtain more training data using an active learning loop and 
methods such as uncertainty sampling.

## Approach 2: Embeddings

[to be continued, e.g. Doc2Vec, GloVe, FastText, BERT, OpenAI]
