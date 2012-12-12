from cdr_graph.models import CDR
from django.db.models import Count
from django.template import RequestContext
from django.shortcuts import render_to_response
import datetime

def draw_line_graph(request, date=None):

    #calls = CDR.objects.filter(start_time=date(2012, 12, 5)).count()

    if request.method == "GET":
        
        date = request.GET.get('date')
        call_list = []
        if not date:
            date = datetime.datetime.today()
            year = date.year
            month = date.month
            day = date.day
        else:
            month, day, year = str(date).split("-")

        day_calls = CDR.objects.filter(start_time__year=str(year),start_time__month=str(month),start_time__day=str(day))
        hour_calls = day_calls.extra(select={'hours': 'DATE_FORMAT(start_time, "%%H")'}).values('hours').order_by('hours')
        hour_calls.query.add_count_column()
        hour_calls.query.group_by = ["hours"]
        for hour in hour_calls:
            call_list.append(hour.values())
            
        context = {'values': call_list, "month":month, "day":day, "year":year}
        if call_list:
            return render_to_response('line_graph.html', context, context_instance=RequestContext(request))
        else:
            return render_to_response('no_line_graph.html', context, context_instance=RequestContext(request))

def draw_pie_chart(request, date=None):

    if request.method == "GET":
        
        date = request.GET.get('date')
        call_stats = []
        if not date:
            date = datetime.datetime.today()
            year = date.year
            month = date.month
            day = date.day
        else:
            month, day, year = str(date).split("-")
        stat_list = CDR.objects.filter(start_time__year=str(year),start_time__month=str(month),start_time__day=str(day)).values('status')
        stat_list.query.add_count_column()
        stat_list.query.group_by = ["status"]
        for stat in stat_list:
            call_stats.append(stat.values())

        context = {'values': call_stats, "month":month, "day":day, "year":year}
        if call_stats:
            return render_to_response('pie_chart.html', context, context_instance=RequestContext(request))
        else:
            return render_to_response('no_pie_chart.html', context, context_instance=RequestContext(request))

