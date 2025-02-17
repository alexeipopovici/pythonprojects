class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return "The name for the menu is : " + self.name + "\nMenu is available between : " + self.start_time + " and " + self.end_time
  def calculate_bill(self, purchased_items):
    calculate_bill = 0
    for item in purchased_items:
      calculate_bill += self.items.get(item, 0)
    return calculate_bill

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return "The adress of the restaurant is : " + self.address
  def available_menus(self, time):
    self.time = time
    available_menus = []
    for menu in self.menus:
      if str(menu.start_time) <= str(self.time) <= str(menu.end_time):
        available_menus.append(menu)
    return available_menus

class Business:
  def __init__(self, name, franchises):
    self.name = name
    franchises = []


brunch = Menu("brunch",{'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50},"11am","4pm")
early_bird = Menu("early bird",{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, "3pm", "6pm")
dinner = Menu("dinner",{'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, "5pm" , "11pm")
kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00} , "11am","9pm")

print(brunch)
breakfast_order = ['pancakes', 'home fries' , 'coffee']
total_bill = brunch.calculate_bill(breakfast_order)
print(total_bill)
early_bird_order = ['salumeria plate' , 'mushroom ravioli (vegan)']
total_bill1 = early_bird.calculate_bill(early_bird_order)
print(total_bill1)

flagship_store = Franchise("1232 West End Road",[brunch,early_bird,dinner,kids])
new_installment = Franchise("12 East Mulberry Street",[brunch,early_bird,dinner,kids])
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(5))

first_business = Business("Basta Fazoolin' with my Heart", [flagship_store , new_installment])
arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_place = Franchise("189 Fitzgeral Avenue", arepas_menu)

new_business = Business("Take a'Arepa", arepas_place)
