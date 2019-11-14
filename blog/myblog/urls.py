from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from . import viewsets


router = DefaultRouter()
router.register('commentaireapi', viewsets.CommentaireViewSet, base_name='commentaireapi')
router.register('likeapi', viewsets.LikeViewSet, base_name='likeapi')
router.register('dislikeapi', viewsets.DisLikeViewSet, base_name='dislikeapi')
router.register('articleapi', viewsets.ArticleViewSet, base_name='articleapi')
router.register('tagueapi', viewsets.TagueViewSet, base_name='tagueapi')
router.register('categorieapi', viewsets.CategorieViewSet, base_name='categorieapi')
router.register('userapi', viewsets.UserViewSet, base_name='userapi')

urlpatterns = [
    path('', views.home , name='home')
]

urlpatterns += router.urls

