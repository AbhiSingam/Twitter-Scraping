import tweepy
import json
import jsonpickle
import re
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from pprint import pprint
from collections import Counter, OrderedDict
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def get_device_counts(tweet_list):
    tweet_device = Counter()
    for tweet in tweet_list:
        tweet_device[tweet['source']] += 1
    tweet_device = tweet_device.most_common(10)
    return tweet_device


def make_word_cloud(tweet_text, stopwords):

    wordcloud = WordCloud(background_color="white", stopwords=stopwords, width=1000, height=1000).generate(tweet_text)

    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.show()

auth = tweepy.OAuthHandler('ww7ffh1BmzyfaQl0yFBDpz7LK',
                           'PIfqesHxGqbXkAU6WZOfM6Y3zO81RDeqfGZiy0Z3suBu3CWilB')
auth.set_access_token('1340274461333864448-hxmqrGS0PdgGHKaLubQMPYmWJgz0wv',
                      'kOhYrBofsrOZ6W9JhG3y4vdZJESkWWl0H73Em1kTbW7wj')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
if (not api):
    print("Authentication failed")
    print("Ending program")
else:
    print("Authentication succeeded")

    print("Please specify below which functions of this code you would like to execute. The input should be a number with the digit-codes of each function you want to execute being present in the number.")
    print("i.e. If you want to execute the functions 1, 2, and 4, you should enter 124 or any permutation of the digits.")
    print("1 - Get fresh tweets (if not specified, the existing tweets in tweet_search_1.json will be used)\n2 - Show analysis of the devices used to post the selected tweets\n3 - Show analysis of the most common words used in the tweets\n4 - Show analysis of tweet location (only considers tweets with a mentioned location)\n5 - Show anaysis of hashtags commonly paired with the selected hashtag")
    val = input("Which functions would you like to execute? ")

    flags = {}

    for i in range(100):
        flags[str(i)] = 0

    for char in val:
        flags[char] = 1
    
    # print(flags)

    file_name = 'tweet_search_1.json'
    if flags['1'] == 1:
        file_name = input("Please enter a file path to store the tweets: ")

        # CODE TO FIND THE TOP TRENDING HASHTAG IN HYD(2295414) AND STORE 20000 TWEETS WITH THE HASHTAG IN A FILE CALLED TWEET_SEARCH_1.JSON

        print("Looking for the top hashtag in HYD")
        tags = api.trends_place(2295414)
        print("\nThe top hashtag in HYD is: " + tags[0]['trends'][1]['name'])
        print("Collecting tweets with the hashtag " + tags[0]['trends'][1]['name'])
        print("\nThis takes a LONG time, better find something to do while you wait. The reason why it takes so long is because the tweets have to be queried from twitter, and the rate of queries to twitter is capped, which means you'll have to wait while the cap replenishes and is then used up again repeatedly. I'd recommend coming back in about an hour or changing the number of tweets being analyzed and running it from scratch.\n")

        

        query = tags[0]['trends'][1]['name']
        max_tweets = 1000
        searched_tweets = [status for status in tweepy.Cursor(
            api.search, q=query, result_type="mixed").items(max_tweets)]

        print("Collected " + str(len(searched_tweets)) + " tweets")

        with open(file_name, 'w') as f:
            for tweet in searched_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')


    # NOW WE ANALYZE THE 20000 COLLECTED TWEETS


    # WHAT DEVICES DO THE USERS USE TO POST THESE POSTS
    # WHAT WORDS ARE COMMONLY SEEN IN POSTS WITH THIS HASHTAG?
    # LANG OF THE POSTS                         (Removed :(, due to the lack of actual info regarding it)
    # LOCATION OF THE TWEETS
    # WHERE ARE THE USERS FROM? (WHEN POSSIBLE)
    # AT WHAT TIME OF DAY (IN UTC) IS THIS HASHTAG THE MOST ACTIVE?
    # WHAT OTHER HASHTAGS IS THIS HASHTAG OFTEN PAIRED UP WITH?
    # SOME ANALYSIS REGARDING FRIENDS AND FOLLOWERS

    # RETRIEVING DATA FROM THE FILE
    

    # Open the file in read mode
    with open(file_name, 'r') as f:
        tweet_string_list = f.readlines()

    # Convert Tweets from string to dict
    tweet_list = []
    for string in tweet_string_list:
        tweet_list.append(json.loads(string))
    # print(tweet_list[0])

    # ANALYSIS 1: WHAT DEVICES DO THE USERS USE TO POST THESE POSTS

    if flags['2'] == 1:
        for tweet in tweet_list:
            tweet['source'] = (tweet['source'])
        device_counter = get_device_counts(tweet_list)
        pprint(device_counter)

        device_labels = []
        device_counts = []

        for tup in device_counter:
            device_labels.append(remove_html_tags(tup[0]))
            device_counts.append(tup[1])

        print(device_labels, '\n', device_counts)

        fig = go.Figure(data=[go.Pie(labels=device_labels, values=device_counts)])
        fig.show()

    # ANALYSIS 2: WHAT WORDS ARE COMMONLY SEEN IN POSTS WITH THIS HASHTAG?

    if flags['3'] == 1:
        tweet_text = ''
        for tweet in tweet_list:
            tweet_text += tweet['text']

        stopwords = set(STOPWORDS)
        stopwords.add('t')
        stopwords.add('https')
        # These stopwords were set for the posts in tweet_search_1.json which had the hashtag #MUNLEE

        make_word_cloud(tweet_text, stopwords)
    
    # ANALYSIS 3: LANG OF THE USERS (ps This failed miserably since lang = none for every single post :(  )

    # if flags['4']==1:
        # langs = Counter()
        # for tweet in tweet_list:
        # langs[tweet['user']['lang']] += 1
        # pprint(langs[0])
        # lang_name = []
        # lang_count = []

        # for lang in langs:
        #     lang_name.append(lang[0])
        #     lang_count.append(lang[1])

        # print(lang_name, '\n', lang_count)

        # fig = go.Figure(
        #     data=[go.Pie(labels=lang_name, values=lang_count)])
        # fig.show()

    # ANALYSIS 4: LOCATION OF THE TWEETS

    if flags['4'] == 1:
        locations = Counter()
        for tweet in tweet_list:
            if tweet['user']['location'] != '':
                locations[tweet['user']['location']] += 1
        # pprint(locations)
        loc_name = []
        loc_count = []

        for loc in locations.most_common(10):
            loc_name.append(loc[0])
            loc_count.append(loc[1])

        print(loc_name, '\n', loc_count)

        fig = go.Figure(data=[go.Pie(labels=loc_name, values=loc_count)])
        fig.show()
    
    # ANALYSIS 5: LOCATION OF THE USERS (couldn't test this thoroughly because it takes soo looong)
    
    # if flags['5'] == 1:
        # print("This takes a LONG time, better find something to do while you wait. The reason why it takes so long is due to the fact that the user information is not included in the tweet itself but instead has to be queried from twitter, and the rate of queries to twitter is capped, which means you'll have to wait while the cap replenishes and is then used up again repeatedly. I'd recommend coming back in about an hour or changing the number of tweets being analyzed and running it from scratch.")
        # locations = Counter()
        # for tweet in tweet_list:
        #     user = api.get_user(tweet['user']['id'])
        #     if user.location != '':
        #         locations[user.location] += 1
        # # pprint(locations)
        # loc_name = []
        # loc_count = []

        # for loc in locations.most_common(10):
        #     loc_name.append(loc[0])
        #     loc_count.append(loc[1])

        # print(loc_name, '\n', loc_count)

        # fig = go.Figure(data=[go.Pie(labels=loc_name, values=loc_count)])
        # fig.show()

    # ANALYSIS 6: WHICH HASHTAGS IS THE SELECTED HASHTAG COMMONLY PAIRED WITH?

    if flags['5'] == 1:

        hashtags = Counter()
        for tweet in tweet_list:
            for hash in tweet['entities']['hashtags']:
                    hashtags[hash['text']] += 1
        
        hash_count = OrderedDict(hashtags.most_common(10))

        labels = list(hash_count.keys())
        counts = list(hash_count.values())    
        
        fig = go.Figure([go.Bar(x=labels, y=counts)])
        fig.show()

    # ANALYSIS 7: WHAT TIME ARE THESE TWEETS TWEETED?
    
    if flags['6'] == 1:
        hours = Counter()
        for tweet in tweet_list:
            # Use re to find the hour in UTC time and use counter.
            searchObj = re.search(r'([0-9][0-9]):[0-9][0-9]:[0-9][0-9]',tweet['created_at'])
            hours[searchObj.group(1)] += 1
        hours_count = OrderedDict(hours.most_common())

        labels = list(hours_count.keys())
        counts = list(hours_count.values())

        fig = go.Figure([go.Bar(x=labels, y=counts)])
        fig.show()