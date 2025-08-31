class Shoping:
    def __init__(self,name):
        self.name=name
        self.customers=[]
        self.sellers=[]
    
    def add_customer(self,customer):
        self.customers.append(customer)

    def add_seller(self,seller):
        self.sellers.append(seller)

    def login_customer(self,email,passward):
        for customer in self.customers:
            if customer.email==email and customer.passward==passward:
                return True
        return False
    
    def login_seller(self,email,passward):
        for seller in self.sellers:
            if seller.email==email and seller.passward==passward:
                return True
        return False
    
    def view_product(self):
        for seller in self.sellers:
            seller.show_stock()

class User:
    def __init__(self,email,passward):
        self.email=email
        self.passward=passward

class Customer(User):
    def __init__(self, email, passward):
        super().__init__(email, passward)

class Seller(User):
    def __init__(self, email, passward):
        super().__init__(email, passward)
        self.stock=[]

    def add_stock(self,product):
        self.stock.append(product)

    def show_stock(self):
        print(f"Seller email : {self.email}")
        if self.stock:
            print("***** STOCK *****")
            print("Name\tQuantity")
            for product in self.stock:
                print(f"{product.name}\t{product.quantity}")
        else:
            print("Stock out!!")

class Product:
    def __init__(self,name,quantity):
        self.name=name
        self.quantity=quantity


#create shoping
daraz=Shoping("Daraz")
#create seller
s1=Seller("s1@gmail.com","S001")
s2=Seller("s2@gmail.com","S002")
s3=Seller("s3@gmail.com","S003")
#add seller to shopping app
daraz.add_seller(s1)
daraz.add_seller(s2)
daraz.add_seller(s3)
#create customer
c1=Customer("c1@gmail.com","C001")
c2=Customer("c2@gmail.com","C002")
c3=Customer("c3@gmail.com","C003")
c4=Customer("c4@gmail.com","C004")
c5=Customer("c5@gmail.com","C005")
c6=Customer("c6@gmail.com","C006")
#add customer to shopping app
daraz.add_customer(c1)
daraz.add_customer(c2)
daraz.add_customer(c3)
daraz.add_customer(c4)
daraz.add_customer(c5)
daraz.add_customer(c6)

#create products
p1=Product("Mobile",100)
p2=Product("Mobile",200)
p3=Product("Laptop",10)
p4=Product("Laptop",50)
p5=Product("Ball",300)
p6=Product("Ball",500)
p7=Product("Bottle",1000)
p8=Product("Book",30)
#add product to seller stock
s1.add_stock(p1)
s1.add_stock(p3)
s1.add_stock(p5)
s1.add_stock(p7)
s1.add_stock(p8)

s2.add_stock(p2)
s2.add_stock(p4)
s2.add_stock(p6)


daraz.view_product()


