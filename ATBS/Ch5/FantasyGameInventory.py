

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        print(str(v) +' ' + str(k))
        item_total += v
    print("Total number of items: " +str(item_total))


def addToInventory(inventory, addedItems):
    for item in addedItems:
        aux = inventory.setdefault(item, 1)
        if aux != 1:
            inventory[item] += 1

    return inventory

#############################################################################

inv  = {'rope': 1, 'gold coin': 42}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)
