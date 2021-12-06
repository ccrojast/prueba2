from django.conf.urls import url 
from tutorials import views 
 
urlpatterns = [ 
#    url(r'^api/tutorials$', views.tutorial_list),
#    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
#    url(r'^api/tutorials/published$', views.tutorial_list_published),
    url(r'^api/comentarios$', views.comentarios_producto),
    url(r'^api/pregunta$', views.preguntas_producto),
    url(r'^api/calificaciones$', views.calificaciones_producto),
]