

class Order():
    def __init__(self) -> None:
        self._items = []
        self._total = None
        
    def get_items(self):
        return self._items
    
    def calculate_price(self):
        self._total = sum([item.price * item.quantity for item in self._items])
    
    def get_total(self):
        if self._total == None:
            self.calculate_price()
        return self._total
        
    def add_item(self, item):
        self._items.append(item)
        
    def includes_main_course(self):
        for item in self._items:
            if isinstance(item, MainCourse):
                return True
        
    def includes_beverage(self):
        for item in self._items:
            if isinstance(item, Beverage):
                return True
   
    def print_bill(self):
        print("Su cuenta es: ")
        for item in self._items:
            print(f"{item.name} - {item.price} - {item.quantity}")
        discount = 0
        items_for_discount = " no llevar ningun producto que aplique para descuento"
        if self.includes_main_course() and self.get_total() > 25000 and self.get_total()  < 50000:
            discount= 0.1* self.get_total()
            items_for_discount = "llevar algún plato principal y más de 25000 pesos en compras"
            
        elif self. includes_main_course and self.includes_beverage():
            items_for_discount = "llevar algún plato principal y alguna bebida"
            discount = 0.05 * self.get_total()
            
        elif self.get_total() > 50000:
            items_for_discount = "llevar más de 50000 pesos en compras"
            discount = 0.2 * self.get_total()
        
        self._total -= discount
        print(f"Total a pagar: {self._total}, con un descuento aplicado de {discount} pesos por {items_for_discount}")


class MenuItem():
    def __init__(self, price, name, quantity) -> None:
        self.price = price
        self.name = name
        self.quantity = quantity
        
    

class Beverage(MenuItem):
    def __init__(self, price, size, name, quantity) -> None:
        super().__init__(price, name, quantity)
        self._size = size
        
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        self._size = size

class Appetizer(MenuItem):
    def __init__(self, price, customers, name, quantity) -> None:
        super().__init__(price, name, quantity)
        self._customers = customers
        
    def get_customers(self):
        return self._customers
    
    def set_customers(self, customers):
        self._customers = customers

class MainCourse(MenuItem):
    def __init__(self, price, grammage, name, quantity) -> None:
        super().__init__(price, name, quantity)
        self._grammage = grammage
        
    def get_grammage(self):
        return self._grammage
    
    def set_grammage(self, grammage):
        self._grammage = grammage
    
class PaymentMeans():
    def __init__(self):
        pass
    
    def pay(self, amount):
        pass
    
class Card(PaymentMeans):
    def __init__(self, number, cvv):
        super().__init__()
        self._number = number
        self._cvv = cvv
    
    def pay(self, amount):
        print(f"Se han pagado {amount} pesos con la tarjeta {self._number}")
        
class Cash(PaymentMeans):
    def __init__(self, amount_payed):
        super().__init__()
        self._amount_payed = amount_payed
    
    def pay(self, amount):
        if self._amount_payed >= amount:
            print(f"Pago realizado en efectivo, cambio: {self._amount_payed - amount} pesos")
        
        else:
            print(f"El monto pagado no es suficiente, faltan {amount - self._amount_payed} pesos")

order = Order()

selection = input("¿Desea ordenar un plato principal? (s/n): ")
if selection == "s":
    print("""Platos principales:
    1. Hamburguesa sencilla
    2. Hamburguesa doble
    3. Hamburguesa ranchera
    4. Hamburguesa vegetariana
    """)
    main_course = int(input("Seleccione una opción: "))
    if main_course == 1:
        print("Hamburguesa sencilla seleccionada")
        order.add_item(MainCourse(12000, 150, "Hamburguesa sencilla", int(input("Cantidad: "))))
    elif main_course == 2:
        print("Hamburguesa doble seleccionado")
        order.add_item(MainCourse(16000, 300, "Hamburguesa doble", int(input("Cantidad: "))))
    elif main_course == 3:
        print("Hamburguesa ranchera seleccionada")
        order.add_item(MainCourse(20000, 200, "Hamburguesa ranchera", int(input("Cantidad: "))))
    elif main_course == 4:
        print("Hamburguesa vegetariana seleccionada")
        order.add_item(MainCourse(18000, 200, "Hamburguesa vegetariana", int(input("Cantidad: "))))


selection = input("¿Desea ordenar una entrada? (s/n): ")
if selection == "s":
    print("""Entradas:
    1. Canasta de pan (3 personas)
    2. Sopa (1 persona)
    3. Papas fritas (5 personas)
    """)
    appetizer = int(input("Seleccione una opción: "))
    if appetizer == 1:
        print("Canasta de pan seleccionada")
        order.add_item(Appetizer(4000, 3, "Canasta de pan", int(input("Cantidad: "))))
    elif appetizer == 2:
        print("Sopa seleccionada")
        order.add_item(Appetizer(6000, 1, "Sopa", int(input("Cantidad: "))))
    elif appetizer == 3:
        print("Papas fritas seleccionadas")
        order.add_item(Appetizer(8000, 5, "Papas fritas", int(input("Cantidad: "))))


selection = input("¿Desea ordenar una bebida? (s/n): ")
if selection == "s":
    print("""Bebidas:
    1. Agua
    2. Refresco
    3. Jugo
    """)
    beverage = int(input("Seleccione una opción: "))
    if beverage == 1:
        print("Agua seleccionada")
        order.add_item(Beverage(2000, 500, "Agua", int(input("Cantidad: "))))
    elif beverage == 2:
        print("Refresco seleccionado")
        order.add_item(Beverage(3000, 500, "Refresco", int(input("Cantidad: "))))
    elif beverage == 3:
        print("Jugo seleccionado")
        order.add_item(Beverage(5000, 600, "Jugo", int(input("Cantidad: "))))

order.calculate_price()


order.print_bill()

card_number = "123581321"
cvv = "161"

while True:
    selection = input("¿Desea pagar con tarjeta? (s/n): ")
    if selection == "s":
        card = Card(card_number, cvv)
        card.pay(order.get_total())
        break
    elif selection == "n":
        cash = Cash(int(input("Ingrese el monto a pagar: ")))
        cash.pay(order.get_total())
        break
    else:
        print("Opción no válida")
    
    



