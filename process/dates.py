# -*- coding: utf-8 -*-
u'''
Обработка связанная с датой и временем
'''

from datetime import date, timedelta

year_start = 2001
u'''
Данные о рабочих, праздничных днях занесены начиная с этого года
'''

year_stop = 2014
u'''
Данные о рабочих, праздничных днях занесены до этого года(исключая его)
'''

def tuple_to_date(tuples):
    u'''
    Преобразует ((2003, 6, 13), (2003, 5, 14)) в [datetime.date(2003, 6, 13), datetime.date(2003, 5, 14)]
    Не используется Generator Expression т.к. требуется быстро эти данные переварить и сохранить в памяти результат
    '''
    dates = map(lambda current_date: date(*current_date), tuples)
    return dates

days_off = tuple_to_date((
    (2001, 1, 1),
    (2001, 1, 2),
    (2001, 1, 8),
    (2001, 3, 8),
    (2001, 5, 1),
    (2001, 5, 2),
    (2001, 5, 9),
    (2001, 6, 12),
    (2001, 11, 7),
    (2001, 12, 12),
    (2002, 1, 1),
    (2002, 1, 2),
    (2002, 1, 7),
    (2002, 2, 25),
    (2002, 3, 8),
    (2002, 5, 1),
    (2002, 5, 2),
    (2002, 5, 3),
    (2002, 5, 9),
    (2002, 5, 10),
    (2002, 6, 12),
    (2002, 11, 7),
    (2002, 11, 8),
    (2002, 12, 12),
    (2002, 12, 13),
    (2003, 1, 1),
    (2003, 1, 2),
    (2003, 1, 3),
    (2003, 1, 6),
    (2003, 1, 7),
    (2003, 2, 24),
    (2003, 3, 10),
    (2003, 5, 1),
    (2003, 5, 2),
    (2003, 5, 9),
    (2003, 6, 12),
    (2003, 6, 13),
    (2003, 11, 7),
    (2003, 12, 12),
    (2004, 1, 1),
    (2004, 1, 2),
    (2004, 1, 7),
    (2004, 2, 23),
    (2004, 3, 8),
    (2004, 5, 3),
    (2004, 5, 4),
    (2004, 5, 10),
    (2004, 6, 14),
    (2004, 11, 8),
    (2004, 12, 13),
    (2005, 1, 3),
    (2005, 1, 4),
    (2005, 1, 5),
    (2005, 1, 6),
    (2005, 1, 7),
    (2005, 1, 10),
    (2005, 2, 23),
    (2005, 3, 7),
    (2005, 3, 8),
    (2005, 5, 2),
    (2005, 5, 9),
    (2005, 5, 10),
    (2005, 6, 13),
    (2005, 11, 4),
    (2006, 1, 2),
    (2006, 1, 3),
    (2006, 1, 4),
    (2006, 1, 5),
    (2006, 1, 6),
    (2006, 1, 9),
    (2006, 2, 23),
    (2006, 2, 24),
    (2006, 3, 8),
    (2006, 5, 1),
    (2006, 5, 8),
    (2006, 5, 9),
    (2006, 6, 12),
    (2006, 11, 6),
    (2007, 1, 1),
    (2007, 1, 2),
    (2007, 1, 3),
    (2007, 1, 4),
    (2007, 1, 5),
    (2007, 1, 8),
    (2007, 2, 23),
    (2007, 3, 8),
    (2007, 4, 30),
    (2007, 5, 1),
    (2007, 5, 9),
    (2007, 6, 11),
    (2007, 6, 12),
    (2007, 11, 5),
    (2007, 12, 31),
    (2008, 1, 1),
    (2008, 1, 2),
    (2008, 1, 3),
    (2008, 1, 4),
    (2008, 1, 7),
    (2008, 1, 8),
    (2008, 2, 25),
    (2008, 3, 10),
    (2008, 5, 1),
    (2008, 5, 2),
    (2008, 5, 9),
    (2008, 6, 12),
    (2008, 6, 13),
    (2008, 11, 3),
    (2008, 11, 4),
    (2009, 1, 1),
    (2009, 1, 2),
    (2009, 1, 5),
    (2009, 1, 6),
    (2009, 1, 7),
    (2009, 1, 8),
    (2009, 1, 9),
    (2009, 2, 23),
    (2009, 3, 9),
    (2009, 5, 1),
    (2009, 5, 11),
    (2009, 6, 12),
    (2009, 11, 4),
    (2010, 1, 1),
    (2010, 1, 4),
    (2010, 1, 5),
    (2010, 1, 6),
    (2010, 1, 7),
    (2010, 1, 8),
    (2010, 2, 22),
    (2010, 2, 23),
    (2010, 3, 8),
    (2010, 5, 3),
    (2010, 5, 10),
    (2010, 6, 14),
    (2010, 11, 4),
    (2010, 11, 5),
    (2011, 1, 3),
    (2011, 1, 4),
    (2011, 1, 5),
    (2011, 1, 6),
    (2011, 1, 7),
    (2011, 1, 10),
    (2011, 2, 23),
    (2011, 3, 7),
    (2011, 3, 8),
    (2011, 5, 2),
    (2011, 5, 9),
    (2011, 6, 13),
    (2011, 11, 4),
    (2012, 1, 2),
    (2012, 1, 3),
    (2012, 1, 4),
    (2012, 1, 5),
    (2012, 1, 6),
    (2012, 1, 9),
    (2012, 2, 23),
    (2012, 3, 8),
    (2012, 3, 9),
    (2012, 4, 30),
    (2012, 5, 1),
    (2012, 5, 7),
    (2012, 5, 8),
    (2012, 5, 9),
    (2012, 6, 11),
    (2012, 6, 12),
    (2012, 11, 5),
    (2012, 12, 31),
    (2013, 1, 1),
    (2013, 1, 2),
    (2013, 1, 3),
    (2013, 1, 4),
    (2013, 1, 7),
    (2013, 1, 8),
    (2013, 3, 8),
    (2013, 5, 1),
    (2013, 5, 2),
    (2013, 5, 3),
    (2013, 5, 9),
    (2013, 5, 10),
    (2013, 6, 12),
    (2013, 11, 4)
))
u'''
Нерабочие дни: праздники и т.п.
'''

