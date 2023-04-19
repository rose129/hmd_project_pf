# 23.04.19

import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_pjt.settings")

django.setup()

from dashboard_drug.models import AgeGroupArrest

CSV_PATH ='./datas/dashboard/age_group_arrests.csv'

with open(CSV_PATH, 'r',  encoding='utf-8') as file:
    
    data_rows = csv.reader(file, skipinitialspace=True)
    
    next(data_rows, None)
    
    data_rows = list(filter(None, data_rows))
    
    for row in data_rows:
        
        if row[0] != None or row[0] !='':
            
            AgeGroupArrest.objects.update_or_create(
                age_group = row[0],
                defaults = {
                    'age_group' : row[0],
                    'num_age_arrested' : row[1],
                }
            )
        else:
            continue

