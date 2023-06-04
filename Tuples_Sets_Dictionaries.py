print('task1')
def get_budgets(lst_budgets):
    return sum([user['budget'] for user in lst_budgets])
print(get_budgets([
        {"name": "Anna", "age": 25, "budget": 51654},
        {"name": "Iara", "age": 31, "budget": 45871},
        {"name": "Lukash", "age": 27, "budget": 69472}
    ]))
print('task2')
def get_student_names(dict_names):
    return sorted(dict_names.values())

print(get_student_names({
  "Student 1" : "Lukash",
  "Student 2" : "Mariia",
  "Student 3" : "Den"
}))

print('task3')
def identical_filter(words):
    new_list = []
    for word in words:
        word_set = set(word)
        if len(word_set) == 1:
            new_list.append(word)
    return new_list


print(identical_filter(["adfghj", "ccccc", "l", "tyue", "xxxxx"]))

print('task4')
def validate_subsets(subsets, one_set):
    one_set = set(one_set)
    for number in subsets:
        number_set = set(number)
        if not number_set.issubset(one_set):
            return False
    return True

print('task5')
def priority_sort(unsort_lst, pri_set):
    # Your code
    return

print('task6')
def len_longest_chain(chain_pairs):
    # Your code
    return

print('task7')
def color_invert(rgb):
    l = []
    for i in rgb:
        l.append(255 - i)
    return tuple(l)
print(color_invert(()))


print('task8')
def check(dict1, dict2, key_ch):
    if key_ch not in dict1 and key_ch not in dict2:
        return "Not found"
    elif key_ch not in dict1 or key_ch not in dict2:
        return "One's empty"
    elif dict1[key_ch] == dict2[key_ch]:
        return True
    else:
        return "Not the same"
dict_first = {"sky": "temple", "horde": "orcs", "people": 12, "story": "fine", "sun": "bright"}
dict_second = {"people": 12, "sun": "star", "book": "bad"}
print(check(dict_first, dict_second, "sun"))
