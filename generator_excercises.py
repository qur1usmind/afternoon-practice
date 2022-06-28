#Generator Excercises

#Problem 1
#Create a generator, primes_gen that generates prime numbers starting from 2.
#from ctypes import pointer
#from tkinter import N


def primes_gen():
    n=1
    while True:
        n+=1
        for num in range(2,n+1):
            if n == num:
                yield n
            if n%num == 0:
                break    


gen=primes_gen()
for _ in range(10):
    print(next(gen), end=' ')

#gen=primes_gen()
#for _ in range(10):
#    print(next(gen), end=' ')
# Expected output
# 2 3 5 7 11 13 17 19 23 29
#----------------------------------------------------------------------------

#Problem 2
#Create a generator, unique_letters that generates unique letters from
#the input string. It should generate the letters in the same order as
#from the input string.
def unique_letters(mystr):    
    unique_char=""
    for letter in mystr:
       if letter not in unique_char: 
          unique_char+=letter          
          yield letter
             
for letter in unique_letters('hello'):
     print(letter, end=' ')
#print (myvar)
# Expected output
# h e l o