from django.urls import path
from . import views 

urlpatterns=[
    path("",views.index,name="index"),
    path("newblogs/",views.newblogs,name="newblogs"),
    path("individual/<int:pk>/",views.individual,name="individual"),
    path("editblogs/<int:pk>/",views.editblogs,name="editblogs"),
    path("delete/<int:pk>",views.deleteblog,name='deleteblog'),
    path("delete/comment/<int:pk>",views.delcomment,name='delcomment')
   

]