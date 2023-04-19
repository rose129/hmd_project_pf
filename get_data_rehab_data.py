# 23.04.19

import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_pjt.settings")

django.setup()

from dashboard_drug.models import RehabData

CSV_PATH='./datas/dashboard/rehab_data.csv'

with open(CSV_PATH, 'r',  encoding='utf-8') as file:
    
    data_rows = csv.reader(file, skipinitialspace=True)
    
    next(data_rows, None) 
    
    data_rows = list(filter(None, data_rows))
    
    for row in data_rows:
        if row[0] != None or row[0] !='':
            RehabData.objects.update_or_create(
                years_rehab_data = row[0],
                defaults = {
                    'years_rehab_data' : row[0],
                    'cure_protect' : row[1],
                    'cure_custody' : row[2],
                }
            )
        else:
            continue

