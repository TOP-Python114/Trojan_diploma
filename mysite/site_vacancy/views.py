from django.shortcuts import render, redirect
from .models import Vacancy
from .forms import VacancyForm


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


