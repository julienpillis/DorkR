import sys
import time

def starting_app() :
    f = open('start.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()

    print(">>>> (-_-)",end='')
    time.sleep(1)
    for i in range(3):
        print("z",end="")
        time.sleep(1)
    print("\n>>>> ＼(◎o◎)／！")
    time.sleep(1)
    print(">>>> Welcome on \033[91mDorkR\033[0m (^_^) ")
    time.sleep(1)
    print(">>>> Here the stuff you'll need for your ride : \n"
          "     \033[1mdork\033[0m(params) : scrap a dork \n"
          "     \033[1mimport\033[0m(query_file) : import your queries from a csv file \n"
          "     \033[1mexit\033[0m : exit DorkR \n"
          "     |--> Exhaustive list available on GitHub")
