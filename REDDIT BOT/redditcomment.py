import random
import randfacts
import praw
from serpapi import GoogleSearch
import time

reddit = praw.Reddit(
        client_id='x9uNAt3civEeZ5UQfAFPig',
        client_secret='NsWvxUA_7oIae_euucgi9zye_-7wxA',
        user_agent='<console:rolandbbosa:1.0>',
        username='rolandbbosa',
        password='martinlking@2005'
    )

    
sub_reddit_list = [
    'technology',
    'ProgrammerHumor',
    'GetMotivated',
    'badcode',
    'creepy',
    'television',
    'nosleep',
    'history',
    'blog',
    'askscience',
    'worldnews',
    'AskReddit',
    'Music',
    'gaming',
    'Showerthoughts',
    'funny'
]

def comment_on_reddit():   
    # random subreddit
    sub_reddit = random.choice(sub_reddit_list)
    print(f'{sub_reddit} IS THE CHOSEN SUBREDDIT')
    print('NEW.... ')

    subreddit = reddit.subreddit(sub_reddit)

    for submission in subreddit.new(limit=1):
        for comment in submission.comments:
            if hasattr(comment, "body"):
                comment_lower = comment.body.lower()
                if "what" or "who" or "where" or "when" or "?" in comment_lower:
                    recepient = comment.body
                    params = {
                            "api_key": "778f1f126087a8dc715cd307bc5c5a827a1358594568299790e100adc6cc0b60",
                            "engine": "google",
                            "q": recepient,
                            }
                    search = GoogleSearch(params)
                    answer = search.get_dict()

                    answer = results['answer_box']['answer']
                    print('----------(0_0)---------')
                    print(recepient)
                    comment.reply(answer)
                    print(answer)
                    break

    time.sleep(660)
