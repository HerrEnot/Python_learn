


def find_name(name):
   mylist =["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
   while mylist:
        a = mylist.pop(0)
        if name == a:
            return "username founded"
   return "nothitng"

b=input("введите искомое имя: ")
print(find_name(b))