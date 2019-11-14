from django.db import models
from tinymce import HTMLField
from django.contrib.auth.models import User
from django.utils.text import slugify
#we can change default User with your custom User

class Categorie(models.Model):

    """Model definition for Categorie."""
    nom = models.CharField(max_length=100)
    image_categorie = models.ImageField(upload_to='images/blog/categories')
    description = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = "Categorie d'articles"
        verbose_name_plural = "Categories d'articles"

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom

class Tague(models.Model):
    """Model definition for Tag."""
    nom = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Les Tags Du blog'
        verbose_name_plural = 'Les Tags Du Blog'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.nom



class Article(models.Model):
    """Model definition for Article."""
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='article_categorie')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_auteur')
    tague = models.ManyToManyField(Tague, related_name='article_tag')
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/')
    contenu = models.TextField()
    vue = models.PositiveIntegerField()
    slug = models.SlugField(max_length=255,editable=False,)
    nb_like =  models.PositiveIntegerField()
    nb_dislike =  models.PositiveIntegerField()
    nb_commentaire = models.PositiveIntegerField()

    status = models.BooleanField(default=False,null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    @property
    def nbr_like(self):
        n = self.article_like.all().count()
        return n

    @property
    def nbr_comment(self):
        n = self.article_commentaire.all().count()
   
        return n
    
    @property
    def nb_dislike(self):
        n = self.Dislike.all().count()
        return n



    def save(self, *args, **kwargs):
        self.titre_slug =slugify(self.titre)
        self.nb_com = self.nbr_comment
        self.nb_like=self.nbr_like
        self.nb_dislike = self.nb_dislike

        super(Article, self).save(*args, **kwargs)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Articles du Blogs'
        verbose_name_plural = 'Articles du Blogs'

    def __str__(self):
        """Unicode representation of Article."""
        return self.titre
    
class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_commentaire')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    message = HTMLField('message')
    sujet = models.CharField(max_length=250)
    
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Categorie."""

        verbose_name = " Commentaires d'articles"
        verbose_name_plural = " Commentaires d'articles"


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Categorie."""

        verbose_name = " Likes d'Article"
        verbose_name_plural = " Likes d'Article"
    
class DisLike(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='Dislike')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_dislike')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Categorie."""

        verbose_name = " DisLikes d'Article"
        verbose_name_plural = "  DisLikes d'Article "