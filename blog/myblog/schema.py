import graphene
from graphene import relay, ObjectType , Connection , Node,Int
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import *
from django_filters import OrderingFilter 
from graphql_relay import from_global_id
class ExtendConnection(Connection):
    class Meta:
        abstract = True

    total_count = Int()
    edge_count = Int()

    def resolve_total_count(root, info, **kwargs):
        return root.length
    def resolve_edge_count(root, info, **kwargs):
        return len(root.edges)

class CustomNode(relay.Node):
    class Meta:
        name= 'Node'

class CategorieNode(DjangoObjectType):
    class Meta:
        model = Categorie
        fields = "__all__"
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'article_sous_categorie__titre':['exact','icontains', 'istartswith'],
            
        }
   
      
        interfaces = (relay.Node, )
        connection_class = ExtendConnection

class TagueNode(DjangoObjectType):
    class Meta:
        model = Tague
        fields = "__all__"
        # Allow for some more advanced filtering here
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'article_tag__titre':['exact','icontains', 'istartswith'],
            
        }
        interfaces = (relay.Node, )


class ArticleNode(DjangoObjectType):
    class Meta:
        
        model = Article
        fields = "__all__"
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
        }
        order_by = OrderingFilter(
            fields=(
                ('date_add','date_add'),
                ('nb_like','nb_like'),
            )
        )
        interfaces = (relay.Node, )
        connection_class = ExtendConnection






class CommentaireNode(DjangoObjectType):
    class Meta:
        model = Commentaire
        fields = "__all__"
        # Allow for some more advanced filtering here
        filter_fields = {
            'message': ['exact', 'icontains', 'istartswith'],
            'article':['exact',],
            'user':['exact',],
          
        }
        interfaces = (relay.Node, )
        connection_class = ExtendConnection


class DisLikeNode(DjangoObjectType):
    class Meta:
        model = DisLike
        fields = "__all__"
        # Allow for some more advanced filtering here
        filter_fields = {
            'article': ['exact',],
            'user':['exact',],
          
        }
        interfaces = (relay.Node, )
        connection_class = ExtendConnection

class LikeNode(DjangoObjectType):
    class Meta:
        fields = "__all__"
        model = Like
        filter_fields = ['date_add',]
        interfaces = (relay.Node, )
        connection_class = ExtendConnection


class RelayCreateTague(graphene.relay.ClientIDMutation):
    tag = graphene.Field(TagueNode)
    class Input:
        nom = graphene.String()
        status = graphene.Boolean()
    def mutate_and_get_payload(root,info,**kwargs):
        nom = kwargs.get('nom') or None
        status = kwargs.get('status',None)
        tague = Tague(nom=nom)
        tague.save()           
        return RelayCreateTague(tags=tague)
    
        
class RelayCreateCategorie(graphene.relay.ClientIDMutation):
    categorie = graphene.Field(CategorieNode)
    class Input:
        
        nom = graphene.String()
        status = graphene.Boolean()
    def mutate_and_get_payload(root,info,**kwargs):
        nom = kwargs.get('nom') or None
        description = kwargs.get('description') or None
        image_categorie = info.context.FILES
        if nom is not None and description is not None and image_categorie is not None:
            cate = Categorie(nom=nom,description=description,image_categorie=image_categorie)
        else:
            raise Exception('les paramettre sont requis')
        cate.save()
        return RelayCreateCategorie(categorie=cate)
        
class RelayCreateArticle(graphene.relay.ClientIDMutation):
    article = graphene.Field(ArticleNode)
    class Input:
        categorie = graphene.ID()
        tague = graphene.String()
        titre = graphene.String()
        description = graphene.String()
        contenu = graphene.String()
        
    def mutate_and_get_payload(root,info,**kwargs):
        image = info.context.FILES
        categorie = kwargs.get('categorie') or None
        auteur = info.context.user or None
        tague = kwargs.get('tag') or None
        titre = kwargs.get('titre') or None
        description = kwargs.get('description') or None
        contenu = kwargs.get('contenu') or None
        
        article = None
        if categorie:
            categorie = from_global_id(categorie)
            categorie=categorie[1]
            categorie = Categorie.objects.get(id=categorie)
        if tague :
            t = tague.split(',')
            tableau = []
            for v in t:
                v = from_global_id(v)
                v=v[1]
                utag = Tague.objects.get(pk=v)
                tableau.append(utag)
        data = {
            'image':image,
            'categorie':categorie,
            'auteur':auteur,
            'titre':titre,
            'description':description,
            'contenu':contenu,

        }
        if image and image and categorie and auteur and Tague and titre and description and contenu :
            article = Article(**data)
            article.save()
            for tags in tableau :
                article.tague.add(tags)
                article.save()
            return RelayCreateArticle(article=article)
        else:
            raise Exception('must be have all data to create article')

        




