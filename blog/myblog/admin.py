from django.contrib import admin

#importation des models
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):

    #les champs à afficher dans la table
    list_display = (
        'viw_image',
        'nom',
        'status',
        'date_add',
        'date_upd',        
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )

    search_fields = (
        'nom',
    )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['nom', 'viw_image']
    
    list_per_page = 3

    ordering = ['nom',]

    readonly_fields = ['detail_image']

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les catégories sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les catégories sélectionnées'

    def viw_image(self, obj):
        return mark_safe('<img src="{img_url}" width="100px" height="50" />'.format(img_url=obj.image_categorie.url))

    def detail_image(self, obj):
        return mark_safe('<img src="{img_url}" width="300px" height="150" />'.format(img_url=obj.image_categorie.url))
    
@admin.register(models.Tague)
class TagueAdmin(admin.ModelAdmin):

    #les champs à afficher dans la table
    list_display = (
        'nom',
        'status',
        'date_add',
        'date_upd',
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )

    search_fields = (
        'nom',
    )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['nom',]
    
    list_per_page = 3

    ordering = ['nom',]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les sous-catégories sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les sous-catégories sélectionnées'

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    
    #les champs à afficher dans la table
    list_display = (
        'categorie',
        'titre',
        'auteur',
        'status',
        'date_add',
        'date_upd',
        'view_image',
            
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'categorie',
        'tague',
    )

    search_fields = (
        'categorie',
        'tague',
        'titre',
    )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['titre', 'view_image']
    
    list_per_page = 3

    ordering = ['titre',]

    readonly_fields = ['detail_image']

    fieldsets = [
        ('Titre et visibilité', {'fields' : ['titre', 'status']}),
        ('Description et image', {'fields' : ['description', 'image', 'contenu', 'auteur']}),
        ('Tague et Sous catégorie', {'fields' : ['categorie', 'tague']}),
    ]

    filter_horizontal = ('tague',)

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les produits sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les produits sélectionnées'

    def view_image(self, obj):
        return mark_safe('<img src="{img_url}" width="100px" height="50" />'.format(img_url=obj.image.url))

    def detail_image(self, obj):
        return mark_safe('<img src="{img_url}" width="300px" height="150" />'.format(img_url=obj.image.url))

    
@admin.register(models.Commentaire)
class CommentaireAdmin(admin.ModelAdmin):

    #les champs à afficher dans la table
    list_display = (
        'user',
        'article',
        'status',
        'sujet',
        'date_add',
        'date_upd',
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )

    search_fields = (
        'sujet',
    )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['user',]
    
    list_per_page = 10

    ordering = ['sujet',]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les sous-catégories sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les sous-catégories sélectionnées'


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):

    #les champs à afficher dans la table
    list_display = (
        'user',
        'article',
        'status',
        'date_add',
        'date_upd',
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )

    search_fields = (
        'user',
    )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['user',]
    
    list_per_page = 10

    ordering = ['user',]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les sous-catégories sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les sous-catégories sélectionnées'


@admin.register(models.DisLike)
class DisLikeAdmin(admin.ModelAdmin):

    #les champs à afficher dans la table
    list_display = (
        'user',
        'article',
        'status',
        'date_add',
        'date_upd',
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )

    search_fields = (
        'user',
    )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['user',]
    
    list_per_page = 10

    ordering = ['user',]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les sous-catégories sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les sous-catégories sélectionnées'
