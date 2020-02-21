# I will use this to configure/do my printouts 

import os
import datetime


today = datetime.datetime.now()

todaydate = today.strftime('%m%d%Y')

file = open('{}_customers.txt'.format(todaydate), 'a+')
file.write("hello\n")