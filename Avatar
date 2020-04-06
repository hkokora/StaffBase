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

token = 'Enter Yours'
filename = 'https://app.staffbase.com/js/c924734a7146466220a765f638131ca6.png'

#file =  open(f'{filename}', 'rb')
print(filename)
header = {
        'Content-Type': 'multipart/form-data',
        "Authorization": f"Basic {token}"

    }
file_header = {'filename': (f'{filename}'),
                        'name': 'avatar'}
data = {
        'Content-Disposition': f"form-data; name=avatar; filename={filename}",
        "Content-Type": "image/png"
}

data_chrome = '$------WebKitFormBoundaryI23A3NUCrQBgyvHK\\r\\nContent-Disposition: form-data; name="avatar"; filename="screenshot.png"\\r\\nContent-Type: image/png\\r\\n\\r\\n\\r\\n------WebKitFormBoundaryI23A3NUCrQBgyvHK--\\r\\n'

files = {"file": f'{filename}'}
url = "https://backend.staffbase.com/api/users/me"

update_image = requests.post(url=url, headers=header, files=file_header, data=None)
print(update_image.json())
