from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postagens/', views.PostagemListView.as_view(), name='postagens'),
    # path('postagem/<int:postagem_id>',
    #    views.postagem_detail, name='postagem-detail'),
    path('postagem/<int:pk>/',
         views.PostagemDetailView.as_view(), name='postagem-detail'),
    path('autor/<int:pk>/',
         views.AutorDetailView.as_view(), name='autor-detail'),
    path('autores/', views.AutorListView.as_view(), name='autores'),
    path('postagem/<int:pk>/comentar/', views.ComentarioCreate.as_view(),
         name='comentario-create')
]
