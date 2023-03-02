from admin import admin
class Operations:
    food_list =[]
    def __init__(self):
        self.n = 1

    def add_new_food(self):
        name =input("Enter your food name : ")
        qunatity = input("Enter your food quantity : ")
        price = float(input("Enter your food price : "))
        discount = input("Enter your food discount : ")
        stock = int(input("No. of stock available : "))
        ID = f"ABC00{self.n}"
        self.n+=1
        admin_obj = admin(Food_id=ID,Food_name=name,Food_quantity=qunatity,Food_price=price,Food_discount=discount,Food_stock=stock)
        self.food_list.append(admin_obj)
        return admin_obj
    
    def viewmenu(self):
        for i in self.food_list:
            print(i,"\n")
            
    def editfoodBy_ID(self):
        id_ = input("Enter food id to edit : ")
        for food in self.food_list:
            if food.get_food_ID() == id_:
                edit_name = input("Enter new food name : ")
                edit_quantity = input("Enter updated food quantity : ")
                edit_price = input("Enter the updated food price : ")
                edit_discount = input("Enter the updated discount : ")
                edit_stock = input("Enter updated stock : ")
                food.set_food_Name(edit_name)
                food.set_food_quantity(edit_quantity)
                food.set_food_price(edit_price)
                food.set_food_discount(edit_discount)
                food.set_food_stock(edit_stock)
                return self.food_list
        else:
            print("invalid id!")

    def removeBy_ID(self):
        id_ = input("Enter food id to edit : ")
        for food in self.food_list:
            if food.get_food_ID() == id_:
                self.food_list.remove(food)
                return self.food_list
        else:
            print("invalid id!")






operations_obj = Operations()
operations_obj.add_new_food()
operations_obj.viewmenu()