from django.shortcuts import render
from blog.models import BookCategory

def index(req):
    book_category_list = BookCategory.objects.all()
    first_book_category_list = [b for b in book_category_list if b.p_category is None]
    print first_book_category_list
    return render(req, 'index.html', {'first_book_category_list':first_book_category_list})

