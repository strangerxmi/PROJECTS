import redditpost
import redditcomment

decide = [
    'post',
    'comment'
]

decided = random.choice(sub_reddit_list)

if decided == 'post':
    redditpost.post_on_reddit()
elif decided == 'comment':
    redditcomment.comment_on_reddit()