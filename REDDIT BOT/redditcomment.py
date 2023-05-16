import random
import randfacts
import praw
from serpapi import GoogleSearch
import time

reddit = praw.Reddit(
        client_id='example',
        client_secret='example',
        user_agent='<console:example:1.0>',
        username='example',
        password='example'
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
                            "api_key": "example",
                            "engine": "google",
                            "q": recepient,
                            }
                    search = GoogleSearch(params)
                    answer = search.get_dict()
                    answer = answer['answer_box']['answer']
                    print('----------(0_0)---------')
                    print(f'COMMENT: {recepient}')
                    print('')
                    print(f'ANSWER: {answer}')
                    comment.reply(answer)
                    break

    time.sleep(660)
