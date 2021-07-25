# python programming code for shopping cart

#Shopping cart Application with qt
import sys
import os




class ShoppingCart:

    # creating cart
    def __init__(self, cart_list, item_prices):
        #cart list is of type dictionary
        self._cartList = cart_list
        self._itemPrices = item_prices

    
    def addToCart(self):

        print('Enter numer of new items you want to add: ')
        count = int(input())

        i=0
        while i in range(0, count):
            item_name = input()
        
            if item_name not in self._cartList:
                item_qty = float(input())
                self._cartList[item_name] = item_qty
                i += 1
            else:
                print('Item already exists')


        


    
    def deleteItem(self):
        print('Enter item name you want to delete: ')
        item_name = input()

        if item_name in self._cartList.keys():
        #pop returns None when the key specified is not found
            self._cartList.pop(item_name, None)

        else:
            print('This item does not exist')
            print()


    def calculateTotalPrice(self):
        cart_total = 0

        for item_k, qty_v in self._cartList.items():
            for item_k, item_v in self._itemPrices.items():
                cart_total += qty_v * item_v

        print()
        #display final list and total amount
        print('Cart list: ')
        self.displayItems()

        print('Total amount: ', cart_total)

        #amount including gst, 18% on fruits
        print('Total amount including GST: ', float( cart_total + (cart_total * 0.18) ) )
        print()

    def updateCart(self):
        #calls delete and add items from here

        #do you want to delete some item or add a new item?
        print('Do you want to delete some item or add or update quantity of an item?')
        print('Enter d for delete, a for adding an item and u for updating: ')

        update_choice = input()

        #if user selects correct option
        if update_choice == 'd' or update_choice == 'D':
            self.deleteItem()

        
        elif update_choice == 'a' or update_choice == 'A':
            self.addToCart()

        #if user selects incorrect option for updation
        elif update_choice == 'u' or update_choice == 'U':


            print('Enter numer of new items you want to update: ')
            count = int(input())

            i=0
            while i in range(0, count):
                print('Enter name of the item and updated quantity: ')
                item_name = input()
                

                if item_name in self._cartList.keys():
                    item_qty = int(input())
                    self._cartList[item_name] = item_qty
                    i += 1
                else:
                    print('Item not entered in the list')



    def displayItems(self):
        
        for k,v in self._cartList.items():
            print(k,'    ',v)
        print()#display purposes
        


def main():


    cart_items = []

    #items available in the store and their corresponding price
    item_prices = {'Apple': 80, 
              'Orange': 40,
              'Strawberries': 50,
              'Blueberries': 50,
              'Banana': 40,
              'Watermelon': 40,
              'Papaya': 50}

    cart_total = 0

    #display items in the mart
    print('Items available in the mart: ')
    print('Item','\t\t','price/kg')
    
    for key, value in item_prices.items():
        print(key,'     ',value )
    

    #ask user to select items from mart to add to cart
    print('Enter numer of items you want: ')
    no_of_items = int(input())
    

    if no_of_items < 1:
        print('At least one item is required')


    else: #when at least one item given
        print('Enter details of ', no_of_items, 'item(s): ')
        print()#for display purposes

        #dictionary used for cart input
        input_list = dict()

        i = 0
        #customer will buy at least one item
        while i in range(0, no_of_items):
        
            print('Enter the item: ')
            item = input()

            #discard incorrect items those not avaialable in list
            if item not in item_prices.keys() or item in input_list.keys():
                print('Please select items from the mart or check not enter items already entered')
            

            else:
                print('Enter quantity in numerals: ')
                qty = float(input())
                input_list[item] = qty
                i += 1#next item can be entered


        #list generated now make an object
        shop_obj = ShoppingCart(input_list, item_prices)

            


        # display the list generated
        print()
        print('Generated cart list: ')
        shop_obj.displayItems()




        # ask if any changes needed
        print('Do you want to make any changes in the list?(y/n): ')
        update_choice = input()

    
        if update_choice == 'y' or update_choice == 'Y':
            #make changes if said yes or don't make changes 
            #and display the resulting list and total amount

            shop_obj.updateCart()
        

            #display total price, updated list printed as well
            shop_obj.calculateTotalPrice()


        else:

            #display total amount and cart list, updated list printed as well
            shop_obj.calculateTotalPrice()
        





if __name__ == '__main__': main()
    