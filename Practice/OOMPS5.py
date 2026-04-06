class Product:
    def __init__(self,ProductName,Price,Quantity):
        self.ProductName=ProductName
        self.Price=Price
        self.Quantity=Quantity
    def stock(self):
        self.y="stock"
        self.z="not in stock"
        if self.Quantity<1:
            return self.z
        else:
            return self.y
    def TotalCost(self):
        self.tax=self.Price*0.133
        self.totalcost="Total Cost:",self.Price+self.tax
        return self.totalcost
    def Overview(self):
        return self.ProductName, self.totalcost
product=Product("Banana",3.99,1)
print(product.stock())
print(product.TotalCost())
print(product.Overview())

