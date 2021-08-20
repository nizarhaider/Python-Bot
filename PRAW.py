import praw
from praw.models import MoreComments
import requests
import pandas as pd

client_id="PjYzPXwewLRZ0JXbu6DfCw"
client_secret="3YnkM60Z7K6W0bbwCaXPXXvgYEwLUw"

reddit = praw.Reddit(
    user_agent="Comment Extraction (by u/USERNAME)",
    client_id=client_id,
    client_secret=client_secret,
    username="Mr_RoastBot",
    password="Milliondollaridea",
)

a=1
b=1
posts = []
for submission in reddit.subreddit("RoastMe").top("all"):
    for top_level_comment in submission.comments[1:10]:
        if isinstance(top_level_comment, MoreComments):
            continue
        print("comment number:", a)
        a=a+1
        posts.append(top_level_comment.body)
    print("Post Number:", b)
    b=b+1
    if b==10:
        break
# print('Title: {}, ups: {}, downs: {}, score: {}'.format(submission.title, submission.ups, submission.downs, submission.score))


posts = pd.DataFrame(posts, columns=["body"])

indexNames = posts[(posts.body == '[removed]') | (posts.body == '[deleted]')].index
posts.drop(indexNames, inplace=True)
print(posts)



# auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
#
# data = {
#     'grant_type': 'password',
#     'username': 'Mr_RoastBot',
#     'password': 'Milliondollaridea'
# }
# headers = {'Agent': 'RoastBot'}
# res = requests.post('https://www.reddit.com/api/v1/access_token',
#                     auth=auth, data=data, headers=headers)
#
# TOKEN = res.json()['access_token']
#
# headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
#
# requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
