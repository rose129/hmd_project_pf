# 23.04.19
# csv 파일을 DB에 넣는 코드

import os
import django
import csv

# 일반 파이썬앱(스크립트)에서 django ORM을 사용하려면 다음의 설정 필요
# django 환경설정 파일 지정

# settings.py 파일이 위치한 폴더를 지정해야 함 (여기서는 doit_django_project 임)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_pjt.settings")
# django settings 메모리 로딩 적용
django.setup()

# food 클래스와 연결된 테이블에 data를 ORM으로 업로딩하기 휘애 import함

# 위 두개의 코드 때문에 아래에서 import를 사용함
from dashboard_drug.models import NumDrugUser

# csv 파일 위치 변수로 정의
CSV_PATH='./datas/dashboard/num_drug_users.csv'

with open(CSV_PATH, 'r',  encoding='utf-8') as file:
    
    # csv.reader (파일식별자)
    data_rows = csv.reader(file, skipinitialspace=True)

    # header(csv 파일의 첫번째 줄 - th부분) 제외
    next(data_rows, None) 
    
    # print('object로 출력되는것 확인 :::::', data_rows)
    # print('값이 null이여도 요소로 취급함 :::::', list(data_rows))
    
    # 비어있는 줄 없애기
    # data_rows = filter(None, list(data_rows))
    
    # csv.reader 객체는 이터레이터이므로, 데이터를 한 번만 읽을 수 있다.
    # 두 번째 for 루프에서 데이터가 없어서 루프가 돌지 않기 때문에 데이터를 미리 리스트에 저장한 후 루프를 돌아야 함.
    data_rows = list(filter(None, data_rows))
    
    for row in data_rows:
        print(row)
        
        # for 문을 돌려 값이 null이나 공백이면 예외처리하기
        if row[0] != None or row[0] !='':
            
            # 추가문 (이 코드를 살려두면 계속 코드가 추가됨)
            # Foods.objects.create(
            #     cook_name = row[0],
            #     count = row[1],
            #     unit_price = row[2],
            # )
            
            # 데이터 중복 예외처리, 업로딩
            # 예외 처리 : 만약에 cook_name이 있다면, 업데이터
            NumDrugUser.objects.update_or_create(
                # filter : 중복을 체크할 값
                # 중복되지 않는 값을 기준으로 중복 여부를 체크함
                years_drug_user = row[0],

                # menu_name이 cook_name 컬럼에 값이 없으면 테이블에 저장하도록 함
                # new value : filter로 돌려서 나온 결과에 중복값이 없을 때
                defaults = {
                    'years_drug_user' : row[0],
                    'num_drug_user' : row[1],
                }
            )
        else:
            # 메뉴가 없을 경우는 pass
            continue

