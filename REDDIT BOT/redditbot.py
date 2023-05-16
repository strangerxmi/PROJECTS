import random
import redditpost
import redditcomment


decide = [
    'post',
    'comment'
]

while True:
    decided = random.choice(decide)

    if decided == 'post':
        print('I AM POSTING NOW')
        redditpost.post_on_reddit()
    elif decided == 'comment':
        print('I AM COMMENTING NOW')
        redditcomment.comment_on_reddit()