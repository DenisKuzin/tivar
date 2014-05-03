# -*- coding: utf-8 -*-
'''
Cache module
'''

from remote.sberbank import source_name, get_tickers as remote_tickers, get_trades as remote_trades
from local.btrfsdb import get_dataset, set_dataset
from datetime import datetime

def get_ticker(update=False, **kwargs):
    '''
    Get ticker from storage or source, and save changes in storage
    Return first ticker with this search parameters
    Use update=True, to force download ticker list from source
    >>> get_ticker(id=13)
    {'launch': datetime.datetime(2006, 10, 11, 0, 0), 'id': 13, 'name': u'\u041c\u0435\u0442\u0430\u043b\u043b\u0443\u0440\u0433\u0438\u044f'}
    '''
    dataset_name = '%s:%s' % (source_name, 'tickers')
    dataset = get_dataset(dataset_name)
    if not dataset or update:
        dataset = remote_tickers()
        set_dataset(dataset_name, dataset)
    if len(kwargs):
        for ticker in dataset:
            hit = True
            for key, value in kwargs.items():
                if ticker[key] != value:
                    hit = False
            if hit:
                return ticker

def get_tickers(update=False, **kwargs):
    '''
    Get ticker list from storage or source, and save changes in storage
    Return list of tickers which corresponds search parameters
    Use update=True, to force download ticker list from source
    >>> get_tickers()[1]
    {'launch': datetime.datetime(2006, 10, 11, 0, 0), 'id': 13, 'name': u'\u041c\u0435\u0442\u0430\u043b\u043b\u0443\u0440\u0433\u0438\u044f'}
    '''
    dataset_name = '%s:%s' % (source_name, 'tickers')
    dataset = get_dataset(dataset_name)
    if not dataset or update:
        dataset = remote_tickers()
        set_dataset(dataset_name, dataset)
    tickers = []
    for ticker in dataset:
        hit = True
        for key, value in kwargs.items():
            if ticker[key] != value:
                hit = False
        if hit:
            tickers.append(ticker)
    return tickers

def get_trades(ticker, start=None, stop=None, **kwargs):
    '''
    Get trades from storage or source, and save changes in storage
    ticker - return trades for ticker
    >>> get_trades(get_ticker(id=1), datetime(2014, 4, 28), datetime(2014, 4, 29))
    [{'price': 23550.45, 'NAV': 7279685561.42, 'time': datetime.datetime(2014, 4, 28, 0, 0)}, {'price': 23526.43, 'NAV': 7331141492.11, 'time': datetime.datetime(2014, 4, 29, 0, 0)}]
    '''
    dataset_name = '%s:%s' % (source_name, ticker['id'])
    dataset = get_dataset(dataset_name)
    dirty = False
    if not dataset:
        dataset = {}
        dirty = True
    if 'start' not in dataset or 'stop' not in dataset:
        if start and start > ticker['launch']:
            download_start = start
        else:
            download_start = ticker['launch']
        if stop and stop <= datetime.now():
            download_stop = stop
        else:
            download_stop = datetime.now()
        dataset['trade'] = remote_trades(ticker['id'], download_start, download_stop)
        if len(dataset['trade']) > 0:
            dataset['start'] = dataset['trade'][0]['time']
            dataset['stop'] = dataset['trade'][-1]['time']
        else:
            dataset['start'] = download_start
            dataset['stop'] = download_stop
        dirty = True
    download_before = False
    if start:
        if start < dataset['start']:
            if start < ticker['launch']:
                download_start = ticker['launch']
            else:
                download_start = start
            download_stop = dataset['start']
            download_before = True
    else:
        if ticker['launch'] < dataset['start']:
            download_start = ticker['launch']
            download_stop = ticker['start']
            download_before = True
    if download_before:
        dataset['trade'].insert(0, remote_trades(ticker['id'], download_start, download_stop)[0:-1])
        dirty = True
    download_after = False
    if stop:
        if stop > dataset['stop']:
            if stop > datetime.now():
                download_stop = datetime.now()
            else:
                download_stop = stop
            download_start = dataset['stop']
            download_after = True
    else:
        if datetime.now() > dataset['stop']:
            download_start = dataset['stop']
            download_stop = datetime.now()
            download_after = True
    if download_after:
        dataset['trade'].append(remote_trades(ticker['id'], download_start, download_stop)[1:])
        dirty = True
    if dirty:
        set_dataset(dataset_name, dataset)
    trades = []
    for trade in dataset['trade']:
        hit = True
        for key, value in kwargs.items():
            if start and trade['time'] < start:
                hit = False
            if stop and trade['time'] > stop:
                hit = False
            if trade[key] != value:
                hit = False
        if hit:
            trades.append(trade)
    return trades


if __name__ == "__main__":
    import doctest
    doctest.testmod()