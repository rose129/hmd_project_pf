from django.contrib import admin

# 23.04.17 추가
from .models import NumDrugUser, AgeGroupArrest, DrugItems, GlobalAddicts, ForeignDrugUser, ForeignDrugUserNation, RepeatCrime, RehabData

from django.contrib.humanize.templatetags.humanize import intcomma

# Register your models here.
class NumDrugUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'years_drug_user', 'comma_num_drug_user')
    
    def comma_num_drug_user(self, obj):
        return intcomma(obj.num_drug_user)
    comma_num_drug_user.short_description = '마약류 사범 수 (단위 : 명)'
    
admin.site.register(NumDrugUser, NumDrugUserAdmin)


class AgeGroupArrestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'age_group', 'comma_num_age_arrested')
    
    def comma_num_age_arrested(self, obj):
        return intcomma(obj.num_age_arrested)
    comma_num_age_arrested.short_description = '검거 수 (단위 : 명)'
    
admin.site.register(AgeGroupArrest, AgeGroupArrestAdmin)


class DrugItemsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'drug_items', 'comma_drug_items_arrested')
    
    def comma_drug_items_arrested(self, obj):
        return intcomma(obj.drug_items_arrested)
    comma_drug_items_arrested.short_description = '단속 수 (단위 : g)'
    
admin.site.register(DrugItems, DrugItemsAdmin)


class GlobalAddictsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'country', 'comma_num_drug_addicts')
    
    def comma_num_drug_addicts(self, obj):
        return intcomma(obj.num_drug_addicts)
    comma_num_drug_addicts.short_description = '중독자 수 (단위 : 만 명)'
    
admin.site.register(GlobalAddicts, GlobalAddictsAdmin)


# 23.04.18 추가
class ForeignDrugUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'years_Foreign_drug_users', 'comma_personnel', 'comma_f_num_drug_user')
    
    def comma_personnel(self, obj):
        return intcomma(obj.personnel)
    comma_personnel.short_description = '외국인 마약류 사범 (단위 : 명)'
    
    def comma_f_num_drug_user(self, obj):
        return intcomma(obj.f_num_drug_user)
    comma_f_num_drug_user.short_description = '국내외 전체사범 중(%)'
    
admin.site.register(ForeignDrugUser, ForeignDrugUserAdmin)


class ForeignDrugUserNationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'country', 'comma_num_drug_user', 'percent')
    
    def comma_num_drug_user(self, obj):
        return intcomma(obj.num_drug_user)
    comma_num_drug_user.short_description = '인원 (단위 : 명)'
    
admin.site.register(ForeignDrugUserNation, ForeignDrugUserNationAdmin)


class RepeatCrimeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'years_repeat_crime', 'comma_all_drug_user', 'comma_rp_drug_user', 'percent')
    
    def comma_all_drug_user(self, obj):
        return intcomma(obj.all_drug_user)
    comma_all_drug_user.short_description = '전체사범 (단위 : 명)'
    
    def comma_rp_drug_user(self, obj):
        return intcomma(obj.all_drug_user)
    comma_rp_drug_user.short_description = '재범인원 (단위 : 명)'
    
admin.site.register(RepeatCrime, RepeatCrimeAdmin)


class RehabDataAdmin(admin.ModelAdmin):
    list_display = ('pk', 'years_rehab_data', 'comma_cure_protect', 'comma_cure_custody')
    
    def comma_cure_protect(self, obj):
        return intcomma(obj.cure_protect)
    comma_cure_protect.short_description = '치료보호 (단위 : 명)'
    
    def comma_cure_custody(self, obj):
        return intcomma(obj.cure_custody)
    comma_cure_custody.short_description = '치료감호 (단위 : 명)'
    
admin.site.register(RehabData, RehabDataAdmin)