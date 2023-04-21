from django.db import models

# Create your models here.

# 23.04.17 table 제작

# 1. 최근 5년간 마약류 사범 수
# (단위: 명) : 2018 ~ 2022년 - Basic Bar Chart
class NumDrugUser(models.Model):
    years_drug_user = models.IntegerField(verbose_name='연도')
    num_drug_user = models.IntegerField(verbose_name='마약사범 수 (단위 : 명)')
    
    def __str__(self):
        return f'{self.years_drug_user} : {self.num_drug_user}'
    
    class Meta:
        verbose_name_plural = "대시보드 1 : 최근 5년간 마약류 사범 수"


# 2. 2022년 기준 연령대별 단속 내역
# (단위: 명) : 19세 이하 / 20대 / 30대 / 40대 / 50대 / 60대 이상 - Horizontal Bar Chart
class AgeGroupArrest(models.Model):
    age_group = models.CharField(max_length=20, verbose_name='연령대')
    num_age_arrested = models.IntegerField(verbose_name='검거 수 (단위 : 명)')
    
    def __str__(self):
        return f'{self.age_group} : {self.num_age_arrested}'
    
    
    class Meta:
        verbose_name_plural = "대시보드 2 : 2022년 기준 연령대별 단속 내역"    


# 3. 2022년 기준 마약류 품목별 단속 현황
# (단위: g) : 신종마약 몇 g / 필로폰 몇 g / 대마 몇 g / 코카인 몇 g / 기타 몇 g - Doughnut Chart
class DrugItems(models.Model):
    drug_items = models.CharField(max_length=20, verbose_name='마약 품목')
    drug_items_arrested = models.IntegerField(verbose_name='압수량 (단위 : g)')
    
    def __str__(self):
        return f'{self.drug_items} : {self.drug_items_arrested}'
    
    class Meta:
        verbose_name_plural = "대시보드 3 : 2022년 기준 마약류 품목별 단속 현황"


# 4. 전 세계 지역별 마약 중독자 수
# (단위: 만 명) : 북미 / 남미 / 유럽 / 아프리카 / 중동 / 서아시아 / 동아시아 / 인도 / 호주 (세계 지도를 연하게 바탕으로 깔고, 그 위에) - Bubble Chart
class GlobalAddicts(models.Model):
    country = models.CharField(max_length=100, verbose_name='지역')
    num_drug_addicts = models.IntegerField(verbose_name='중독자 수 (단위 : 만 명)')
    
    def __str__(self):
        return f'{self.country} : {self.num_drug_addicts}'
    
    class Meta:
        verbose_name_plural = "대시보드 4 : 전 세계 지역별 마약 중독자 수"


# 5. 최근 5년간 국내 외국인 마약류 사범 현황
# (단위: 명) : 2018 ~ 2022년 - Basic Bar Chart
# class name: ForeignDrugUser
# label: (x)f_years, (y)f_num_drug_user
class ForeignDrugUser(models.Model):
    years_foreign_drug_users = models.IntegerField(verbose_name='연도')
    personnel = models.IntegerField(verbose_name='외국인 마약사범 수 (단위 : 명)')
    f_num_drug_user = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='국내외 전체사범 중 비율 (%)')
    
    def __str__(self):
        return f'{self.years_foreign_drug_users} : {self.personnel} - {self.f_num_drug_user}'
    
    
    class Meta:
        verbose_name_plural = "대시보드 5 : 최근 5년간 국내 외국인 마약류 사범 현황"


# 6. 2022년 기준 국내 외국인 마약사범 국적별 현황
# (단위: 명) : 태국 / 중국 / 베트남 / 우즈베키스탄 / 러시아 / 기타 - Doughnut Chart
# class name: ForeignDrugUserNation
class ForeignDrugUserNation(models.Model):
    country = models.CharField(max_length=100, verbose_name='국적')
    num_drug_user = models.IntegerField(verbose_name='사범 수 (단위 : 명)')
    percent = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='국적별 비중 (%)')
    
    def __str__(self):
        return f'{self.country} : {self.num_drug_user} - {self.percent}'

    class Meta:
        verbose_name_plural = "대시보드 6 : 2022년 기준 국내 외국인 마약사범 국적별 현황"


# 7. 2021년 까지 연도별 재범률
# (재범률 단위: %), (사범/인원 단위: 명) : 2017 ~ 2021년 - Mixed Line Chart
# class name: RepeatCrime
# label: (x)rp_years, (y)all_drug_user, rp_drug_user
class RepeatCrime(models.Model):
    years_repeat_crime = models.IntegerField(verbose_name='연도')
    all_drug_user = models.IntegerField(verbose_name='전체사범 수 (단위 : 명)')
    rp_drug_user = models.IntegerField(verbose_name='재범인원 수 (단위 : 명)')
    percent = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='재범률 (%)')
    
    def __str__(self):
        return f'{self.years_repeat_crime} : {self.all_drug_user} - {self.rp_drug_user} - {self.percent}'

    class Meta:
        verbose_name_plural = "대시보드 7 : 2021년 까지 연도별 재범률"


# 8. 2021년 까지 중독자 치료보호 및 감호 현황
# (단위: 명) : 2017 ~ 2021년 - Mixed Line Chart
# class name: RehabData
# label: (x)cure_years, (y)cure_protect, cure_custody
class RehabData(models.Model):
    years_rehab_data = models.IntegerField(verbose_name='연도')
    cure_protect = models.IntegerField(verbose_name='치료보호 (단위 : 명)')
    cure_custody = models.IntegerField(verbose_name='치료감호 (단위 : 명)')
    
    def __str__(self):
        return f'{self.years_rehab_data} : {self.cure_protect} {self.cure_custody}'

    class Meta:
        verbose_name_plural = "대시보드 8 : 2021년 까지 중독자 치료보호 및 감호 현황"