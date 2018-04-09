'''Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory 
(like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should return a dictionary
 that represents the updated inventory. Note that the addedItems list can contain multiples of the same item.'''



# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for k, v in inventory.items():
		# FILL IN THE CODE HERE
		print(v," ",k)
		item_total += v
	print("Total number of items: " + str(item_total))
	
displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    # your code goes here
	for i in addedItems:
		inventory.setdefault(i, 0)
		inventory[i] = inventory[i] + 1
	return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)