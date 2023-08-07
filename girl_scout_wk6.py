
cont = ''
order_total = 0
item_cnt = 0
qty_total = 0
box_qty = 12
box_cnt = 0
total_boxes = 0

print('Welcome to the GSC Program')
while True:
    name = input('What is your name?\n')
    if len(name) < 1 or len(name) > 20:
        print('name must be between 1 and 20 characters')
    else:
        break
    
cont = input(f'Hello {name}, would you like to order some cookies?> (y/n)\n')

print(f"Cookie Order for {name}\n")

while cont.lower() == 'y':
    
    print('Welcome!')
    print('Please Choose a Flavor')
    print('1. Savannah')
    print('2. Thin Mintz')
    print('3. Tagalongs')    
    
    while True:
        item  = int(input('Please enter the cookie flavor:\n'))
        if item == 1:
            price = 3.5
            box_price = 42
            break
        if item == 2:
            price = 3.5
            box_price = 42
            break
        if item == 3:
            price = 5.0
            box_price = 60
            break
        else:
            print('Please enter either 1,2 or 3')
            
            
    while True:
        try:
            box_qty = int(input('how many boxes would you like?:\n'))
        except ValueError:
            print('Error: value must be an integer between 1 and 5')
        except Exception as detail:
            print('Error:',detail)
        else:
            if box_qty >= 1 and box_qty <= 5 :
                total_boxes += box_qty
                break
            if box_qty < 0:
                print('value cannot be a negative number')
                continue
            
    while True:
        try:
            qty = int(input("How many individual cookies would you like?:\n"))
        except ValueError:
            print('Error: value must be an integer between 1 and 10')
        except Exception as detail:
            print('Error:',detail) 
        else:    
            if qty < 1 or qty > 10:
                print('Error: enter a value between 1 and 10:')
                continue
            else:
                break
            

    total_box_price = box_price * box_qty
    total = (price * qty) + total_box_price
    
    
    # accumulators
    order_total += total
    item_cnt += 1
    qty_total += qty
    total_boxes += box_qty
    # print detail information
    if item == 1:
        print("Count | Flavor | Price | Qty | Total")
        print(f"  {item_cnt}  |  Savannah | {price}  |  {qty}  |  ${total} (includes {box_qty} box(es))\n")
    if item == 2:
        print("Count | Flavor | Price | Qty | Total")
        print(f"  {item_cnt}  |  Thin Mintz | {price}  |  {qty}  |  ${total} (includes {box_qty} box(es))\n")
    if item == 3:
        print("Count | Flavor | Price | Qty | Total")
        print(f"  {item_cnt}  |  Tagalongs | {price}  |  {qty}  |  ${total} (includes {box_qty} box(es))\n")
    
    cont = ''
    while cont.lower() != 'y' and cont.lower() != 'n':
        cont = input('Would you like to add another item?> (y/n)\n')

print(f'Order summary for {name}\n')

print(f'Total Flavors: {item_cnt}\n')
print(f'Total cookies: {qty_total}\n')
print(f'Total Boxes: {total_boxes}\n')
print(f'Your Total is ${order_total}')
print('Thank You!')
