

def total_price_wo_tax(items):
    total = 0
    for price in items.values():
        total += price['get_price']
    return float(total)

def total_price_w_tax(items):
    total = 0
    for price in items.values():
        total += price['get_price']
    
    total_orginal = total
    tax_amount = total_orginal * 0.05
    total = total + tax_amount 
    return total



def tax(items):
    total = 0
    print(items)
    for price in items.values():
        print(price['get_price']) 
        total += price['get_price']        
    tax_amount = total * 0.05
    return tax_amount


