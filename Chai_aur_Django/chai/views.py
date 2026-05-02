from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import ChaiVarity

# Create your views here.
def all_chai(request):
    Chais = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'Chais': Chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, id=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai': chai})

def add_chai(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        chai_type = request.POST.get('type')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if name and chai_type:
            chai = ChaiVarity(name=name, type=chai_type, description=description, image=image)
            chai.save()
            return HttpResponseRedirect(reverse('all_chai'))

    return render(request, 'chai/add_chai.html')