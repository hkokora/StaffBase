import requests
import pprint as pp
import json
import feedparser
import ssl

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


# class Auth:
#     def __init__(self, token=None):
#         self.token = token

class NewsfeedPosts:
    def __init__(self, token=None, debug=False):
        self.token = token
        self.common_headers = {"Authorization": f"Basic {token}"}
        self.debug = debug
        self.posts_url = "https://backend.staffbase.com/api/channels/5e84e21f251ebf0c01c3949b/posts"

    def make_requests(self, data=None, file=None, method=None, headers=None):
        results = ''
        if method == 'POST':
            results = requests.post(url=self.posts_url, data=data, headers=headers)
        else:
            results = requests.get(url=self.posts_url, headers=self.common_headers, data=data, files=file)

        if self.debug:
            print(results.reason)
            print(results.status_code)
            pp.pprint(results.json(), indent=2)
            return results.json()
        else:
            return results.json()

    def post(self, data=None):
        headers = {'Content-type': 'application/json'}
        headers.update(self.common_headers)
        response = self.make_requests(data=data, method='POST', headers=headers)
        return response

    def parse_feed(self, url=None, count=None):
        data = []
        feeds = feedparser.parse(url)
        for feed in feeds.entries:
            data.append({"externalID": f'{count}',
                         "contents": {
                             "en_US": {
                                 "content": requests.get(feed.link).text,
                                 "image": feed.links[1].href,
                                 "teaser": feed.summary,
                                 "title": feed.title
                             }
                         }
                         })
            count += 1
        return data
