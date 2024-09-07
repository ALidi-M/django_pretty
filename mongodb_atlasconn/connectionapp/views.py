

from django.core.paginator import Paginator
from django.shortcuts import render
from bson import ObjectId
from .mongodb import mongo_db

# def mongo_test_view(request):
#     # Access the MongoDB database from the settings file
#     # db = settings.mongo_db  # Ensure this points to the actual database object, not just the name
    
#     # If db is correctly assigned, the following line should work without error
#     collection = mongo_db['SampleCollection']

#     # Example: Inserting a document into the collection
#     document = {"name": "Test", "value": 123}
#     result = collection.insert_one(document)

#     # print(type(db))
    
#     return HttpResponse(f"Inserted document ID: {result.inserted_id}")




def mongo_test_view(request):
    # Access the 'listingsAndReviews' collection in the 'sample_airbnb' database
    collection = mongo_db['listingsAndReviews']
    
    # Fetch all documents from the collection
    documents = list(collection.find({}))

    # Filter out blanks
    def is_blank(document):
        # Check if all values in the document are either empty strings or None
        return all(value in (None, '', []) for value in document.values())

    documents = [doc for doc in documents if not is_blank(doc)]

    # Convert BSON ObjectId to string for rendering
    for document in documents:
        for key, value in document.items():
            if isinstance(value, ObjectId):
                document[key] = str(value)

    # Paginating db documents
    paginator = Paginator(documents, 5) 
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)

    # Pass paginated documents to the template
    return render(request, 'myapps/index.html', {'page_obj': page_obj})
