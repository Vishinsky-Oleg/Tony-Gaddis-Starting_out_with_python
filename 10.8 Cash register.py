import ob


item_1 = ob.RetailItem('Jacket', 12, 59.95)
item_2 = ob.RetailItem('Designer Jeans', 40, 34.95)
item_3 = ob.RetailItem('Shirt', 20, 24.95)


list1 = ob.CashRegister()
list1.purchase_item(item_1)
list1.purchase_item(item_2)
list1.purchase_item(item_3)
print(format(list1.get_total(), '.2f'))
list1.show_items()
list1.clear()
if list1.get_len() == 0:
    print("list is empty")
else:
    print(list1.get_len())

