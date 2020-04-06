import requests
import pprint as pp



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
