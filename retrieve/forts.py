# -*- coding: utf-8 -*-
u'''
Скачиваем данные о сделках FORTS
http://ftp.rts.ru/pub/info/stats/history/F/2003/FT030104.ZIP
'''

from datetime import datetime, date, time, timedelta
from process.dates import work_dates_between

forts_tradesfile_publish_time = time(19)
u'''
Время суток в которое на серверах выкладываются файлы с совершенными сделками FORTS
19:00
'''

def download_files():
    start_date = date(2003, 01, 04)
    if datetime.now().time() >= forts_tradesfile_publish_time:
        stop_date = date.today()
    else:
        stop_date = date.today() - timedelta(1)
    for current_date in work_dates_between(start_date, stop_date):
        print current_date.strftime(u'http://ftp.rts.ru/pub/info/stats/history/F/%Y/FT%y%m%d.ZIP')