import sys
import time

def starting_app() :
    f = open('start.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    f = open('help.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()


def input_listener():
    """Listen and prepare the user's entry for processing"""

    entry = input(">>>>? ")
    entry = entry.split(sep='(')
    function = entry[0]
    params = []
    if function not in ['exit', 'dork', 'import']:
        print("      Bad entry. Please check your query.")
    else :
        if (len(entry) >= 2):
            if function == "dork" :
                params_tmp = entry[1].split(')')[0].split(sep=',')
                params = [param for param in params_tmp if param in ["country","region","city","ip","url_name","short_url","url"] ]

    return function,params


