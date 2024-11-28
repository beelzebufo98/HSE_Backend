class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
        self.sale = 0

    def edit_category(self, new_category):
        self.category = new_category

    def edit_price(self, new_price):
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.price = new_price

    def set_sale(self, sale):
        if sale < 0 or sale > 100:
            return  ValueError("Величина скидки должна находиться в диапазоне от 0 до 100")
        self.sale = sale
    def cancel_sale(self):
        self.sale = 0

    def get_price(self):
        return self.price * (1 - self.sale / 100)

    def __repr__(self):
        return f"Product(Name: '{self.name}', Category: '{self.category}', Price: {self.price:.2f})"
