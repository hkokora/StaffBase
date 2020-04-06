import requests

class Avatar:
    def __init__(self, token=None, debug=False):
        self.token = token
        self.common_headers = {"Authorization": f"Basic {token}"}
        self.debug = debug
        self.avatar_url = ""

    def make_requests(self, data=None, file=None, method=None, headers=None):
        results = ''
        if method == 'POST':
            results = requests.post(url=self.avatar_url, data=data, headers=headers)
        else:
            results = requests.get(url=self.avatar_url, headers=self.common_headers, data=data, files=file)

        if self.debug:
            print(results.reason)
            print(results.status_code)
            pp.pprint(results.json(), indent=2)
            return results.json()
        else:
            return results.json()

