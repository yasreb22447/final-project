from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import universities
from .models import canada, germany, USA
from django.shortcuts import redirect

from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())


def scholarships(request):
  mymembers = universities.objects.all().values()
  Canada = canada.objects.all().values()
  Germany = germany.objects.all().values()
  usa = USA.objects.all().values()
  template = loader.get_template('scholarships.html')
  context = {
    'mymembers': mymembers,
    'Canada': Canada,
    'Germany': Germany,
    'usa': usa
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = universities.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))



def details2(request, id):
  Canada = canada.objects.get(id=id)
  template = loader.get_template('details2.html')
  context = {
    'Canada': Canada,
  }
  return HttpResponse(template.render(context, request))




def details3(request, id):
  Germany = germany.objects.get(id=id)
  template = loader.get_template('details3.html')
  context = {
    'Germany': Germany,
  }
  return HttpResponse(template.render(context, request))



def details4(request, id):
  usa = USA.objects.get(id=id)
  template = loader.get_template('details4.html')
  context = {
    'usa': usa,
  }
  return HttpResponse(template.render(context, request))


class search():
    model = germany, canada, USA, universities
    template_name = "search_results.html"

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        return germany, canada, USA, universities.objects.filter(
            Q(name__icontains="location") | Q(state__icontains="universtiy")  | Q(state__icontains="Degree")
        )
    




