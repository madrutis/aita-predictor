import praw
import pprint
from praw.models import MoreComments


class Post:
    def __init__(self, title, content, coms):
        self.title = title
        self.content = content
        self.comments = coms

    def print_post(self):
        ppa = pprint.PrettyPrinter(indent=2, width=100)
        print('Title: ', end=' ')
        ppa.pprint(self.title)
        print('Content: ', end=' ')
        ppa.pprint(self.content)
        print("Comments: ")
        pp = pprint.PrettyPrinter(indent=6, width=100)
        for comment in self.comments:
            pp.pprint(comment)
            print()
        print('END POST\n')


posts = []
num_posts = 2
comments_per_post = 5


def get_reddit():
    return praw.Reddit(
        client_id="hn4ACib40dq2_537QDanyg",
        client_secret="zXHU8m22n4mehB0FhtZb3swJUiJvoA",
        user_agent="aita_scraper"
    )


def get_reddit_posts(num_post, num_comments):
    reddit = get_reddit()
    aita = reddit.subreddit("AmItheAsshole")
    for reddit_post in aita.hot(limit=num_post):
        if reddit_post.stickied:
            continue
        comments = []
        reddit_post.comments.replace_more(limit=num_comments)
        i = 0
        for curr_comment in reddit_post.comments:
            if i == num_comments:
                break
            elif curr_comment.stickied:
                continue
            else:
                comments.append(curr_comment.body)
                i += 1
        posts.append(Post(reddit_post.title, reddit_post.selftext, comments))


def print_posts():
    for post in posts:
        post.print_post()


def main():
    get_reddit_posts(num_posts, comments_per_post)
    print_posts()


if __name__ == '__main__':
    main()
