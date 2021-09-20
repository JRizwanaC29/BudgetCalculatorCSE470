import p_list

test = "Users\Desktop\BUDget\BUDGet\model\sth"
test_chk = "Users\Documents\BUDget\BUDGet\model"
def model_tst():
    if p_list.model == test:
        print("Test For Model: OK!")
    else:
        print("Test For Model: Wrong Path!")

def model_tst_2():
    if p_list.model == test_chk:
        print("Test For Model: OK!")
    else:
        print("Test For Model: Wrong Path!")


def main():
    model_tst()
    model_tst_2()

main()