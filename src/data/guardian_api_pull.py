"""
Accesses the Guardian API and retrieves the article data.

I have made some very minor modifications, but full credit for this
script belongs to dannguyen:
https://gist.github.com/dannguyen/c9cb220093ee4c12b840

""""

import json
import requests
from os import makedirs
from os.path import join, exists
from datetime import date, timedelta
from pathlib import Path

def set_startdate(year, month=1, day=1):
    return date(year, month, day)

def set_enddate(year, month=12, day=31):
    return date(year, month, day)

year = 2020
start_date = set_startdate(year, 6, 1)
end_date = set_enddate(year, 6, 30)

ARTICLES_DIR = Path.cwd().parent.parent.joinpath('data', 'raw', str(year))

makedirs(ARTICLES_DIR, exist_ok=True)
# Sample URL
#
# http://content.guardianapis.com/search?from-date=2016-01-02&
# to-date=2016-01-02&order-by=newest&show-fields=all&page-size=200
# &api-key=your-api-key-goes-here

MY_API_KEY = open("creds_guardian.txt").read().strip()
API_ENDPOINT = 'http://content.guardianapis.com/search'
my_params = {
    'from-date': "2016-01-01",
    'to-date': "2016-12-31",
    'order-by': "newest",
    'show-fields': 'all',
    'page-size': 200,
    'api-key': MY_API_KEY
}


# day iteration from here:
# http://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates

dayrange = range((end_date - start_date).days + 1)
for daycount in dayrange:
    dt = start_date + timedelta(days=daycount)
    datestr = dt.strftime('%Y-%m-%d')
    fname = join(ARTICLES_DIR, datestr + '.json')
    if not exists(fname):
        # then let's download it
        print("Downloading", datestr)
        all_results = []
        my_params['from-date'] = datestr
        my_params['to-date'] = datestr
        current_page = 1
        total_pages = 1
        while current_page <= total_pages:
            print("...page", current_page)
            my_params['page'] = current_page
            resp = requests.get(API_ENDPOINT, my_params)
            data = resp.json()
            all_results.extend(data['response']['results'])
            # if there is more than one page
            current_page += 1
            total_pages = data['response']['pages']

        with open(fname, 'w') as f:
            print("Writing to", fname)

            # re-serialize it for pretty indentation
            f.write(json.dumps(all_results, indent=2))
