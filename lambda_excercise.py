#Lambda Excercise 1

#Consider the List

from re import X


prog_lang = [('Python', 3.8),
    ('Java', 13),
    ('JavaScript', 2019),
    ('Scala', 2.13)]

#1. Sort the list by each language's version in ascending order.
#[('Scala', 2.13), ('Python', 3.8), ('Java', 13), ('JavaScript', 2019)]
prog_lang = sorted(prog_lang,key=lambda x:x[1])
print (prog_lang)

#2. Sort the list by the length of the name of each language in descending order.
#[('JavaScript', 2019), ('Python', 3.8), ('Scala', 2.13), ('Java', 13)]
prog_lang = sorted(prog_lang,key=lambda x:x[0], reverse=True)
print (prog_lang)
#3. Filter the list so that it only contains languages with 'a' in it.
#[('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]
def myfilter(prog_lang):
    return list (filter(lambda x: 'a' in x[0], prog_lang))
print (myfilter(prog_lang))    

#4. Filter the list so that it only contains languages whose version is in integer form.
#[('Java', 13), ('JavaScript', 2019)]

mylist =list(filter(lambda x:type(x[1]) == int,prog_lang))
print (mylist)
#5. Transform the list so that it contains the tuples in the form,
#("language in all lower case", length of the language string)
#[('python', 6), ('java', 4), ('javascript', 10), ('scala', 5)]
     
mylist = list(map(lambda x: (x[0].lower(), len(x[0])), prog_lang))
print(mylist)

#6. Generate a tuple in the form,
#("All languages separated by commas","All versions separated by commas")
#('Python,Java,JavaScript,Scala', '3.8,13,2019,2.13')
mylist1 = list(map(lambda x: x[0],prog_lang))
mylist2 = list (map(lambda x: str(x[1]), prog_lang))
print(mylist1+mylist2)
