import auth
import praw
import randfacts
import time


auth.authenticate()

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