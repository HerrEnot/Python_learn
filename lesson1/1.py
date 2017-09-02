def get_summ(one, two=3, delimeter=' '):
    return str(one).upper() + str(delimeter) + str(two)
print(get_summ('Hello', delimeter="_"))
