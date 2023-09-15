from random import choice, randint, uniform
from django.core.management.base import BaseCommand
from myapp5.models import Category, Product


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        """� ������ add_arguments()������������ �������� ��������� ������'count', ������� ����� ��������� ���������� ���������, ������� ����� �������������."""
        parser.add_argument('count', type=int, help='UserID')

    def handle(self, *args, **kwargs):
        """����� handle() ���������� ��� ���������� �������.�� �������� ��� ��������� �� ��, ������� ������ ��������� � ��������� ��� ��������� �������
        �����,��������� ����� bulk_create(),�������� ����������� ���."""
        categories = Category.objects.all()  # ������ � ���� ������, �������� ��� ���������
        products = []   # ������ ��������� ������� �� ������� �������
        count = kwargs.get('count')    # ����� �������� ������� ��� ���� �������������
        for i in range(1, count + 1):  #
            products.append(Product(        # � ������ ��������� ��������� ��������� �������
                name=f'������� �����{i}',
                category=choice(categories),  # ��������� ����� ��������� �� ������ ����� ���������
                description='������� �������� ��������,������� � ��� ����� �� ������',
                price=uniform(0.01, 999_999.99),
                quantity=randint(1, 10_000),
                rating=uniform(0.01, 9.99),
            ))
        Product.objects.bulk_create(products)  # bulk_create ��������� ������ �������� � ��������� � ���� ������