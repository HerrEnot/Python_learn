

def compare_s(first, second): 
 if first == second :
  return 1
 elif len(first) > len(second):
  return 2
 elif first != second and second == "python" :
  return 3
string1 = input(" введите первую строку: ") 
string2 = input(" введите вторую строку: ") 

print(compare_s(string1, string2))
