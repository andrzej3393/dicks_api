import urllib.request
import json


class DicksApi:

    """
    dicks-api (http://dicks-api.herokuapp.com/) client class.
    """

    def __init__(self):
        self.url = "http://dicks-api.herokuapp.com/dicks/"

    def get(self, amount=1, size=None):
        """
        Get dicks from API.

        Keyword arguments:
        amount -- quantity of dicks (default 1)
        size -- dicks size, there are 4 possible options:
            'asian'
            'european'
            'black'
            None

        Returns:
        list of dicks
        """
        if not isinstance(amount, int):
            raise TypeError("amount should be integer")

        if size not in ['asian', 'european', 'black', None]:
            raise ValueError("incorrect size")

        url = self.url + str(amount)

        if size is not None:
            url = url + "?size=" + size

        response = urllib.request.urlopen(url).read().decode('utf-8')
        result = json.loads(response)
        dicks = result['dicks']
        return dicks
