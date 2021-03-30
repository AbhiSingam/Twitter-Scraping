# Twitter Scraping
Here I wanted to find the top trending hashtag in Hyderabad and pick around 20000 tweets and analyze them to produce insights on the users, their followers and friends, and the language aspect of the corpus.  
Since querying 20000 tweets take a lot of time (due to the API's query rate limits), I've included a file called tweet_search_1.json which contains 20000 tweets with the hashtag #MUNLEE which was the top trending hashtag at the time of collection. Unfortunately due to GitHub file size restrictions, I was forced to remove 8000 of the posts in tweet_search_1.json. There are still 12000 tweets, but your results when testing with tweet_search_1.json may vary from my results mentioned below.  
The graphs and insights are diplayed upon request, i.e. you can pick which ones you want to see at the time of execution. 

`
Note: This takes a significant amount of time to run due to the twitterAPI's query limits.
`

### Executing the code:
The code can be executed by simply running one of the following:
```
python hashtag_analysis_twitter.py
```
or
```
python3 hashtag_analysis_twitter.py
```

Once you execute the code, you will be given the choice of which different functions of the code you would like to execute.  

### Required libraries:
The required libraries for this code are:  
- tweepy
- json
- jsonpickle
- re
- matplotlib
- tkinter
- matplotlib  
- pprint  
- collections
- plotly 
- wordcloud

### Different insights:
The different insights we obtain using this code are the following (for all these insight I used the tweets in tweet_search_1.json which contains tweets from #MUNLEE):  
- **Insight 1**: From analysing the devices used to make the tweets.  
    By analyzing the devices, we come to know that a majority (55%) of the users use an android device, while a significantly smaller number (35%) of users use an iPhone.  
    This kind of analysis may seem insignificant at first, but given that the hashtag being analyzed is related to football matches which are almost certainly streamed online, companies who wish to cater to a large audience of android users and football enthusiasts can be better equipped when advertizing on related advertising channels. This becomes more refined with later insights.  

- **Insight 2**: From analysing the commonly used words in the relevant tweets.  
    By analyzing the language used in the tweets, we can find the commonly used words (or buzzwords) used in these posts. From this, we can draw insights about what the popular references are in the community and what it is that the community at large is dicussing at a given time. This becomes especially useful when trying to interact with the community, but only in a few very niche situations.  

- **Insight 3**: From analysing the location of the users who posted the tweets.  
    By analysing the locations of the users we can find one very important piece of information, which is the general location of the users/consumers of the media under the hashtag. The reason this is so important is because it allows for a much better understanding of the community and its distibution.  
    This insight ties in well with the use-case of Insight 1, as with these a company can understand more about the consumers they wish to cater to and make more informed decisions to better cater to their prospective users.  
    From the selected set of tweets, we notice that a majority (>50%) of the users are posting from different parts of Nigeria. This allows for a better understanding of Insight 5 alongside being valuable information to have.  

- **Insight 4**: From analysing the commonly paired hashtags.  
    By analysing the hashtags that are commonly tweeted alongside the selected hashtag, we can find a direction to branch out in to analyze more about any aspect of the tweets or the users tweeting the tweets. This becomes especially useful when trying to do market research as shown in Insights 1 and 3. This also allows us to link different hashtags together as they may be similar in terms of the content posted under them.  

- **Insight 5**: From analysing the time of tweeting the tweets.  
    By analysing the time of tweetting the tweets, we can gain some useful insights, especially when paired with the user's location.  
    From just analysing the times of tweeting alone, we can find when the community is most active and when the hashtag is being viewed by the maximum number of people.  
    By pairing this with the location information of the users, we can find more specific information. An example of such an insight would be gauging the interest levels of the users/audience of these football matches. Are the tweets from certain places coming out as the match is going on or as soon as it ends, or are they coming up at a later time (for example, when it becomes morning for the place in question). Such information can depict how committed members in different areas of the world are to the sport/event.  
    Unfortunately, the value of this insight isn't shown when analyzing the tweets in tweet_search_1.json as they were collected with the "result_type" as "mixed", i.e. it gives both recent and popular posts (all the tweets ended up being tweeted within the same hour). This would work much better when using "popular" as the "result_type" as there would be a more varied time distribution. The issue with using "popular" is that you simply don't get enough posts to analyze when using "popular" instead of "mixed"  

- **Other possible insights**:  
    Some insights that I wanted to implement were not feasible given the duration it would take to test the code and query all this infomation and the deadline given for these tasks, and hence I'm mentioning them here.  
    
    - **Insight 6**: Analysing the likes on a tweet.  
        By analysing the likes on a tweet, we can find many different insights.  
        By analysing all the users who liked a certain tweet we can gauge the impact of using that hashtag on a post's reach. We can do this by analysing how many likes came from accounts that aren't followers/friends of the account that posted the tweet. Thus implying that these likes can from people who saw the tweet due to it showing up in their "explore" page (or twitter's equivalent of the "explore" page on instagram) or in general being recommended to them. This could provide insights about how much reach a post gains when adding certain hashtags.  
        By analysing the likes (considered to be an estimation of the reach of a tweet) a tweet has along with the words/phrases used in the tweet, we can accurately find the popular topics being discussed under certain hashtags. This insight simply improves upon the earlier mentioned insight in terms of measuring the effects of certain words and phrases on the reach of a post.

    - **Insight 7**: Analysing the comments on a post  
        The comments on a post are a valuable resource when trying to understand a community as the comments section is the forum for discussion about a post and generally has far more participation from users when compared to tweets.
        By analysing the comments on a post you can gain insights about WHY certain things are popular and how they are perceived by the community.  
        For example, Tesla's cybertruck gained massive popularity through memes. And the reason for this popularity wasn't because of how good/bad the truck was, but rather due to it's overly geometric design. Such information is lost when analysing the posts directly but can be gained by analysing the comments on a post.
    
    - **Insight 8**: Analysing the use of certain hashtags over a period of time.  
        Hashtags grow and fall in terms of popularity rapidly, and thus even though something may appear to be very influential or important, it may be something trivial. By analysing the frequency of use of a certain hashtag by the community in general we can better understand the relevance of the hashtag itself.

    - **Insight 9**: Analysing the timelines of users.  
        By analysing the timelines of users, we can find how frequently users use a certain hashtag, which serves a similar purpose to Insight 8, and also find out what interests the users who post a certain hashtag which will allow you to improve upon Insight 4.


### Resources used
Some of the important resources used when writing my code were:
- To obtain 20000 posts: https://stackoverflow.com/questions/22469713/managing-tweepy-api-search
- To learn about the tweepy module: http://docs.tweepy.org/en/latest/api.html
- To learn the basics of data analysis and insights: https://github.com/devanshmanu/UG1CHD
- To learn about text data visualization: https://www.pluralsight.com/guides/text-data-visualization-and-insights-in-python
- To learn how to use WordCloud: https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html
- To learn about using regular expressions: https://www.tutorialspoint.com/python/python_reg_expressions.htm
- To learn about using matplotlib: https://matplotlib.org/tutorials/introductory/pyplot.html
