from .models import Products
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def bulkCreateProducts(products):
    try:
        Products.objects.bulk_create(products)
        return True
    except Exception as e:
        logger.error("bulkCreateProducts@error")
        logger.error(e)
        return False
