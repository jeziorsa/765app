import csv

def import_wordlist(file):
    csvReader = csv.reader(open(file,'rb'), delimiter=' ', quotechar='|')
    return csvReader

def clear_list(list):
    
    return

def show_list(list):
    for row in list:
        print ', '.join(row)
    return


if __name__ == '__main__':
    list = import_wordlist('wordlist.csv')	
    print list
    #show_list(list)
