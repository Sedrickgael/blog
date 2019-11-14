from rest_framework import viewsets
from rest_framework import filters
from django.contrib.auth.models import User
from . import models
from . import serializer


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class DisLikeViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = models.DisLike.objects.all()
    serializer_class = serializer.DisLikeSerializer


class LikeViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = models.Like.objects.all()
    serializer_class = serializer.LikeSerializer


class CommentaireViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = models.Commentaire.objects.all()
    serializer_class = serializer.CommentaireSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = models.Article.objects.all()
    serializer_class = serializer.ArticleSerializer


class TagueViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = models.Tague.objects.all()
    serializer_class = serializer.TagueSerializer


class CategorieViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = models.Categorie.objects.all()
    serializer_class = serializer.CategorieSerializer

class UserViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer