# 23.04.19

import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_pjt.settings")

django.setup()

from dashboard_drug.models import DrugItems

CSV_PATH='./datas/dashboard/drug_items.csv'

with open(CSV_PATH, 'r',  encoding='utf-8') as file:
    
    data_rows = csv.reader(file, skipinitialspace=True)
    
    next(data_rows, None) 
    
    data_rows = list(filter(None, data_rows))
    
    for row in data_rows:
        if row[0] != None or row[0] !='':
            DrugItems.objects.update_or_create(
                drug_items = row[0],
                defaults = {
                    'drug_items' : row[0],
                    'drug_items_arrested' : row[1],
                }
            )
        else:
            continue

