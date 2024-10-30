"""
================ Marketing Program ================
"""

#================ Variables ================
interaction = """
Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
"""
input_action = 'Please enter an action: \n'

name_itens = []
valor_itens = []
amount_itens = []


#================ Functions ================
def shopping_actions(interaction):
    print(interaction)
    action = int(input(input_action))
    return action  # Retorna a ação escolhida
    
def shopping_view_cart():
    index = 0
    for index in range(len(name_itens)):
        print(f'{index + 1}. ({amount_itens[index]}) {name_itens[index]} - ${valor_itens[index]}')
    
    print()

def shopping():
    action = 0
    while action != 5:
        action = shopping_actions(interaction)
        
        # ADD ITEM
        if action == 1:

            item = input('What item would you like to add? ')
            item = item.title()
            
            valor = float(input(f"What is the price of {item}? "))
            valor = round(valor, 2)
            
            amount = int(input(f"how many items will be added? "))
            
            name_itens.append(item)
            valor_itens.append(valor)
            amount_itens.append(amount)
            
            
        
        # VIEW CART
        elif action == 2:
            shopping_view_cart()
            input('Press enter...')
            
                        
        
        # REMOVE ITEM
        elif action == 3:
            shopping_view_cart()
            
            item = int(input ('Which item would you like to remove (use the number of the item)?\n '))
            print()
            list_item = item - 1
            
            if amount_itens[list_item] > 1:
                while True:
                    amount = int(input (f'you have {amount_itens[list_item]} {name_itens[list_item]} in the cart. How many items do you want to delete? \n '))
                    print()
                    if amount < amount_itens[list_item]:
                        amount_itens[list_item] -= amount
                        print(f'Item(ns) success deleted \n')
                        break
                    
                    elif amount == amount_itens[list_item]:
                        name_itens.pop(list_item)
                        valor_itens.pop(list_item)
                        amount_itens.pop(list_item)
                        print(f'Item(ns) success deleted \n')
                        break

                    else:
                        print(f'Your choice is higuer than the itens in the cart. Please, chose a option lower or ecqual of the amount of the {name_itens[list_item]} \n')
            
            elif amount_itens[list_item] == 1:
                name_itens.pop(list_item)
                valor_itens.pop(list_item)
                amount_itens.pop(list_item)
                print(f'Item(ns) success deleted \n')

           
            
            
        
        # COMPUTE TOTAL
        elif action == 4:
            total_itens = sum(valor_itens)
            total_amount = sum(amount_itens)
            
            total = total_itens * total_amount
            print(f'The total price of items in your cart is: ${total:.2f}')

            print(f'Item(ns) success deleted \n')
                
        
        # QUIT
        elif action == 5:
            print('Quitting...')

        else:
            print('Invalid action. Please try again.')

# Inicia o programa
shopping()
