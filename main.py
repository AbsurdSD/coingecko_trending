import requests
import json
from tabulate import tabulate
from prettytable import PrettyTable

url = 'https://api.coingecko.com/api/v3/search/trending'
response  = requests.get(url).text
json_data = json.loads(response)

top_coins = json_data['coins']
lst = []
#append coin in [] list of lists
for key in top_coins:
    coin = key['item']['name']
    lst.append(coin)

#tabulate view method uses a tuple of list of lists
""" tup = tuple(lst)
tabel = tabulate(tup, headers=['Trending coins'], tablefmt="tsv")
"""

pretty = PrettyTable()

#prettytable using rows 'P.S: takes rows as a list of lists'
""" pretty.field_names = ["TrendingCoins",]
pretty.add_rows(lst) """

#prettytable using column by column addition
pretty.add_column('TrendingCoins',lst)
print(pretty)


