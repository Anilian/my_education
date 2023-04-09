import sys

def get_data_from_terminal():
    items_length, bag = [int(i) for i in input().split()]
    items = []

    for i in range(0, items_length):
        items.append([int(i) for i in input().split()])
    assert len(items) == items_length
    return items_length, bag, items

def sorting_capacity(items):
    #вычислили удельную стоимость
    order = [(v / w,w) for v,w in items]
    order.sort(reverse=True)
    return(order)
    #unit_cost = []
    #for i in range(len(items)+1):
        #unit_cost.append((items[i])[0]/(items[i])[1])
    #print('unit_cost', unit_cost)
    
    #отсортировали
    #sorted_dict = []
    #sorted_keys = sort(unit_cost, reverse=True)
    #for w in sorted_keys:
       #sorted_dict[w] = unit_cost[w]
    #print('sorted_dict: ', sorted_dict)
    #print('\n')
    #return(sorted_dict)
def algoritm(items_length, bag, sorted_dict):
        
    total_price = 0
    for i in range(0,items_length):
        
        #print('удельный вес', sorted_dict[0])
        #print('вес этого предмета целиком', sorted_dict[1])
        #print('цена на весь объект',sorted_dict[0]* sorted_dict[1])
        unit_cost = (sorted_dict[i])[0]
        w = (sorted_dict[i])[1]
        #print(w)
        
        if bag > 0:
            #print('место до заполнения',bag)
            if w > bag: #если места уже недостаточно для всего объема
                
                #print('-----добавляем остатки предмета {}-----'.format(i))
                
    
                total_price = total_price + unit_cost * bag
                bag = 0
                #print('остатки total_price',total_price)
                #print('\n')
            else: #если места достаточно
                #print('------для внесения объекта по степени уменьшения {}-----'.format(i))
                
                total_price = total_price + unit_cost * w
                #print('total_price',total_price)
                bag = bag - w
                #print('осталось места',bag)
                #print('\n')
                
    return total_price

def main():
    #получили значения с терминала
    items_length, bag, items = get_data_from_terminal()
    #print('items_length: ', items_length)
    #print('bag: ', bag)
    #print('items:{}\n'.format(items))
    
    #вычислили удельную стоимость и отсотировали 
    sorted_dict = sorting_capacity(items)
    #print(sorted_dict)
    total_price = algoritm(items_length, bag, sorted_dict)

    print("{:.3f}".format(total_price))
    
if __name__ == "__main__":
    main()
