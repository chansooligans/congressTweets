# %%
import pandas as pd
import re
from gensim import corpora, models
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from tqdm import tqdm
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
tqdm.pandas()

# %%
df = pd.read_csv(f"../../data/tweets.csv")
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = re.sub(r'\b(?:https?://|www\.)\S+\b', '', text)
    tokens = word_tokenize(text.lower())  # Tokenize the text and convert to lowercase
    tokens = [token for token in tokens if token.isalpha()]  # Remove non-alphabetic tokens
    tokens = [token for token in tokens if token not in stop_words]  # Remove stopwords
    tokens = [lemmatizer.lemmatize(token) for token in tokens]  # Lemmatize the tokens
    return tokens

df['preprocessed_text'] = df["text"].progress_apply(preprocess_text)

# %%
# Create a dictionary representation of the documents
dictionary = corpora.Dictionary(df['preprocessed_text'])

# Convert the dictionary to a bag-of-words corpus
corpus = [dictionary.doc2bow(doc) for doc in df['preprocessed_text']]

# %%
%%time
# Perform topic modeling using LDA
lda_model = models.LdaModel(corpus, num_topics=10, id2word=dictionary, passes=10)

# %%
%%time
document_topics = [lda_model.get_document_topics(doc) for doc in corpus]

# %%
# Calculate the marginal topic distribution
marginal_topic_distribution = [0] * lda_model.num_topics
for topics in document_topics:
    for topic_num, prob in topics:
        marginal_topic_distribution[topic_num] += prob

# Normalize the marginal topic distribution
marginal_topic_distribution /= sum(marginal_topic_distribution)
marginal_topic_distribution = [
    (prob, topic_num) 
    for topic_num, prob in enumerate(marginal_topic_distribution)
]
marginal_topic_distribution = sorted(marginal_topic_distribution, key=lambda x: -x[0])

# %%
# Print the topics and their associated keywords
topics = lda_model.print_topics()

for prob, topic_num in marginal_topic_distribution:
    print(f"Topic #{topic_num}: Probability={prob}")
    print(f"\tWords: {topics[topic_num][1]}")

# %%
# %%
