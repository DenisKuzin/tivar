# -*- coding: utf-8 -*-
'''
Source module for sberbank-am.ru
'''

from requests import get
from io import StringIO
from csv import reader
from datetime import datetime
from re import findall

def get_tickers():
    '''
    Get ticker list from sberbank-am.ru
    '''
    raw_html = get('http://sberbank-am.ru/rus/statistics/table.wbp').text
    tickers = {}
    for ticker in findall(r'fundMap\[\'(\d+)\'\][^\};]+fundName:\'([^\']+)\'[^\};]+lunchDate:\'(\d+/\d+/\d+)\',[^\};]+\};', raw_html):
        tickers[int(ticker[0])] = {u'name': unicode(ticker[1]), u'remote_start': datetime.strptime(ticker[2], '%Y/%m/%d')}
    return tickers

def get_trades(ticker, start, stop):
    '''
    Get trades from sberbank-am.ru
    NAV - Net Asset Value
    '''
    raw_csv = get('http://sberbank-am.ru/visible/chart/getCsv?fund=%s&dateFrom=%s&monthFrom=%s&yearFrom=%s&dateTo=%s&monthTo=%s&yearTo=%s' % (
        ticker['fund'], start.day, start.month, start.year, stop.day, stop.month, stop.year))
    csv_reader = reader(StringIO(raw_csv), delimiter=';')
    trades = []
    for id, row in enumerate(csv_reader):
        if id in (0, 1, 2):
            trades.append({'date': datetime.strptime(row[0], '%d-%m-%Y'), 'price': float(row[1].replace(',', '.')), 'NAV': float(row[2])})
    return trades

def get(ticker, start=None, stop=None):
    return