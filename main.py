from sentiment_analysis import sentiment_text
from text_regulation import get_clean_text, preprocess_tweet


def main():
    file_name = 'apple.xlsx'

    data = get_clean_text(preprocess_tweet(file_name))

    summary = sentiment_text(data)

    #print data
    print(summary)


    #Output data to csv
    # output_file_name = 'sentiment_apple.csv'
    # summary.to_csv(output_file_name, index=False)

if __name__ == '__main__':
    main()

