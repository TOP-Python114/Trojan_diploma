from django.shortcuts import render, redirect
from .models import Vacancy
from .forms import VacancyForm
from django.views.generic import DetailView, UpdateView, DeleteView


def index(request):
    return render(
        request,
        'site_vacancy/base.html',
        {
            'text_vacancy': 'Открытые вакансии',
            'text_about': 'Компания ООО "Транспортная Логистика" образована в 2007г. как автотранспортное подразделение группы компаний ЗАО "СЦЛ" (вертикально интегрированный холдинг, в состав которого входят добывающие, транспортные и судостроительные компании). На сегодняшний день, общая численность сотрудников холдинга составляет около 2000 человек. '
                          'ООО "Транспортная логистика" специализируется на поставке инертных материалов автомобильным транспортом.'
        }
    )

def page_vacancy(request):
    return render(
        request,
        'site_vacancy/index.html',
        {
            'vacancies': Vacancy.objects.all(),
        }
    )

class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'site_vacancy/detail.html'
    context_object_name = 'vac'

class VacancyUpdateView(UpdateView):
    model = Vacancy
    template_name = 'site_vacancy/create.html'
    form_class = VacancyForm

class VacancyDeleteView(DeleteView):
    model = Vacancy
    success_url = '/page_vacancy'
    template_name = 'site_vacancy/vacancy-delete.html'
    context_object_name = 'vac'

def create(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/page_vacancy')

    form = VacancyForm()

    data = {
        'form': form
    }

    return render(
        request,
        'site_vacancy/create.html', data
    )

