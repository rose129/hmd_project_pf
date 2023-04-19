# 23.04.19

import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_pjt.settings")

django.setup()

from dashboard_drug.models import ForeignDrugUserNation

CSV_PATH='./datas/dashboard/foreign_drug_user_nation.csv'

with open(CSV_PATH, 'r',  encoding='utf-8') as file:
    
    data_rows = csv.reader(file, skipinitialspace=True)
    
    next(data_rows, None) 
    
    data_rows = list(filter(None, data_rows))
    
    for row in data_rows:
        
        if row[0] != None or row[0] !='':
            ForeignDrugUserNation.objects.update_or_create(
                country = row[0],
                defaults = {
                    'country' : row[0],
                    'num_drug_user' : row[1],
                    'percent' : row[2],
                }
            )
        else:
            continue

