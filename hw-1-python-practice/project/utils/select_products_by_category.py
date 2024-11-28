def select_products_by_category(products, category):
     category_prod = []
     for product in products:
         if product.category == category:
             category_prod.append(product)
     return category_prod
