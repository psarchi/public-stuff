a = [1,3, 8, 6]
b = [2, 7, 4, 9, 5]

def list_append(l,element):
    element = [element]
    return l + element

def list_remove(l,element):
    _l = []
    for item in l:
        if element == item:
            pass
        else:
            _l = list_append(_l,item)
    return _l

def is_element_lowest(element,c):
    lowest = element
    for item in c:
        if element > item:
            lowest = item
    if element is lowest:
        return True
    return False


def list_manipulation(c,d):
    for element in c:
        if is_element_lowest(element,c):
            d = list_append(d,element)
            c = list_remove(c,element)
            break
    return c , d
        
    
def main(a,b):
    c = a + b
    d = []
    while c:
        c , d = list_manipulation(c,d)
    return d


print(main(a,b))