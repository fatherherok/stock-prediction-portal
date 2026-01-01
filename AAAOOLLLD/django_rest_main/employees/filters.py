import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact') # iexact takes case insensitive
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name='id') # id is for primary key and that is why it used RangeFilter instead of Charfilter
    id_min =  django_filters.CharFilter(method='filter_by_id_range', label='From EMP ID')
    id_max =  django_filters.CharFilter(method='filter_by_id_range', label='To EMP ID')

    class Meta:
        model = Employee
        # fields = ['designation', 'emp_name', 'id'] #this is for the id RangeFilter
        fields = ['designation', 'emp_name', 'id_min', 'id_max']
    
    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value) #gte means greater than or equals to
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value) #gte means less than or equals to
        return queryset