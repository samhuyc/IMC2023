## This file is a test for python3



def should_buy(product, price, valuations):
    if product not in valuations:
        return False
    return valuations[product] > price


def mystery_box_value(products, valuations):
    box = {}
    for key in products:
        box[key] = products[key] * valuations[key]
    
    return box

def main():
    """
    valuations = {"apple": 5, "banana": 10, "coconut": 8}
    print(should_buy("apple", 10, valuations))
    """
    products = {'banana':200, 'shell':300, 'coconut':100}
    valuations = {'banana':8, 'shell':4, 'coconut':13}

    print(mystery_box_value(products,valuations))
    
main()