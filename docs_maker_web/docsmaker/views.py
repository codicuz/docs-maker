from django.shortcuts import render
from .models import DocsMaker
from docs_maker_messages import set_language

l = set_language('ru')

def docs_maker(request):
    dm = DocsMaker.objects.all()
    dm_messages = {'docs_maker': l.gettext('App Title'), 'btn_clicked': l.gettext('btn_clicked')}
    return render(request, 'docsmaker/dm_index.html', {'dm': dm_messages})
