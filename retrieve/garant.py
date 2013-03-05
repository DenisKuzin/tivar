# -*- coding: utf-8 -*-
u'''
Скачивает данные о производственном календаре Гарант
http://www.garant.ru/doc/busref/spr_proizv_calend/2003/
'''

from requests import get
from os.path import join
from settings import data_dir
from common import check_dir

def download_files():
    current_year = 1998
    while current_year < 2012:
        page = get('http://www.garant.ru/doc/busref/spr_proizv_calend/%s/' % current_year).text
        current_dir = join(data_dir, u'garant')
        check_dir(current_dir)
        current_file = join(current_dir, u'%s.html' % current_year)
        with open(current_file, 'w') as f:
            f.write(page)
        current_year += 1