# Apiviews
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()    #by default it has get method
def hello_world_get(request):
    return Response({'msg': 'Hello World'})

# Function based apiviews
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == "GET":
        return Response({'msg': 'This is GET request'})
    if request.method == "POST":
        print(request.data)
        return Response({'msg': 'This is POST request'})
    
