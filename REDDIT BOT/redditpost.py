import randfacts
import praw
import time

reddit = praw.Reddit(
        client_id='x9uNAt3civEeZ5UQfAFPig',
        client_secret='NsWvxUA_7oIae_euucgi9zye_-7wxA',
        user_agent='<console:rolandbbosa:1.0>',
        username='rolandbbosa',
        password='martinlking@2005'
    )

def post_on_reddit():
    fact = randfacts.get_fact()
    fact = f'did you know {fact}'
    fact = fact.lower()

    subr = 'FunFacts' # Choose your subreddi
    subreddit = reddit.subreddit(subr) # Initialize the subreddit to a variable
    title = fact
    selftext = '#facts'
    subreddit.submit(title,selftext)
    print('Posted... >' + fact)
    time.sleep(660)