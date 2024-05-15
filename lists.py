# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):

    if len(list_to_remove_elements) >= 6:
        del list_to_remove_elements [5]
        del list_to_remove_elements [4]
        del list_to_remove_elements [0]
    elif len(list_to_remove_elements) == 5:
        del list_to_remove_elements [4]
        del list_to_remove_elements [0]
    elif len(list_to_remove_elements)>=1:
        del list_to_remove_elements [0]
    
    return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements.append("Yellow")
    list_to_add_elements.insert(0,"Pink")


    return list_to_add_elements

def is_empty(list_to_check):

    if len(list_to_check)== 0:
        return True
    else:
        return False



def check_lists(list4, list5):

    if is_empty(list4) or is_empty(list5):
        return False
    else:
        if list4[2:3] == list5[2:3]:
            return True
        else:
            return False



def list_of_lists(lista):
    new_lista1 = lista[0][0:2]
    new_lista2 = lista[1][1:4]
    new_lista3 = lista[2][-2:]
    lista_externa = [new_lista1, new_lista2, new_lista3]
    return lista_externa
