from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd
from newspaper import Article
from newspaper import Config
import nltk


googlenews = GoogleNews(start='03/01/2018', end='03/21/2021')
googlenews.search('food insecurity Mississippi')
result = googlenews.result()
df = pd.DataFrame(result)

for i in range(2, 15):
    googlenews.getpage(i)
    result = googlenews.result()
    df = pd.DataFrame(result)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent
config.request_timeout = 50

list = []
for ind in df.index:
    try:
        dict = {}
        article = Article(df['link'][ind], config=config)
        article.download()
        article.parse()
        article.nlp()
        dict['Date'] = df['date'][ind]
        dict['Media'] = df['media'][ind]
        dict['Title'] = article.title
        dict['Article'] = article.text
        dict['Summary'] = article.summary
        list.append(dict)
    except:
        print("caught a timeout")
news_df = pd.DataFrame(list)
googlenews.clear()

news_df
