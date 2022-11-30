from kipcon.kipdb.database_actions import *


if __name__ == "__main__":
    """@add_client
    def test(x):
        return x

    @add_client2
    def test2(x):
        return x

    @add_client3(f = 52)
    def test3():
        print(81)
    
    print(test(2))
    print(test2()) # 3

    @addx(x = 200)
    def calc(y): # xy
        return y    

    print(calc)"""
    # PRACTICE

    @const_folders(column = "main_folder_name")
    def update(value = "main2"):
        return value

    print(update)