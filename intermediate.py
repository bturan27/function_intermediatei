from importlib.machinery import WindowsRegistryFinder


x = [ [5,2,3], [10,8,9] ] 
students = [
{'first_name':  'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15

students[0]['last_name']='Bryant'
print(students)


sports_directory['soccer'][0]="Andres"

z[0]['y']=30
print(z)

students = [
{'first_name':  'Michael', 'last_name' : 'Jordan'},
{'first_name':  'John', 'last_name' : 'Rosales'},
{'first_name':  'Mark', 'last_name' : 'Guillen'},
{'first_name':  'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(some_list):
    for x in range(len(some_list)):
        a=(some_list[x]['first_name'])
        b=(some_list[x]['last_name'])
        print(f" first_name-{a}last_name-{b}")
iterateDictionary(students)

#3
students = [
{'first_name':  'Michael', 'last_name' : 'Jordan'},
{'first_name':  'John', 'last_name' : 'Rosales'},
{'first_name':  'Mark', 'last_name' : 'Guillen'},
{'first_name':  'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])

iterateDictionary2('last_name',students)


dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


#4 print out of the lenght of the values
#print out key Words
#print out values in list

def printInfo(some_dict):
    for x in some_dict:
        print(f"{len(some_dict[x])} {x}")
        for value in range(0,len(some_dict[x])):
            print(some_dict[x][value])
printInfo(dojo)