class CommentaireNode(DjangoObjectType):
    class Meta:
        model = Commentaire
        fields = "__all__"
        filter_fields = {
            'message':['icontains','exact','istartswith'],
            'sujet':['icontains','exact','istartswith'],
            'status':['exact',],
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection

class RelayCreateComment(graphene.relay.ClientIDMutation):
    comment = graphene.Field(CommentaireNode)
    class Input:
        article = graphene.ID()
        message = graphene.String()
        sujet = graphene.String()
        status = graphene.Boolean()
        
    def mutate_and_get_payload(root,info,**kwargs):

        article = kwargs.get('article') or None
        user = info.context.user or None
        message = kwargs.get('message') or None
        sujet = kwargs.get('sujet') or None

        
        comment = None
        if article:
            article = from_global_id(article)
            article=article[1]
            article = Article.objects.get(id=article)
        data = {
            'article':article,
            'user':user,
            'message':message,
            'sujet':sujet,
        }
        if article and message and sujet :
                
            comment = Commentaire(
            **data
            )

            comment.save()
                
            return RelayCreateComment(comment=comment)
        else:
            
            raise Exception('must be have all data to create comment')





class RelayCreateLike(graphene.relay.ClientIDMutation):
    like = graphene.Field(LikeNode)
    class Input:

        article = graphene.ID()
        status = graphene.Boolean()
    def mutate_and_get_payload(root,info,**kwargs):
        status = kwargs.get('status',None)
        id = kwargs.get('id') or None
        article = kwargs.get('article') or None
        user = info.context.user or None

        like_user=None
        if article:
            article = from_global_id(article)
            article=article[1]
            article = Article.objects.get(id=article)
        data = {
            'article':article,
            'user':user,
            'status':status,
        }

        if article :
                        
            like_user = Like(
            **data
            )
                        
            like_user.save()
                        
            return RelayCreateLike(like=like_user)
        else:
            raise Exception('must be have all data to create Like')


class RelayCreateDisLike(graphene.relay.ClientIDMutation):
    dis_like = graphene.Field(DisLikeNode)
    class Input:
        article = graphene.ID()
    def mutate_and_get_payload(root,info,**kwargs):

        article = kwargs.get('article') or None
        user = info.context.user or None
        dislike=None

        if article:
            article = from_global_id(article)
            article=article[1]
            article = Article.objects.get(id=article)
        data = {
            'article':article,
            'user':user,

        }
            
        if article :
                        
            dislike = DisLike(
            **data
            )

            dislike.save()
                        
            return RelayCreateDisLike(dis_like=dislike)
        else:
            raise Exception('must be have all data to create disLike')
        


class Query(graphene.ObjectType):
    article = relay.Node.Field(ArticleNode)
    all_articles = DjangoFilterConnectionField(ArticleNode)
    
    category = relay.Node.Field(CategorieNode)
    all_categories = DjangoFilterConnectionField(CategorieNode)
    
    tague = relay.Node.Field(TagueNode)
    all_tags = DjangoFilterConnectionField(TagueNode)
    
    commentaire = relay.Node.Field(CommentaireNode)
    all_commentaires = DjangoFilterConnectionField(CommentaireNode)

    like = relay.Node.Field(LikeNode)
    all_like = DjangoFilterConnectionField(LikeNode)
    
    dislike = relay.Node.Field(DisLikeNode)
    all_dislike = DjangoFilterConnectionField(DisLikeNode)

class RelayMutation(graphene.AbstractType):
    relay_create_categorie = RelayCreateCategorie.Field()
    relay_create_article = RelayCreateArticle.Field()
    relay_create_comment = RelayCreateComment.Field()
    relay_creat_like = RelayCreateLike.Field()
    relay_create_tag = RelayCreateTague.Field()
    relay_create_dislike = RelayCreateDisLike.Field()




