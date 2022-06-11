from django.shortcuts import render
from django.shortcuts import redirect
from django.core import serializers
# 重定向包
from django.core.paginator import Paginator#分页功能
from app import models
# Create your views here.


def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('UserName')
        user_passwd = request.POST.get('PassWord')
        users_obj = models.User.objects.get(UserName=user_name)
        if not users_obj is None:
            if users_obj.PassWord == user_passwd:
                return redirect('/app/booklist')
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def addbook(request):
    if request.method == 'POST':
        # 获取数据
        book_id = request.POST.get('id')
        book_name = request.POST.get('BookName')
        book_author = request.POST.get('Author')
        book_price = request.POST.get('Price')
        book_publisher = request.POST.get('Publisher')
        book_isbn = request.POST.get('ISBN')
        book_isreadonline = request.POST.get('IsReadOnline')
        book_booknum = request.POST.get('BookNum')
        # 保存到数据库中
        models.Book.objects.create(id=book_id, BookName=book_name, Author=book_author,
                                  Price=book_price, Publisher=book_publisher,
                                  ISBN=book_isbn, IsReadOnline=book_isreadonline,
                                  BookNum=book_booknum)
        return redirect('/app/booklist')
    return render(request, 'addbook.html')


def booklist(request):
    # 获取数据库中的数据并保存到字典中传入页面
    book_list = models.Book.objects.all()
    # 测试分页功能
    paginator = Paginator(book_list, 5)
    page = request.GET.get('page', 1)
    books = paginator.page(page)
    return render(request, 'booklist.html', {"book_obj_list": books})


def edit_book(request):
    if request.method == 'POST':
        # 获取id
        book_id = request.POST.get('id')
        book_name = request.POST.get('BookName')
        book_author = request.POST.get('Author')
        book_price = request.POST.get('Price')
        book_publisher = request.POST.get('Publisher')
        book_isbn = request.POST.get('ISBN')
        book_isreadonline = request.POST.get('IsReadOnline')
        book_booknum = request.POST.get('BookNum')
        # 根据id去数据库中找对象
        book_obj = models.Book.objects.get(id=book_id)
        # 修改
        book_obj.BookName = book_name
        book_obj.Author = book_author
        book_obj.Price = book_price
        book_obj.Publisher = book_publisher
        book_obj.ISBN = book_isbn
        book_obj.IsReadOnline = book_isreadonline
        book_obj.BookNum = book_booknum
        # 保存
        book_obj.save()
        # 重定向到列表
        return redirect('/app/booklist')

    else:
        # 获取id
        id = request.GET.get('id')
        # 去数据库中查找对应的数据
        book_obj = models.Book.objects.get(id=id)
        book_obj_list = models.Book.objects.all()
        # 返回页面
        return render(request, 'edit_book.html',
                      {"book_obj": book_obj, "book_obj_list": book_obj_list})


def del_book(request):
    # 获取要删除的id
    id = request.GET.get("id")
    # 根据id删除出局库中的记录
    models.Book.objects.filter(id=id).delete()
    return redirect("/app/booklist")


def find(request):
    if request.method == 'POST':
        # 获取数据
        book_name = request.POST.get('BookName')
        book_author = request.POST.get('Author')
        book_isreadonline = request.POST.get('IsReadOnline')
        if book_name != '':
            book_obj = models.Book.objects.filter(BookName=book_name)
            return render(request, 'find.html', {"book_obj_list": book_obj})
        # 获取数据库中数据
        if book_author != '':
            book_obj = models.Book.objects.filter(Author=book_author)
            return render(request, 'find.html', {"book_obj_list": book_obj})
        if book_isreadonline != '':
            book_obj = models.Book.objects.filter(IsReadOnline=book_isreadonline)
            return render(request, 'find.html', {"book_obj_list": book_obj})
    return render(request, 'find.html')


def find_end(request):

    return render(request, 'find_end.html')


