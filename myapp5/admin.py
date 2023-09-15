from django.contrib import admin
from.models import Category, Product


@admin.action(description="�������� ���������� � ����")
def reset_quantity(modeladmin, request, queryset): # ������, ������ � ���� ������
    queryset.update(quantity=0) # �� ��� ������, ���� �������� �� �������� 0


class ProductAdmin(admin.ModelAdmin):
    """������� �������� ��� ���������. ������ ����� Product Admin ��� �������� ���
    admin.ModelAdmin. �� �������� �������� ������ � ���������� � �������, �� �����
    ������ ��������. ������������� ��� �� ���� ������ ��������, ������� ���������
    � ���� ������."""
    list_display = ['name', 'category', 'quantity'] #���������� list_display �������� ����������������� ������. Django ������������� ����� � � ��������� ���������� ������.
    ordering = ['category', '-quantity'] # ordering ����� �������� �����������������������.������������� ���������� ���������.� ������ �� ���������� �� ����������� ���������� �����, ����� �� ���������� �� �������� � ����� ���������.
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = '����� �� ���� �������� �������� (description)'
    actions = [reset_quantity]  # ��������� ���� ������� � �����������
    """��������� �������."""
    #fields = ['name', 'description', 'category', 'date_added', 'rating'] #fields ���������� ������� ������ ��������� �����.���� �������� �����-������,��� ���������� ������������.
    readonly_fields = ['date_added', 'rating'] # readonly_fields ����� �������� ������ �����. ��� ���� ����� �������������,�� ������ ��������.�� ������� ������������ �������.
# 'date_added' ���������� ���� ������������, ��� ��� ���� ������������� ����������������������������������.��������������������������� ������: ... date_added=models.DateTimeField(auto_now_add=True)
    readonly_fields = ['date_added','rating']
    fieldsets = [
        (
            None, {                  # ���������� ���� ��� ������������� ��������
                'classes': ['wide'],  # ����� ['wide'] ����������� ������� ���� � ������
                'fields':['name'],   # � �������� ���� name
            },
        ),
        (
            '�����������',           # ���� �����������
            {
                'classes': ['collapse'], # ���������� ����(�������)
                'description': '��������� ������ � ��� ��������� ��������',# ��� ��������� ������ ��������
                'fields': ['category','description'],# �� ���� ������� �� ��������
            },
        ),
        (
            '�����������',
            {
                'fields': ['price','quantity'],
            }
        ),
        (
            '������� � ������',
            {
                'description': '������� ����������� ������������� �� ������ ������ �����������',
                'fields': ['rating', 'date_added'],
            }
        ),
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)