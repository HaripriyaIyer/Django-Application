from django.urls import path
from . import views
#from django_filters.views import FilterView
#from catalog.filters import filter

urlpatterns = [
    path('', views.index, name='index'),
    path('keys_list/', views.keywordListView.as_view(), name='keyword_view'),
    path('books_list/', views.BookListView.as_view(), name='book_view'),
    path('books_search/', views.search, name='keyword_search'),
    #path('search/', FilterView.as_view(filterset_class=KeywordFilter, template_name='keyword_search.html'), name='keyword_search'),

]


