import praw
import pprint
import pandas as pd
from stopwatch import Stopwatch


class Scraper:
    def __init__(self, num_post, num_comments):
        self.posts = []
        self.get_reddit_posts(num_post, num_comments)
        self.df = self.create_df()

    def to_csv(self):
        self.df.to_csv('posts_data.csv')

    @staticmethod
    def get_reddit():
        return praw.Reddit(
            client_id="hn4ACib40dq2_537QDanyg",
            client_secret="zXHU8m22n4mehB0FhtZb3swJUiJvoA",
            user_agent="aita_scraper"
        )

    def create_df(self):
        post_data = []
        for post in self.posts:
            post_data.append(post.info)
        return pd.DataFrame(post_data)

    def get_reddit_posts(self, num_post, num_comments):
        sw = Stopwatch(3)
        sw.start()
        reddit = self.get_reddit()
        aita = reddit.subreddit("AmItheAsshole")
        for reddit_post in aita.hot(limit=num_post):
            if reddit_post.stickied:
                continue
            comments = []
            if num_comments >= 32:
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
            new_post = Post(reddit_post.title, reddit_post.selftext, comments)
            self.posts.append(new_post)
        sw.stop()
        print(sw.duration)
    def print_posts(self):
        for post in self.posts:
            post.print_post()

    def print_ratings(self):
        for post in self.posts:
            post.print_rates()


class Post:
    def __init__(self, title, content, coms):
        self.info = {'title': title,
                     'content': content,
                     'category': '',
                     'NTA': 0,
                     'YTA': 0,
                     'NAH': 0,
                     'ESH': 0}
        self.comments = coms
        self.check_ratings()

    def check_ratings(self):
        ratings = ['NTA', 'YTA', 'NAH', 'ESH']
        for comment in self.comments:
            for rate in ratings:
                if rate in comment:
                    self.info[rate] += 1
        # get category
        self.info['category'] = self.get_category(ratings)

    def get_category(self, ratings):
        return max({key: self.info[key] for key in ratings}, key=self.info.get)

    def print_rates(self):
        pp = pprint.PrettyPrinter(indent=2, width=100)
        for rate, count in self.ratings.items():
            pp.pprint(rate + ': ' + str(count))

    def print_post(self):
        ppa = pprint.PrettyPrinter(indent=2, width=100)
        print('Title: ', end=' ')
        ppa.pprint(self.info['title'])
        print('Content: ', end=' ')
        ppa.pprint(self.info['content'])
        print("Comments: ")
        pp = pprint.PrettyPrinter(indent=6, width=100)
        for comment in self.comments:
            pp.pprint(comment)
            print()
        print('END POST\n')


def main():
    scraper = Scraper(3, 31)
    # scraper.print_posts()
    # scraper.print_ratings()
    scraper.to_csv()


if __name__ == '__main__':
    main()
