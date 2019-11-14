from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from . import models
from django.contrib.auth.models import User


class DisLikeSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.DisLike
        fields = '__all__'


class LikeSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = '__all__'


class CommentaireSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Commentaire
        fields = '__all__'


class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    article_commentaire = CommentaireSerializer(many=True,  read_only=True, required=False )

    article_like = LikeSerializer(many=True,  read_only=True, required=False)
    
    Dislike = DisLikeSerializer(many=True,  read_only=True, required=False)

    class Meta:
        model = models.Article
        fields = '__all__'

class TagueSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    article_tag = ArticleSerializer(many=True,  read_only=True, required=False)


    class Meta:
        model = models.Tague
        fields = '__all__'


class CategorieSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    article_categorie = ArticleSerializer(many=True,  read_only=True, required=False)

    class Meta:
        model = models.Categorie
        fields = '__all__'

class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    article_auteur = ArticleSerializer(many=True,  read_only=True, required=False)
    user_comment = CommentaireSerializer(many=True,  read_only=True, required=False)
    user_like = LikeSerializer(many=True,  read_only=True, required=False)
    user_dislike = DisLikeSerializer(many=True,  read_only=True, required=False)

    class Meta:
        model = User
        fields = '__all__'