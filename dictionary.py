def clear(): #create a function
    language={
        'Python':1,
        'C++':2,
        'C#':3,
        'Java':4
        }
    print()
    print ("FOR CLEAR METHOD")
    print(language)
    language.clear() #clears/removes the inheritance of clear()
    print(language)
    print("=========================================================================================================================")
def kopy(): #create a function
    language={
        'Python':1,
        'C++':2,
        'C#':3,
        'Java':4
        }
    print()
    print ("FOR COPY METHOD")
    language2 = language.copy() #copies the inheritance of kopy()
    print(language2)
    print("=========================================================================================================================")
def getto(): #create a function
    language={
        'Python':1,
        'C++':2,
        'C#':3,
        'Java':4
        }
    print()
    print ("FOR GET METHOD")
    language2 = language.get('Python') #get the key of an specified properties of getto()
    print(language2)
    print("=========================================================================================================================")
def aytems(): #create a function
    language={
        'Python':1,
        'C++':2,
        'C#':3,
        'Java':4
        }
    print()
    print ("FOR ITEMS METHOD")
    language2 = language.items() #returns the keys and values of the propeties inside the aytems()
    print(language2)
    print("=========================================================================================================================")
def kiss(): #create a function
    language={
        'Python':1,
        'C+':2,
        'C#':3,
        'Java':4
        }
    print()
    print ("FOR KEYS METHOD")
    print('These are the dictionary keys:', language.keys()) #returns the values of the properties inside the kiss()
    print("=========================================================================================================================")


clear() 
kopy() 
getto() 
aytems() 
kiss() 

print()
print ("FOR UPDATE METHOD")
number={'one':'wan', 'two':'too', 'three':'tree', 'four':'for'}
numadded={'five':'fibe', 'six':'sex'}
number.update(numadded) #inserts the numadded keys and values on the number's keys and values
print(number)
print("=========================================================================================================================")

print()
print ("FOR VALUES METHOD")
number={'one':'wan', 'two':'too', 'three':'tree', 'four':'for','five':'fibe', 'six':'sex'}
print(number.values()) #returns and prints the values of the properties inside the number variable
print("=========================================================================================================================")

print()
print ("FOR POP METHOD")
print(number)
number.pop('six') #removes the specified key and values upon entering the chosen key
print(number)
print("=========================================================================================================================")

print()
print ("FOR POPITEM METHOD") 
print(number)
number.popitem() #removes a key and value on the rear of the number properties
print(number)
print("=========================================================================================================================")

