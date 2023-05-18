
def starting_app() :
    f = open('text/start.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    f = open('text/help.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()


def input_listener():
    """Listen and prepare the user's entry for processing"""

    entry = input(">>>>? ")
    entry = entry.split(sep='(')
    function = entry[0]
    params = []
    if function not in ['exit', 'dork', 'dork_csv']:
        print("      Bad entry. Please check your query.")
    else :
        if (len(entry) >= 2):
            if function == "dork" :
                params_tmp = entry[1].split(')')[0].split(sep=',')
                params = [param for param in params_tmp if param in ["country","region","city","ip","url_name","short_url","url","tld"]]
            if function == "dork_csv" :
                params_tmp = entry[1].split(')')[0].split(sep=',')
                params = [param for param in params_tmp if param in ["country", "region", "city", "ip", "url_name", "short_url", "url","tld"]]
                params.insert(0,params_tmp[0])
    return function,params

def ask_pages():
    begin = -1
    end = -2
    while (end < begin):
        try:
            begin = int(input("     From page : "))
            end = int(input("     To page : "))
        except:
            print("     Please enter an integer.")
    return (begin,end)

def print_settings(params):
    settings = "     * default (url,url_name,short_url,tld)"
    if (len(params) > 0):
        settings = "     * url (default)\n"
    for p in params:
        settings += "     * " + p + "\n"
    print("     Your dorking settings : \n" + settings)

