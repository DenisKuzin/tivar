#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import check_dir
from settings import data_dir
from retrieve import forts
from retrieve import garant

if __name__ == '__main__':
    check_dir(data_dir)
    garant.download_files()
    forts.download_files()