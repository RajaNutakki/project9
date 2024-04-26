from django.shortcuts import render
from django.views import View
from .models import Product
class DisplayView(View):
    def get(self,request):
        qs=Product.objects.all()
        con_dic={"records":qs}
        return render(request,template_name="display.html",context=con_dic)