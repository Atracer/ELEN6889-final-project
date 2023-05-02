import re
import pandas as pd
import unicodedata
from emoji import demojize


def remove_emoji(text):
    return ''.join(c for c in text if not unicodedata.category(c).startswith('So'))

def preprocess_tweet(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#', '', text)
    text = text.lower()

    # Remove emojis
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+",
        flags=re.UNICODE,
    )
    text = emoji_pattern.sub(r'', text)

    # Remove emojis
    text = demojize(text)

    return text



file_name = 'apple.xlsx'
data = pd.read_excel(file_name)
# print(data.columns)
data['cleaned_text'] = data['tweet_text'].apply(preprocess_tweet)

# Filter tweets for Google and Amazon
keywords = ['google', 'amazon', 'goog', 'amzn']
data = data[data['cleaned_text'].str.contains('|'.join(keywords))]

#print data
print(data['cleaned_text'])


#Output data to csv
# output_file_name = 'cleaned_tweets.csv'
# data.to_csv(output_file_name, index=False)

