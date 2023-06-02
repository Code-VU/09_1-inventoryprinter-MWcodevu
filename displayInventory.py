stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    t = 0
    print("Inventory:")
    for k,v in inventory.items():
        print(v,k)
        t = t+v
    print(f"Total number of items: {t}")       













if __name__ == "__main__":
    displayInventory(stuff)
