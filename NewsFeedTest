from NewFeed import NewsfeedPosts
import json

token = 'Enter Your Personal Token'
new_post = NewsfeedPosts(token=token, debug=True)
url = 'https://www.smithsonianmag.com/rss/arts-culture/'
json_data = json.dumps(new_post.parse_feed(url, count=302), indent=2)

for data in new_post.parse_feed(url, count=303):
    post_data = json.dumps(data, indent=2)
    new_post.post(post_data)
