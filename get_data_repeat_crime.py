# 23.04.19

import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_pjt.settings")

django.setup()

from dashboard_drug.models import RepeatCrime

# csv 파일 위치 변수로 정의
CSV_PATH='./datas/dashboard/repeat_crime.csv'

with open(CSV_PATH, 'r',  encoding='utf-8') as file:
    
    data_rows = csv.reader(file, skipinitialspace=True)
    
    next(data_rows, None) 
    
    data_rows = list(filter(None, data_rows))
    
    for row in data_rows:
        if row[0] != None or row[0] !='':
            RepeatCrime.objects.update_or_create(
                years_repeat_crime = row[0],
                defaults = {
                    'years_repeat_crime' : row[0],
                    'all_drug_user' : row[1],
                    'rp_drug_user' : row[2],
                    'percent' : row[3],
                }
            )
        else:
            continue

