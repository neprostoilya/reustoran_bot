from django.urls import path
from .views import MainView, CategoriesView, SelectTimeForOrderView, \
    SelectTableForOrderView, CartView, SelectQuantityOfPeopleForOrderView

app_name = 'frontend'

urlpatterns = [
    path('<token>/', MainView.as_view(), name='events_and_dishes_view'),
    path('<token>/category/<category>/', CategoriesView.as_view(), name='categories_view'),
    path('<token>/cart/', CartView.as_view(), name='carts_view'),
    path('<token>/select_time/', SelectTimeForOrderView.as_view(), name='select_time_view'),
    path('<token>/select_table/', SelectTableForOrderView.as_view(), name='select_table_view'),
    path('<token>/select_quantity_of_people/', SelectQuantityOfPeopleForOrderView.as_view(), name='select_quantity_of_people_view'),
]