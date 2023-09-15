from django.core.management.base import BaseCommand
from myapp2.models import User


# class Command(BaseCommand):
#     help = "Get user byid."
#
#     def add_arguments(self, parser):
#         parser.add_argument('id', type=int, help='UserID') # ��������� ������ � id �������� � ���������� ��� ��� id ������������
#
#     def handle(self, *args, **kwargs):
#         id = kwargs['id']                  # �� ������� ������ �� ����� ���� ��������� �������� ������ ����
#         user = User.objects.get(id=id)     # � ������� get ����� ��� ��� ����� id. ���� ������ ������������ ��� get ������� ������. ����� ������������ filter
#         self.stdout.write(f'{user}')


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='UserID') # ��� �� ��� ��� � ����, pk ��������� ���� ������ id ����� �� �������� ���������

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()      # ������ ������ get �� ������� ������ ���� ������ ��������� ��� first() - ������� ������� ���� �� ���������
        self.stdout.write(f'{user}')