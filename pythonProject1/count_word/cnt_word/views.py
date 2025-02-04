from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .forms import FormEnterCnt
from .models import Result
def count_word(path_file, find_word):
    with open(path_file, 'r',encoding='utf8') as input_file:
        cnt=0
        for line in input_file:
            _list_line=line.split()
            for word in _list_line:
                word = word.lower()
                if word == find_word:
                    cnt += 1
    return cnt
@csrf_protect
def api_cnt_word(request):
    if request.method == 'GET':
        # передали форму
        total_list = Result.objects.all()
        sum_cnt = Result.objects.all().aggregate(Sum('cnt'))
        form = FormEnterCnt()
        return render(request, 'index.html', {'form': form, 'sum_cnt': sum_cnt, 'total_list': total_list})
    if request.method == 'POST':
        form = request.POST
        cnt = count_word(form['name_file'],form['word'])
        Result.objects.create(path_file=form['name_file'],word=form['word'], cnt=cnt)
        sum_cnt = Result.objects.filter(word=form['word']).aggregate(Sum('cnt'))
        return redirect('count_substring')

@csrf_protect
def clear_result(request):
    Result.objects.all().delete()
    response = redirect('count_substring')
    return response