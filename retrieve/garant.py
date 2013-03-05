# -*- coding: utf-8 -*-
u'''
Скачивает данные о производственном календаре Гарант
http://www.garant.ru/doc/busref/spr_proizv_calend/2003/
'''

from requests import get
from os.path import join, exists
from os import rename
from settings import data_dir
from common import check_dir

def download_files():
    current_year = 1998
    while current_year < 2013:
        current_dir = join(data_dir, u'garant')
        check_dir(current_dir)
        current_file = join(current_dir, u'%s.html' % current_year)
        if not exists(current_file):
            temp_file = current_file + '.tmp'
            page = get('http://www.garant.ru/doc/busref/spr_proizv_calend/%s/' % current_year).text
            with open(temp_file, 'w') as f:
                f.write(page.encode('utf-8'))
            rename(temp_file, current_file)
        current_year += 1