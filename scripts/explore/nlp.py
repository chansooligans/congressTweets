# %%
import pandas as pd
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
# Perform topic modeling using LDA
lda_model = models.LdaModel(corpus, num_topics=10, id2word=dictionary, passes=10)

# Print the topics and their associated keywords
for topic_num, words in lda_model.print_topics():
    print(f"Topic #{topic_num}: {words}")
