from django.shortcuts import render

# 23.04.17 추가
from django.views import View

# model 불러오기
from .models import NumDrugUser, AgeGroupArrest, DrugItems, GlobalAddicts, ForeignDrugUser, ForeignDrugUserNation, RepeatCrime, RehabData

# Create your views here.
class Dashboard(View):
    template_name = 'dashboard_drug/dashboard.html'
    
    def get(self, request):
        num_drug_users = NumDrugUser.objects.all()
        age_group_arrests = AgeGroupArrest.objects.all()
        drug_items = DrugItems.objects.all()
        global_addicts = GlobalAddicts.objects.all()
        foreign_drug_users = ForeignDrugUser.objects.all()
        foreign_drug_user_nation = ForeignDrugUserNation.objects.all()
        repeat_crime = RepeatCrime.objects.all()
        rehab_data = RehabData.objects.all()
        
        context = {
            'num_drug_users': num_drug_users,
            'age_group_arrests': age_group_arrests,
            'drug_items': drug_items,
            'global_addicts': global_addicts,
            'foreign_drug_users': foreign_drug_users,
            'foreign_drug_user_nation': foreign_drug_user_nation,
            'repeat_crime': repeat_crime,
            'rehab_data': rehab_data,
        }
        
        return render(request, self.template_name, context)
