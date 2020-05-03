from django.urls import path
from myApp2 import views
urlpatterns=[
	path('',views.hello,name='hello'),
	path('register/',views.register,name='register'),
	path('show/',views.show, name='show'),
	path('edit/<int:id>',views.edit, name='edit'),
	path('delete/<int:id>',views.delete,name='delete')
]
