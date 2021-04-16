# for different search terms and to get the reply count, retweet counts and other data from the tweets related to the search term.

import pandas as pd
import snscrape.modules.twitter as sntwitter


tweets_list2 = []


# terms=['fertile ground', 'food access', 'food insecurity', 'food security', 'food health', 'food deserts', 'food swamps','#fertilegroundjxn','#healthyfood']
term = 'food access'
geocode = '32.2998,-90.1848'
radius = '50km'
date = "2018-03-01"

term = input("Enter the term you want to search for in Twitter:")
geocode = input(
    "Enter the coordinates of location(Example for Jackson= 32.2998,-90.1848):")
radius = input("Enter radius in km(example-50km):")
date = input("Enter start date to search the data from(e.g. 2018-03-01):")
maxtweets = int(input("Enter max number of tweets allowed:"))

# for term in terms:
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(term+' geocode:'+geocode+','+radius+' since:'+date).get_items()):

    if i > maxtweets:
        break

    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.user.location,
                         tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount])


tweets_df2 = pd.DataFrame(tweets_list2, columns=[
                          'Datetime', 'Tweet Id', 'Text', 'Username', 'User Location', 'Reply Count', 'Retweet Count', 'Like Count', 'Quote Count'])
print(tweets_df2)

# tweets_df2.to_csv("demotweets.csv")
