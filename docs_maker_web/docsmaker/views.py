from django.shortcuts import render
from .models import DocsMaker

def docs_maker(request):
    dm = DocsMaker.objects.all()
    return render(request, 'docsmaker/dm_index.html', {'docs_maker': dm})