work_days = tuple_to_date((
    (2002, 4, 27),
    (2002, 5, 18),
    (2002, 11, 10),
    (2002, 12, 15),
    (2003, 1, 4),
    (2003, 1, 5),
    (2003, 6, 21),
    (2005, 3, 5),
    (2005, 5, 14),
    (2006, 2, 26),
    (2006, 5, 6),
    (2007, 4, 28),
    (2007, 6, 9),
    (2007, 12, 29),
    (2008, 5, 4),
    (2008, 6, 7),
    (2008, 11, 1),
    (2009, 1, 11),
    (2010, 2, 27),
    (2010, 11, 13),
    (2011, 3, 5),
    (2012, 3, 11),
    (2012, 4, 28),
    (2012, 5, 5),
    (2012, 5, 12),
    (2012, 6, 9),
    (2012, 12, 29)
))
u'''
Рабочие дни: перенесенные выходные дни и т.п.
'''

short_days = tuple_to_date((
    (2001, 3, 7),
    (2001, 4, 30),
    (2001, 5, 8),
    (2001, 6, 11),
    (2001, 11, 6),
    (2001, 12, 11),
    (2001, 12, 31),
    (2002, 2, 22),
    (2002, 3, 7),
    (2002, 4, 30),
    (2002, 5, 8),
    (2002, 6, 11),
    (2002, 11, 6),
    (2002, 12, 11),
    (2002, 12, 31),
    (2003, 1, 5),
    (2003, 3, 7),
    (2003, 4, 30),
    (2003, 5, 8),
    (2003, 6, 11),
    (2003, 11, 6),
    (2003, 12, 11),
    (2003, 12, 31),
    (2004, 1, 6),
    (2004, 4, 30),
    (2004, 6, 11),
    (2004, 12, 31),
    (2005, 2, 22),
    (2005, 3, 5),
    (2005, 11, 3),
    (2006, 2, 22),
    (2006, 3, 7),
    (2006, 5, 6),
    (2006, 11, 3),
    (2007, 2, 22),
    (2007, 3, 7),
    (2007, 4, 28),
    (2007, 5, 8),
    (2007, 6, 9),
    (2007, 12, 29),
    (2008, 2, 22),
    (2008, 3, 7),
    (2008, 4, 30),
    (2008, 5, 8),
    (2008, 6, 11),
    (2008, 11, 1),
    (2008, 12, 31),
    (2009, 4, 30),
    (2009, 5, 8),
    (2009, 6, 11),
    (2009, 11, 3),
    (2009, 12, 31),
    (2010, 2, 27),
    (2010, 4, 30),
    (2010, 6, 11),
    (2010, 11, 3),
    (2010, 12, 31),
    (2011, 2, 22),
    (2011, 3, 5),
    (2011, 11, 3),
    (2012, 2, 22),
    (2012, 3, 7),
    (2012, 4, 28),
    (2012, 5, 12),
    (2012, 6, 9),
    (2012, 12, 29),
    (2013, 2, 22),
    (2013, 3, 7),
    (2013, 4, 30),
    (2013, 5, 8),
    (2013, 6, 11),
    (2013, 12, 31)
))
u'''
Сокращенные рабочие дни
'''

