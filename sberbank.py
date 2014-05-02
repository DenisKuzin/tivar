# -*- coding: utf-8 -*-
'''
Source module for sberbank-am.ru
'''

from requests import get
from datetime import datetime
from re import findall

source_name = 'sberbank'

def get_tickers():
    '''
    Get ticker list from sberbank-am.ru
    >>> get_tickers()[1]
    {'launch': datetime.datetime(2006, 10, 11, 0, 0), 'id': 13, 'name': u'\u041c\u0435\u0442\u0430\u043b\u043b\u0443\u0440\u0433\u0438\u044f'}
    '''
    raw_html = get('http://sberbank-am.ru/rus/statistics/table.wbp').text
    tickers = []
    for ticker in findall(r'fundMap\[\'(\d+)\'\][^\};]+fundName:\'([^\']+)\'[^\};]+lunchDate:\'(\d+/\d+/\d+)\',[^\};]+\};', raw_html):
        tickers.append({'id': int(ticker[0]), 'name': ticker[1], 'launch': datetime.strptime(ticker[2], '%Y/%m/%d')})
    return tickers

def get_trades(ticker, start, stop):
    '''
    Get trades from sberbank-am.ru
    NAV - Net Asset Value

    >>> get_trades(1, datetime(2014, 4, 28), datetime(2014, 4, 29))
    [{'date': datetime.datetime(2014, 4, 29, 0, 0), 'price': 23526.43, 'NAV': 7331141492.11}, {'date': datetime.datetime(2014, 4, 28, 0, 0), 'price': 23550.45, 'NAV': 7279685561.42}]
    '''
    csv = get('http://sberbank-am.ru/visible/chart/getCsv?fund=%s&dateFrom=%s&monthFrom=%s&yearFrom=%s&dateTo=%s&monthTo=%s&yearTo=%s' % (
        ticker, start.day, start.month, start.year, stop.day, stop.month, stop.year))
    trades = []
    for line in csv.text.split('\n')[3:]:
        splited_line = line.split(';')
        if len(splited_line) == 3:
            trades.append({'date': datetime.strptime(splited_line[0], '%d-%m-%y'), 'price': float(splited_line[1].replace(',', '.')), 'NAV': float(splited_line[2])})
    return trades

if __name__ == "__main__":
    import doctest
    doctest.testmod()