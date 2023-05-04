from django.urls import path
from.import views
app_name='shopapp'

urlpatterns=[
    path('',views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat,name='products_by_category'),
    path('<slug:category_slug>|<slug:product_slug>|',views.proddetail,name='proddetail'),

]