days_count = {
    2001: {
        'work_days': 251,
        'short_days': 7,
        'days_off': 114
    },
    2002: {
        'work_days': 250,
        'short_days': 8,
        'days_off': 115
    },
    2003: {
        'work_days': 250,
        'short_days': 8,
        'days_off': 115
    },
    2004: {
        'work_days': 251,
        'short_days': 4,
        'days_off': 115
    },
    2005: {
        'work_days': 248,
        'short_days': 3,
        'days_off': 117
    },
    2006: {
        'work_days': 248,
        'short_days': 4,
        'days_off': 117
    },
    2007: {
        'work_days': 249,
        'short_days': 6,
        'days_off': 116
    },
    2008: {
        'work_days': 250,
        'short_days': 7,
        'days_off': 116
    },
    2009: {
        'work_days': 249,
        'short_days': 5,
        'days_off': 116
    },
    2010: {
        'work_days': 249,
        'short_days': 5,
        'days_off': 116
    },
    2011: {
        'work_days': 248,
        'short_days': 3,
        'days_off': 117
    },
    2012: {
        'work_days': 249,
        'short_days': 6,
        'days_off': 117
    },
    2013: {
        'work_days': 247,
        'short_days': 6,
        'days_off': 118
    },
}

def check_dates_lists():
    u'''
    Ищет ошибки в словарях дат
    '''
    for current_date in days_off:
        if current_date in work_days:
            print 'Error days_off %s' % current_date
    for current_date in work_days:
        if current_date in days_off:
            print 'Error work_days %s' % current_date
    for current_date in short_days:
        if current_date in days_off:
            print 'Error short days %s' % current_date
    for current_year in xrange(year_start, year_stop):
        if current_year not in days_count:
            print 'Year %s not checked by days_count' % current_year
            continue
        days_off_count = 0
        work_days_count = 0
        short_days_count = 0
        for days in xrange((date(current_year + 1, 1, 1) - date(current_year, 1, 1)).days):
            current_date = date(current_year, 1, 1) + timedelta(days)
            if current_date.weekday() in (5, 6):
                if current_date in days_off:
                    print 'Error in days_off: %s sat or sun in days_off' % current_date
                if current_date in work_days:
                    work_days_count += 1
                else:
                    days_off_count += 1
            if current_date.weekday() not in (5, 6):
                if current_date in work_days:
                    print 'Error in days_off: %s this day already work' % current_date
                if current_date in days_off:
                    days_off_count += 1
                else:
                    work_days_count += 1
            if current_date in short_days:
                if current_date in days_off:
                    print 'Error in short_days: %s in days_off' % current_date
                else:
                    short_days_count += 1
        if days_off_count != days_count[current_year]['days_off']:
            print 'Error in %s: days_off' % current_year
        if work_days_count != days_count[current_year]['work_days']:
            print 'Error in %s: work_days' % current_year
        if short_days_count != days_count[current_year]['short_days']:
            print 'Error in %s: short_days' % current_year

def work_dates_between(start_date, end_date):
    u'''
    Возвращает даты рабочих дней
    '''
    if start_date.year < year_start or end_date < start_date or end_date >= year_stop:
        raise ValueError()
    for days in xrange((end_date - start_date).days + 1):
        current_date = start_date + timedelta(days)
        if current_date.weekday() in (5, 6):
            if current_date in work_days:
                yield current_date
        else:
            if current_date not in days_off:
                yield current_date