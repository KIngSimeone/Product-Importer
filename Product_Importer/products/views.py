from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import add
from .utils import bulkCreateProducts


@api_view(['GET', 'PUT', 'POST'])
def add_view(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        request_data = request.data
        x = request_data['x']
        y = request_data['y']

        result = add.delay(x,y)
        result = result.get()
        return Response({"result": result })

@api_view(['GET', 'PUT', 'POST'])
def upload(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        file = request.FILES.get('file')
        bulkCreateProducts.delay(file)
        return Response({"result": "OK"})
