from django.shortcuts import render
from .models import chaivarity, Store  
from django.shortcuts import get_object_or_404
from .forms import ChaivarityForm


def all_chai(request):
   chais= chaivarity.objects.all()
   return render(request,'chai/all_chai.html',{'chais':chais})


def chai_detail(request,chai_id):
   chai=get_object_or_404(chaivarity, pk= chai_id)
   return render(request,'chai/chai_details.html',{'chai':chai})  


def chai_store_view(request):
   stores=None 
   if request.method == 'POST':
      form = ChaivarityForm(request.POST)  
      if form.is_valid():
       chai_variety= form.cleaned_data['chai_varity']
       stores= Store.objects.filter(chai_varieties=chai_variety) 
      form=ChaivarityForm()    
   return render(request, 'chai/chai_stores.html', {'stores': stores, 'form': form})

