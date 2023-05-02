from sentiment_analysis import sentiment_text
from text_regulation import get_clean_text, preprocess_tweet


file_name = 'apple.xlsx'

data = get_clean_text(preprocess_tweet(file_name))

print(data)

summary = sentiment_text(data)

#print data
# print(summary)


#Output data to csv
output_file_name = 'cleaned_tweets.csv'
data.to_csv(output_file_name, index=False)