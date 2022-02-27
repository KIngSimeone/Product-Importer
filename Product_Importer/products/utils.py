from .models import Products
from config.celery import app

# import the logging library
import logging
import pandas as pd

# Get an instance of a logger
logger = logging.getLogger(__name__)

@app.task()
def bulkCreateProducts(file):
    try:
        products = []
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = Products(
                       name= row["name"],
                       sku= row['sku'],
                       description= row["description"]
                       )
            products.append(new_file)
        Products.objects.bulk_create(products)
        return True
    except Exception as e:
        logger.error("bulkCreateProducts@error")
        logger.error(e)
        return False
