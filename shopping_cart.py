import statistics as st

class ShoppingCart:
    def __init__(self, employee_discount = None):
        self._total = 0
        self._items = []
        self._employee_discount = employee_discount

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total += value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, item):
        self._items.append(item)

    @property
    def employee_discount(self):
        return self._employee_discount

    @employee_discount.setter
    def employee_discount(self, number):
        employee_discount = number

    def add_item(self, item, price, quantity = 1):
        new_item = dict(name = item, price = price, quantity = quantity)
        self._total += round((new_item['price']*new_item['quantity']), 2)
        self._items.append(new_item)

    def mean_item_price(self):
        quantity = 0
        for item in self._items:
            quantity += item['quantity']
        return round(self._total/quantity, 2)

    def median_item_price(self):
        prices = list(map(lambda item: item['price'], self._items))
        return st.median(prices)

    def apply_discount(self):
        if self._employee_discount:
            self._total = self._total*(1 - self._employee_discount/100)
            return self._total
        return "Sorry, there is not discount for you!!!"

    def item_names(self):
        item_list = []
        for item in self._items:
            for i in range(item['quantity']):
                item_list.append(item['name'])
        return item_list

    def void_last_item(self):
        if not self._items:
            return "There are no items in your cart"
        else:
            voided_item = self._items.pop()
            self._total -= round((voided_item['price']*voided_item['quantity']), 2)

discount_shopping_cart = ShoppingCart(20)
shopping_cart = ShoppingCart()
