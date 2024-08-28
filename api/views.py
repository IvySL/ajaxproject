from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Address #從models.py檔案匯入Address這個模型

# Create your views here.
def index(request):
    content = 'API首頁'
    response = HttpResponse(content, content_type='text/plain; charset=utf-8')
    return response

def cities(request):
    cities = Address.objects.values('city').distinct()
    cities = [item['city'] for item in cities]
    #print(cities)
    #return HttpResponse('讀取City資料')
    return JsonResponse(cities, safe=False)

#/api/districts/金門縣
#/api/districts/?city_name=金門縣
#兩種不一樣
def districts(request, city_name):
    districts = Address.objects.filter(city=city_name).values('site_id').distinct()
    print(districts)
    districts = [item['site_id'] for item in districts]
    return JsonResponse(districts, safe=False)