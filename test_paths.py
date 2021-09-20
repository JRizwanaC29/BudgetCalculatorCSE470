import p_list

x1 = "./components/ExpenseForm"
x2 = "./components/ExpenseList"

def test_path_1():
    if p_list.p1 == x1:
        print("Test 1 : ok!")

    else:
        print("Test 1 : Wrong!")

def test_path_2():
    if p_list.p2 == x2:
        print("Test 2 : ok!")
    
    else:
        print("Test 2 : Wrong!")

def test_path_3():
    if p_list.p1 == x2:
        print("Test 3 : ok!")
    
    else:
        print("Test 3 : Wrong!")

def test_path_4():
    if p_list.p2 == x1:
        print("Test 4 : ok!")
    
    else:
        print("Test 4 : Wrong!")

def main():
    test_path_1()
    test_path_2()
    test_path_3()
    test_path_4()

main()