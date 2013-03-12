# -*- coding: utf-8 -*-
u'''
Скачиваем данные о сделках FORTS
http://ftp.rts.ru/pub/info/stats/history/F/2003/FT030104.ZIP
'''

from datetime import datetime, date, time, timedelta
from process.dates import work_dates_between
from common import download_file
from requests import get
from lxml.html import fromstring

forts_tradesfile_publish_time = time(19)
u'''
Время суток в которое на серверах выкладываются файлы с совершенными сделками FORTS
19:00
'''

def parse_links():
    u'''
    Парсит странички http://ftp.rts.ru/pub/info/stats/history/F/YYYY/
    Находит ссылки на файлы и качает их
    '''
    for current_year in xrange(2003, date.today().year + 1):
        page_link = u'http://ftp.rts.ru/pub/info/stats/history/F/%s/' % current_year
        html = fromstring(get(page_link).text)
        html.make_links_absolute(page_link)
        for current_link in html.xpath('/html/body/pre/a[@href!="http://ftp.rts.ru/pub/info/stats/history/F/"]/@href'):
            if current_link.split('/')[-1].lower().startswith('ft'):
                download_file('ft', current_link)

def generate_links():
    u'''
    Генерирует прямые ссылки на файлы по календарю
    '''
    start_date = date(2003, 01, 04)
    if datetime.now().time() >= forts_tradesfile_publish_time:
        stop_date = date.today()
    else:
        stop_date = date.today() - timedelta(1)
    for current_date in work_dates_between(start_date, stop_date):
        download_file('ft', current_date.strftime(u'http://ftp.rts.ru/pub/info/stats/history/F/%Y/FT%y%m%d.ZIP'))