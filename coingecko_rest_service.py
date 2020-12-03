########################################################################################################################
# Project : Tanuki tavern
# Name : simple dash app to see some numbers on cryptos
# Description : Is used to create the web app with dash components
# API doc : https://www.coingecko.com/api/documentations/v3#/
########################################################################################################################
import requests
import pandas as pd


def ping_coingecko():
    return requests.get("https://api.coingecko.com/api/v3/ping").json()


def get_coins_list():
    return requests.get("https://api.coingecko.com/api/v3/coins/list").json()


def get_coins_market_chart(coin_id, vs_currency, days, interval):
    query = "https://api.coingecko.com/api/v3/coins/" + coin_id + "/market_chart?vs_currency=" + vs_currency + \
            "&days=" + days + "&interval=" + interval
    return requests.get(query).json()

