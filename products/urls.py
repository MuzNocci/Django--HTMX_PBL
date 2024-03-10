from django.urls import path
from products import views, htmx



urlpatterns = [

    path('list_products/', views.list_products, name='list_products'),

]

html_urlpatterns = [

    path('check_product/', htmx.check_product, name='check_product'),
    path('save_product/', htmx.save_product, name='save_product'),
    path('delete_product/<int:id>', htmx.delete_product, name='delete_product'),

]

urlpatterns += html_urlpatterns