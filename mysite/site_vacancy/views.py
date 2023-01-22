from django.shortcuts import render
from django.http import HttpResponse


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
    return render(request, 'site_vacancy/index.html')

