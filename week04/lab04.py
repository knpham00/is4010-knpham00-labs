def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    common = set1.intersection(set2)

    return list(common) 

def find_user_by_name(users, name):

    user_lookup = {user['name']: user for user in users}
    
    return user_lookup.get(name)

def get_list_of_even_numbers(numbers):
   
    even_numbers = [n for n in numbers if n % 2 == 0]
    
    return even_numbers