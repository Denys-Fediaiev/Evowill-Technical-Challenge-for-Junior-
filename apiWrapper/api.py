import requests


class Api(object):
    def __init__(self, act_type, participants, min_price, max_price, min_accessibility, max_accessibility):
        self.act_type = act_type
        self.participants = participants,
        self.min_price = min_price,
        self.max_price = max_price,
        self.min_accessibility = min_accessibility,
        self.max_accessibility = max_accessibility,

    def random_activity(self):
        api_url = 'https://www.boredapi.com/api/activity'
        params = {
            'type': self.act_type,
            'participants': self.participants,
            'minprice': self.min_price,
            'maxprice': self.max_price,
            'minaccessibility': self.min_accessibility,
            'maxaccessibility': self.max_accessibility,
        }
        response = requests.get(api_url, params=params)
        return response.json()
