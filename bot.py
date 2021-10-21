import requests
import random
from dataclasses import dataclass
import configparser

config = configparser.ConfigParser()
items = config.read('rules.cfg')

STATISTICS = {'Created users': {},
              'Created posts': {},
              "Created likes": {}}

number_of_users = int(config['VARIABLES']['number_of_users'])
max_posts_per_user = int(config['VARIABLES']['max_posts_per_user'])
max_likes_per_user = int(config['VARIABLES']['max_likes_per_user'])


@dataclass
class Auth:
    username: str
    password: str

    _host = "http://127.0.0.1:8006"

    def _get_user_credentials(self) -> dict:
        return {
            "username": self.username,
            "password": self.password
        }

    def signup(self) -> dict:
        url = self._host + "/api/v1/users/register/"
        try:
            result = requests.post(url=url, data=self._get_user_credentials())
            return result.json()
        except Exception as e:
            print(f'Error while creating new user with username {self.username}. Exception: {e}')
            return {}

    @property
    def get_token(self) -> str:
        url = self._host + "/api/token/"
        result = requests.post(url=url, data=self._get_user_credentials())
        token = result.json().get("access")
        return token

    @property
    def get_headers(self) -> dict:
        return {
                "Authorization": f"Bearer {self.get_token}",
                "Content-type": "application/json",
            }


class API(Auth):
    def create_post(self, user: str) -> dict:
        url = self._host + "/api/v1/posts/"
        data = {
            "title": f"{user}'s post",
            "body": f"{user}'s content"
        }
        try:
            result = requests.post(url=url, headers=self.get_headers, json=data)
            return result.json()
        except Exception as e:
            print(f"Exception while creating post with data: {data}. Exception: {e}")
            return {}

    def like_post(self, post_id: int) -> bool:
        url = self._host + "/api/v1/posts/%s/post-like/" % post_id
        try:
            requests.post(url=url, headers=self.get_headers)
            return True
        except Exception as e:
            print(f"Exception while liking post with id {post_id}. Exception: {e}")
            return False

    def get_posts_ids(self) -> list:
        url = self._host + "/api/v1/posts"
        try:
            result = requests.get(url=url, headers=self.get_headers)
            ids = [post['id'] for post in result.json()]
            return ids
        except Exception as e:
            print(f"Exception while parsing post ids: {e}")
            return []


def create_users(max_users: int) -> dict:
    users_data = {}
    for u in range(1, max_users + 1):
        username = "test" + str(u)
        password = "password123"
        user = Auth(username, password)
        register = user.signup()
        if register:
            users_data[username] = password
    STATISTICS['Created users'] = users_data
    return users_data


def create_posts(users: dict, max_posts: int) -> dict:
    post_data = {}
    for user, password in users.items():
        api = API(user, password)
        user_posts = []
        posts_amount = random.randint(1, max_posts)
        for u in range(1, posts_amount + 1):
            post = api.create_post(user)
            if post:
                user_posts.append({"title": post['title'], "id": post['id']})
        post_data[user] = user_posts
    STATISTICS['Created posts'] = post_data
    return post_data


def like_posts(users: dict, post_ids: list, max_likes: int) -> dict:
    likes = {}

    for user in users.items():
        likes_amount = random.randint(1, max_likes)
        posts_to_like = random.sample(post_ids, likes_amount)
        api = API(user[0], user[1])
        user_likes = []
        for post in posts_to_like:
            like = api.like_post(post)
            if like:
                user_likes.append(post)
        likes[user[0]] = user_likes
    STATISTICS['Created likes'] = likes
    return likes


def main(max_users: int, max_posts: int, max_likes: int) -> dict:
    users_data = create_users(max_users)
    create_posts(users_data, max_posts)
    post_request = API(list(users_data.keys())[0], list(users_data.values())[0])
    post_ids = post_request.get_posts_ids()
    like_posts(users_data, post_ids, max_likes)
    return STATISTICS


if __name__ == '__main__':
    print(main(number_of_users, max_posts_per_user, max_likes_per_user))
