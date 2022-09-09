import json
import azure.functions as func
from src import mercadolibre_api as ml_api

def main(req: func.HttpRequest) -> func.HttpResponse:

    category_id = req.params.get('category_id')
    data = []
    # Create a session for mercadolibre api
    session = ml_api.create_session()
    # Get categories from mercadolibre (site MX)
    site_id = 'MLM'
    categories = ml_api.get_categories(site_id, session)

    for c in categories:
        if c['id'] == category_id:
            category_name = c['name']
            try:
                res_items_by_category = ml_api.get_highlights_by_category(category_id, session)
                best_items_by_category = res_items_by_category['content']

                for item in best_items_by_category:
                    try:
                        item_data = ml_api.get_item(item['id'], session)
                        data.append({
                            'category_id': category_id,
                            'category': category_name,
                            'item_id': item['id'],
                            'position': item['position'],
                            'title': item_data['title'],
                            'price': item_data['price']
                        })
                    except:
                        print("An exception occurred")
            except:
                print("An exception occurred")
            break
    
    return func.HttpResponse(
        mimetype="application/json",
        body= json.dumps(data),
        status_code=200
    )
