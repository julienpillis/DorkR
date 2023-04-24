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
          "     \033[1mdork\033[0m(params) : scrap a dork | params : (country,region,city,ip,url_name,short_url,url)\n"
          "     \033[1mimport\033[0m(query_file) : import your queries from a csv file \n"
          "     \033[1mexit\033[0m : exit DorkR \n"
          "     |--> Exhaustive list available on GitHub")


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


# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()