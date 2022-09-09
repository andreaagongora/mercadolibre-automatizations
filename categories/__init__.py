import logging
import json
from src import mercadolibre_api as ml_api

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:

    category_id = req.params.get('name')

    # Create a session for mercadolibre api
    session = ml_api.create_session()
    # Get categories from mercadolibre (site MX)
    site_id = 'MLM'
    categories = ml_api.get_categories(site_id, session)

    return func.HttpResponse(
        mimetype="application/json",
        body= json.dumps(categories),
        status_code=200
    )
