from abc import ABC

from Products import Products


class ShoppingCart(Products, ABC):

    def __init__(self):
        self.products = []
        self.product = Products()

    def addproduct(self, product):
        self.products.append(product)

    def getproduct(self):
        return self.products

    def removeproduct(self, product):
        self.products.remove(product)

    def getsubtotal(self, product):
        return self.product.get_price() * product.get_quantity()

    def gettotalamount(self):
        total = 0
        for product in self.getproduct():
            total += self.getsubtotal(product)
        return total

    def isitemavailable(self, item):
        stock = 8
        pass


if __name__ == '__main__':
    obj = ShoppingCart()
