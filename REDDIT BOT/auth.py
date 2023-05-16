def authenticate():
    reddit = praw.Reddit(
            client_id='example',
            client_secret='example',
            user_agent='<console:example:1.0>',
            username='example',
            password='example'
        )
