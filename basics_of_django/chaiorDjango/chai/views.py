from django.shortcuts import render
from.models import chaivarity
from django.shortcuts import get_object_or_404


def all_chai(request):
   chais= chaivarity.objects.all()
   return render(request,'chai/all_chai.html',{'chais':chais})


def chai_detail(request,chai_id):
   chai=get_object_or_404(chaivarity, pk= chai_id)
   return render(request,'chai/chai_details.html',{'chai':chai})