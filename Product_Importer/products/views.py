from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import io, csv, pandas as pd
from .tasks import add
from .models import Products


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
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = Products(
                       name= row["name"],
                       sku= row['sku'],
                       description= row["description"]
                       )
            new_file.save()
        return Response({"result": "OK"})
