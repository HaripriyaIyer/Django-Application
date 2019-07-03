from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView
# Create your views here.
from catalog.models import Book, Keyword
#from .filters import KeywordFilter
from django.db.models import Q

def index(request):
    """View function for home page of site."""
    #context = RequestContext(request)

    category_list = Keyword.objects.all().count()
    context_dict = {'categories': category_list}

    
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_keywords = Keyword.objects.all().count()
    

    context = {
        'num_books': num_books,
        'num_keywords': num_keywords,
        'categories': category_list,
      }


    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html',context)

def choice(request):
    form = DropDown(request.POST)
    if form.is_valid():
            #redirect to the url where you'll process the input
        return HttpResponseRedirect('/index.html/') # insert reverse or url
    else:

        errors = form.errors or None # form not submitted or it has errors
        return render(request, 'index.html',{
            'form': form,
            'queryset': queryset,
            'errors': errors,
       })

class keywordListView(ListView):
    model = Keyword
    template_name = 'keyword_view.html'
    keyall = Keyword.objects.all()
    
    context_object_name = 'keywords'
    def get_queryset(self):
            """Return the last five published questions."""
            return Keyword.objects.all()


class BookListView(ListView):
    model = Book
    template_name = 'book_view.html'

  
    context_object_name = 'books_title'
    def get_queryset(self):
        """Return the last five published questions."""
        return Book.objects.order_by('sales_rank')[:5]

    #return render(request, 'book_view.html',csontext)

class DetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

# def search(request):
#     key_list = Bool.objects.all()
#     key_filter = KeywordFilter(request.GET, queryset=user_list)
#     return render(request, 'keyword_search.html', {'filter': key_filter})

def search(request):
    template = 'keyword_search.html'
    #results = Book.objects.all()
    category = Keyword.objects.all()
    #category = forms.ChoiceField(choices=CATEGORIES, required=True )

    results = ''
    query = ''
    # if request.method == ["POST"]:
    #     query = request.POST['list']
    #     print(query)
    # # print a
    query = request.GET.get('list')
    print(query)
    if query:
            results = Book.objects.filter(Q(keyword_s__icontains=query))

    #print(results)
    context = {
    'res':results,
    'category':category,

    } 
    return render(request,template,context)

def search(request):
    template = 'keyword_search.html'
    #results = Book.objects.all()
    category = Keyword.objects.all()
    #category = forms.ChoiceField(choices=CATEGORIES, required=True )
    openmediares = ''
    results = ''
    query = ''
    orRes = ''
    completed = False


    # if request.method == ["POST"]:
    #     query = request.POST['list']
    #     print(query)
    # # print a
    query = request.GET.get('list')
    
    if 'yes' in request.GET:
        completed = True

    else:
        completed = False

 
    if query and completed:
        results = Book.objects.filter(Q(keyword_s__iexact=query),Q(isbn='B008F4NSXO')|Q(isbn='B008UX8YPC')|Q(isbn='B00EBO23WO')|Q(isbn='B00U7Y5TI2')|Q(isbn='B01N49MWZH')|Q(isbn='B06XRSTBMN'))

    elif query:    
        results = Book.objects.filter(Q(keyword_s__iexact=query),Q(keyword_s__icontains=query))

    #print(results)

    context = {
    'res':results,
    'category':category,
     } 
    return render(request,template,context)