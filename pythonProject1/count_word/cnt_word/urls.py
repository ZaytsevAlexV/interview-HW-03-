from django.urls import path
from .views import api_cnt_word,clear_result

urlpatterns = [
    path('', api_cnt_word, name='count_substring'),
    path('clear', clear_result, name='clear_result'),
]
