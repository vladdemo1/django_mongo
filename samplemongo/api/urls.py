from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('databases-list/', views.databases_list, name="databases-list"),
    path('database-detail/<str:database>/', views.database_detail, name="database-detail"),
    path('collection-detail/<str:database>/<str:collection>/', views.collection_detail, name="collection-detail"),
    path('collection-detail-filter/<str:database>/<str:collection>/', views.collection_detail_filter, name="collection-detail-filter"),
    path('add-to-collection/<str:database>/<str:collection>/', views.add_to_collection, name="add-to-collection"),
    path('update-in-collection/<str:database>/<str:collection>/<str:mode>/', views.update_in_collection, name="update-in-collection"),
    path('delete-element/<str:database>/<str:collection>/<str:mode>/', views.delete_element, name="delete-element"),
]