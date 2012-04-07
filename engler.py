import csv
import re

def import_wordlist(file):
    csvReader = csv.reader(open(file,'rb'), delimiter=' ', quotechar='|')
    return csvReader

def clear_list(list):
    
    return

def show_list(list):
    p = re.compile('[a-z]')	
    for row in list:
	#print ', '.join(row)
	print ''.join(p.findall(row[0]))
	#print row[0]
    return


if __name__ == '__main__':
    list = import_wordlist('wordlist.csv')	
    #print list
    show_list(list)

    #isinstance(list, tuple)
    
    #type(list)
    #print 'im working'
