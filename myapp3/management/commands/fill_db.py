from random import choices                        # ����� ��������� ������� ���� � �� ��������
from django.core.management.base import BaseCommand # ��� �������� ������
from myapp3.models import Author, Post


# LOREM ����� ���������� ������

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."\
        "Accusamus accusantium aut beatae consequatur consequunturcumque,delectusetilloistemaxime"\
        "nihilnonnostrumodioofficia,perferendisplaceat quasiquibusdamquisquamquodsunt"\
        "tempore temporibus ut voluptatum? A aliquam culpa ducimus,eaqueeumillomollitianemo"\
        "tempore unde vero! Blanditiis deleniti ex hic, laboriosammaioresoditofficiapraesentium"\
        "quaequisquamratione,reiciendis,veniam.Accusantium assumendaconsecteturconsequatur"\
        "consequunturcorporisdignissimosducimuseiusesteum expeditailloin,inventore"\
        "ipsumiustomaioresminusmollitianecessitatibusneque nisioptioquasiquoquod,"\
        "quosremrepellendustemporibustotamundevelvelit verovitaevoluptates."


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='UserID')  # ��������� count ��� ���� �������

    def handle(self, *args, **kwargs):
        text = LOREM.split()     # ����� ���� ����� �� ��������� �����
        count = kwargs.get('count')# ��������� �� ����� ������� �� �������� � ��������� ������
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@mail.ru') # ��������� �� 1 �� count ������������ +1 ��������� ����� � ���������
            author.save()
            for j in range(1, count + 1):   # c ������� ������ ����� ��� �� ��� � � ��������
                post = Post(
                    title=f'Title-{j}',    # ����� �� ���������
                    content=" ".join(choices(text, k=64)), # �������� ������ 64 ����� � ��������� �� ����� ������ ������ ����������� ��������
                    author=author  # � �������� ������ ��������� ������ � 27 ������
                )
                post.save()