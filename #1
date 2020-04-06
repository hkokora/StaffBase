import requests

class AutoImport:
    def __init__(self, csv=None, token=None, mappings=None):
        self.csv = csv
        self.common_header = {"Authorization": f"Basic {token}"}
        self.upload_url = "https://backend.staffbase.com/api/users/import/csv/upload"
        self.update_url = "https://backend.staffbase.com/api/users/import/csv/update"
        self.mappings = mappings

    def make_requests(self, url=None, headers=None, data=None, file=None, debug=False):
        results = requests.post(url=url, headers=headers, data=data, files=file)

        if debug:
            import pprint as pp
            print(results.reason)
            print(results.status_code)
            pp.pprint(results.json())
            return results.json()
        else:
            return results.json()

    def upload_csv(self, debug=False): #dry run TODO
        upload_headers = {}
        upload_headers.update(self.common_header)
        file_header = {'csv': (f'{self.csv}', open(f'{self.csv}', 'rb')),
                        'encoding': (None, 'windows-1252'),
                        'fieldSeparator': ','}

        self.make_requests(url=self.upload_url,headers=upload_headers, file=file_header, debug=debug)

    def update_csv_mappings(self, debug=False):
        update_mappings_headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        update_mappings_headers.update(self.common_header)
        data_header = {'mappings': f'{self.mappings}'}
        self.make_requests(url=self.update_url, headers=update_mappings_headers, data=data_header, debug=debug)

    def final_update(self, debug=False):
        final_update_headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        final_update_headers.update(self.common_header)
        data_header = {'sendMailsPending' : 'false', 'sendMailsNew' : 'true', 'dry' : 'false'}
        self.make_requests(url=self.update_url, headers=final_update_headers, data=data_header, debug=debug)


