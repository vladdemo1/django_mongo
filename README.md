# Django Mongo Project

Basic methods for managing elements with remote mongo base using API.

## Getting Started

You can see the main commands for managing functions on the main page, which will be presented below.

## Main Page

Here you can access the main page
- [Page](http://127.0.0.1:8000/api/)

## Get Databases

The construct to get all existing databases is as follows

    /databases-list/

Here you can get a list of all databases
- [List of all databases](http://127.0.0.1:8000/api/databases-list/)

## Get Collections

The construct to get all existing collections in current database is as follows

    /database-detail/<str:database>/

In This construction, database is the name of the database from which you want to get the names of all existing collections

For example, we can get all the collections of the [django](http://127.0.0.1:8000/api/database-detail/django/) database

## Get Documents

The construct to get all existing documents in current database is as follows

    /collection-detail/<str:database>/<str:collection>/

In this construction:
- database - the name of the selected database
- collection - the name of the selected collection

For example, we can get documents from the django database by selecting a [collection with all users and administrators](http://127.0.0.1:8000/api/collection-detail/django/auth_user/)

## Get Documents with a Filter

The construct to get all existing documents in current database with a filter is as follows

    /collection-detail-filter/<str:database>/<str:collection>/?param=value

In this construction:
- database - the name of the selected database
- collection - the name of the selected collection
- param - the name of the parameter that will act as a search key
- value - parameter value

For example:

    ?name=Vlad&city=Kharkiv

Translate to JSON for NoSQL Filter as

    {"name": "Vlad", "city": "Kharkiv"}

For example, we can [get all documents](http://127.0.0.1:8000/api/collection-detail-filter/test/test/?name=Vlad&city=Kharkiv) from the 'test' database using the 'test' collection and a filter to find all elements that have 'name = Vlad' and 'city = Kharkiv'

## Adding one or many items to Collection

The construct for adding elements to current collection is as follows

    /add-to-collection/<str:database>/<str:collection>/

In this construction:
- database - the name of the selected database
- collection - the name of the selected collection

For examples of adding one or many elements, we will use the 'test' database and the 'test' collection

### Adding one element

To add one element, we will use [this link](http://127.0.0.1:8000/api/add-to-collection/test/test/) and the following construction:

    [
        {
            "name": "Jacque Fresco",
            "age": 101,
            "city": "New York"
        }
    ]

And then we can check the result by [this link](http://127.0.0.1:8000/api/collection-detail/test/test/)

### Adding many element

To add many elements, we will use [same link](http://127.0.0.1:8000/api/add-to-collection/test/test/) and the following construction:

    [
        {
            "car": "Dodge",
            "speed": 320,
            "city": "New York",
            "price": 79800
        },
        {
            "car": "Tesla",
            "speed": 280,
            "city": "New York",
            "price": 112000
        }
    ]

And then we can check the result by [this link](http://127.0.0.1:8000/api/collection-detail/test/test/)

## Update one or many items in Collection

The construct for update elements in current collection is as follows

    /update-in-collection/<str:database>/<str:collection>/<str:mode>/

In this construction:
- database - the name of the selected database
- collection - the name of the selected collection
- mode - mode selection when changing elements, you can choose [one](http://127.0.0.1:8000/api/update-in-collection/test/test/one/) or [many](http://127.0.0.1:8000/api/update-in-collection/test/test/many/).

For examples of update one or many elements, we will use the 'test' database and the 'test' collection

### Update one element

For update one element, we will use [this link](http://127.0.0.1:8000/api/update-in-collection/test/test/one/) and the following construction:

    [
        {
            "name": "Jacque Fresco"
        },
        {
            "city": "New York City"
        }
    ]

And then we can check the result by [this link](http://127.0.0.1:8000/api/collection-detail/test/test/)

### Update many elements

For update many elements, we will use [this link](http://127.0.0.1:8000/api/update-in-collection/test/test/many/) and the following construction:

    [
        {
            "city": "New York"
        },
        {
            "city": "Boston"
        }
    ]

And then we can check the result by [this link](http://127.0.0.1:8000/api/collection-detail/test/test/)

## Delete one or many items from Collection

The construct for delete elements from current collection is as follows

    /delete-element/<str:database>/<str:collection>/<str:mode>/?param=value

In this construction:
- database - the name of the selected database
- collection - the name of the selected collection
- mode - mode selection when delete elements, you can choose [one](http://127.0.0.1:8000/api/delete-element/test/test/one/) or [many](http://127.0.0.1:8000/api/delete-element/test/test/many/).
- param - the name of the parameter that will act as a search key
- value - parameter value

For example:

    ?name=Vlad&city=Kharkiv

Translate to JSON for NoSQL Filter as

    {"name": "Vlad", "city": "Kharkiv"}

For examples of delete one or many elements, we will use the 'test' database and the 'test' collection

### Delete one element

For delete one element, we will use [this link](http://127.0.0.1:8000/api/delete-element/test/test/one/?name=Jacque%20Fresco).

In [this link](http://127.0.0.1:8000/api/delete-element/test/test/one/?name=Jacque%20Fresco) we have parameters like this:

    ?name=Jacque%20Fresco

Translate to JSON for NoSQL Filter as

    {"name": "Jacque Fresco"}

And then we can check the result by [this link](http://127.0.0.1:8000/api/collection-detail/test/test/)

### Delete many elements

For delete many elements, we will use [this link](http://127.0.0.1:8000/api/delete-element/test/test/many/?city=Boston).

In [this link](http://127.0.0.1:8000/api/delete-element/test/test/many/?city=Boston) we have parameters like this:

    ?city=Boston

Translate to JSON for NoSQL Filter as

    {"city": "Boston"}

And then we can check the result by [this link](http://127.0.0.1:8000/api/collection-detail/test/test/)

## Conclusion

### Author

    Демченко Владислав

### Group

    555вМ1

### Programming language

    Python

### Used framework

    Django and DRF

### Database

    MongoDB - Atlas

### Mongo Engine for Django

    Djongo

### Package for Mongo Client in Python

    pymongo

### Connect to MongoDB

    By link