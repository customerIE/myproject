from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, get_object_or_404 # get_object_or_404 �������� ���������� get,�.�.������ select� ����� � ���� ������.�� ���� ������ �� ����� ������ �� ������� ��,������������� �������� �������� � ������� 404.
from django.views.generic import TemplateView  # ��������� ��������� ������������� �� ������ ������
from.models import Author, Post


def hello(request):   # request ����� ������, �� ������ �� ���������, �� ��� ������ ��� ������������ ����������
    return HttpResponse("Hello World from function!")


class HelloView(View):
    def get(self, request):                    # get ��� post �������
        return HttpResponse("Hello World from class!")


def year_post(request, year):  # ��������� ������ ������� � ���
    text = ""
    ... # ��������� ������ �� ���
    return HttpResponse(f"Posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ... # ��������� ������ ����� � �����
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")


def post_detail(request, year, month, slug):
    ... # ��������� ������ �� ��� � ����� �� ��������������. ���� �������� ��� �������� � ���� ������
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "��� ������� ������ ������ � Python,list()��� []",
        "content": "� �������� ��������� ��������� ��������� ��������� ��� ���, ����� ������ �������� ������� � Python ���������������..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False}) # ���������� ������ ���� � ������� ������ json_dumps_params={'ensure_ascii': False} ��� ��������� �������� �����


def my_view(request):
    context = {"name": "John"}  # ������� ��� ���� ��������� � ���������� ������ ������� {{name}}
    return render(request, "myapp3/my_template.html", context) # request - ������ ������ �� ������������ � ���������� ��� ����� � ��������


class TemplIf(TemplateView):
    template_name = "myapp3/templ_if.html"   # ��� ���������� ��� �������

    def get_context_data(self, **kwargs):   # ���������� ������� - ����� � �������� ����� ����� ���
        context = super().get_context_data(**kwargs) # super() ���������� � ������������� ������ � ��������� ��� ������ (**kwargs) + ��������� ���� ������
        context['message'] = "������,���!"
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        '������': '�������',
        '�������': '���������',
        '������': '�����',
        '�����': '������',
        '���': '�������',
        '�����': '�����',
        '�����': '����������',
    }
    context = {'my_list': my_list, 'my_dict': my_dict} # ����� ������ ����� �� ����� ������� �� ���������� ������ �������, � �������� ������ ��������� � ������� ���������� ������ ������������� � templ_for html ��� � �������� my_list � my_dict
    return render(request, 'myapp3/templ_for.html', context) # ��������� ������ ������������ ���������� � ������ � ������������ ���� �����


def index(request):
    return render(request, "myapp3/index.html") #  ���������� ������ index


def about(request):
    return render(request, "myapp3/about.html") #  ���������� ������ about


def author_posts(request, author_id): # �������� ����� �� ������������ � id ������
    author = get_object_or_404(Author, pk=author_id) # ��������� ������, ���� ������ ��� ������ ���� ������ 404
    posts = Post.objects.filter(author=author).order_by('-id')[:5] # ���� ����� ������, �� ������� ��� �����, ������� ������� ����� order_by('-id') ����������� ��� ����� �� id � �������� ������� [:5] � ������ 5 ������� � ������
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {'post': post}) # � ������� ������� ������ ������������ ������ post_full ��������� ���� � �������� ��������� ���� ����� post �� ����� ����