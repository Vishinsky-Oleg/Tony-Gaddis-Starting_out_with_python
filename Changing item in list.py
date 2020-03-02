

def listw():
    food = ['Hamburger', 'Hot Dog', 'Shaverma']
    print('That\'s what we got: ')
    print(food)
    item = input('Element that got to be changed: ')
    try:
        item_index = food.index(item)
        new_item = input('New item: ')
        food[item_index] = new_item
        print('New list:')
        print(food)
    except:
        print('Item doesn\'t found')


listw()