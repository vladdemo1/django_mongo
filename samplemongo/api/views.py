import json
from bson import json_util

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .serializers import TaskSerializer

# from .models import Task

from .mongo_con import get_client


@api_view(['GET'])
def api_overview(request):
    """
    Full list about url's api
    """
    api_urls = {
        'List': '/databases-list/',
        'Database Detail': '/database-detail/<str:pk>',
        'Collection Detail': '/collection-detail/<str:database>/<str:collection>',
        'Collection Detail with Filter': '/collection-detail-filter/<str:database>/<str:collection>/?param=value',
        'Add to Collection': '/add-to-collection/<str:database>/<str:collection>/',
        'Update in Collection': '/update-in-collection/<str:database>/<str:collection>/<str:mode>/',
        'Delete from Collection': '/delete-element/<str:database>/<str:collection>/<str:mode>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def databases_list(request):
    """
    Show all databases
    """
    client = get_client()
    databases = client.list_database_names()
    return Response(databases)


@api_view(['GET'])
def database_detail(request, pk):
    """
    Show full collections in current database
    """
    client = get_client()

    # Get list of collections
    collections = client[pk].list_collection_names()
    return Response(collections)


@api_view(['GET'])
def collection_detail(request, database, collection):
    """
    Show collection in
    """
    client = get_client()

    # Get list of collections
    data = client[database][collection].find({})

    return Response(parse_json(list(data)))


@api_view(['GET'])
def collection_detail_filter(request, database, collection):
    """
    Show collection in with filters
    """
    client = get_client()

    parameters = request.GET.items()

    print(parameters)
    # Get list of collections
    data = client[database][collection].find(dict(parameters))

    return Response(parse_json(list(data)))


def parse_json(data):
    return json.loads(json_util.dumps(data))


@api_view(['POST'])
def add_to_collection(request, database, collection):
    """
    Add element(s) to current collection
    """
    client = get_client()

    # Get list of collections

    data=request.data

    cursor = client[database][collection]

    print(len(data))

    if len(data) == 1:
        cursor.insert_one(*data)
    
    if len(data) > 1:
        cursor.insert_many(data)

    return Response(parse_json(data))


@api_view(['PUT'])
def update_in_collection(request, database, collection, mode):
    """
    Update element(s) in current collection
    """
    client = get_client()

    # Get list of collections

    data=request.data

    find_data = data.pop(0)

    cursor = client[database][collection]

    data = {"$set": data[0]}

    if mode == "one":
        cursor.update_one(find_data, data)
    
    if mode == "many":
        cursor.update_many(find_data, data)

    return Response(parse_json(data))


@api_view(['DELETE'])
def delete_element(request, database, collection, mode):
    """
    Delete element(s) from current collection
    """
    client = get_client()

    # Get list of collections

    parameters = request.GET.items()

    print(dict(parameters))

    data=request.data

    cursor = client[database][collection]

    if mode == "one":
        cursor.delete_one(dict(parameters))
    
    if mode == "many":
        cursor.delete_many(dict(parameters))

    return Response(parse_json(data))
