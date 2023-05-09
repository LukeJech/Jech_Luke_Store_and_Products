class Store: 
    def __init__(self,info):
        self.name = info["name"]
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        print("You just sold a...")
        self.products.pop(id).print_info()

    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_discount, False)



class Product:
    def __init__(self,info):
        self.name = info["name"]
        self.price = info["price"]
        self.category = info["category"]

    def print_info(self):
        print(f"""
        product name: {self.name}
        category: {self.category}
        price: {self.price}""")
        return self
    
    def update_price(self, percent_changed, is_increased):
    
        if not is_increased: percent_changed *= -1
        # increase or decrease price based on percentage and round it to the nearest cent
        self.price = round(self.price +(self.price * percent_changed),2)
        return self



walle_mart_info = {
    "name": "WallE-Mart"
}

theo_chocolate_info = {
    "name": "75% Sea Salt Dark Chocolate",
    "price" : 4,
    "category" : "desserts"
}

cardboard_pizza_info = {
    "name": "Dijornos",
    "price" : 11,
    "category" : "freezer food"
}

walle_mart = Store(walle_mart_info)
theo_chocolate = Product(theo_chocolate_info)
cardboard_pizza = Product(cardboard_pizza_info)

walle_mart.add_product(theo_chocolate)
walle_mart.add_product(cardboard_pizza)

walle_mart.inflation(1)
walle_mart.products[0].print_info(), walle_mart.products[1].print_info()

walle_mart.set_clearance("desserts", .30)
walle_mart.products[0].print_info(), walle_mart.products[1].print_info()