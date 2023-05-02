'''
Author - Ravindra Dayaram Bagul
College - SKNCOE, Pune
University - SPPU
'''

'''
Assignment No:1
Consider telephone book database of N clients. Make use of a hash table 
implementation to quickly lookupclient‘s telephone number. Make useoftwo
collision handling techniques and compare them using number of comparisons 
required to find a set of telephone numbers. Write a Python program for the 
same.
'''

def initializeHashTable():
    size = int(input('Enter size of hash table: '))
    hashtable = [[-1, 'null'] for i in range(size)]
    print('Hashtable of size', size, 'is successfully created .....')
    print(' ')
    return(size, hashtable)
choice = 1
while(choice!= 4):
    print('\n****** Menu ******')
    print(' 1.Linear Probing')
    print(' 2.Double Hashing')
    print(' 3.Exit\n')
    choice = int(input('Enter your choice: '))
    print()
    count = 0

    if choice == 1:
        size, hashtable = initializeHashTable()
        choice1 = 1
        while(choice1 != 4):
            print('\n* Menu for Linear Probing *')
            print('    1.Insert')
            print('    2.Search')
            print('    3.Display')
            print('    4.Back\n')
            choice1=int(input('Enter your choice: '))
            print()
            if choice1 == 1:
                if(count == size):
                    print('Hash table is Full .........')
                else:
                    number = int(input('Enter number : '))
                    name = input('Enter Name : ')
                    hashvalue = number % size
                    while(hashtable[hashvalue][0] != -1):
                        print('\nCollision has occured .....')
                        print('Now, Calculating new hash value by using linear Probing')
                        hashvalue = (hashvalue + 1)%size
                    hashtable[hashvalue][0] = number
                    hashtable[hashvalue][1] = name
                    count += 1
                    print('Data is successfully inserted in the hash table ....')
                    print('Total inserted record=',count)
                    print('')
            if choice1 == 2:
                number = int(input('Enter number to search: '))
                hashvalue = number % size
                comparision = 0
                #i= 0
                while(hashtable[hashvalue][0] != number and comparision < size):
                    hashvalue = (hashvalue + 1)%size
                    comparision += 1
                    #i=i+1
                if comparision < size:
                    print('The number', number, 'is found at location', hashvalue, 'with total comparisions=', comparision+1)
                else:
                        print('The number is NOT found in the hashtable.... with comparisions', comparision+1)
            if choice1 == 3:
                for i in range(size):
                    print('Hash Value ', i,' -> ',hashtable[i])
     
        count= 0
    if choice == 2:
        size, hashtable = initializeHashTable()
        choice1 = 1
        while(choice1 != 4):
            print('\n* Menu for Double Hashing *')
            print('    1.Insert')
            print('    2.Search')
            print('    3.Display')
            print('    4.Back\n')
            choice1=int(input('Enter your choice : '))
            print()
            if choice1 == 1:
                if(count == size):
                    print('Hash table is Full .........')
                else:
                    number = int(input('Enter number : '))
                    name = input('Enter Name : ')
                    hashvalue1= number % size
                    i= 1
                    while(hashtable[hashvalue1][0] != -1):
                        print('\nCollision has occured ..... ')
                        print('Now, Calculating new hash value by Double Hashing Technique')
                        hashvalue1= number % size
                        prime=int(input("\nEnter prime number lesser than size of HASH TABLE : "))
                        hashvalue2 = (prime-(number % prime))
                        hashvalue3= (hashvalue1 + i* hashvalue2) % size 
                        i=i+1
                        hashvalue1=hashvalue3
                    hashtable[hashvalue1][0] = number
                    hashtable[hashvalue1][1] = name
                    count += 1
                print('Data is successfully inserted in the hash table .....')
                print('Total inserted record=',count)
                
            if choice1 == 2:
                number = int(input('Enter number to search: '))
                hashvalue1 = number % size
                comparision = 0
                i = 1
                while(hashtable[hashvalue1][0] != number and comparision < size):
                    hashvalue1 = number % size
                    prime=int(input("Enter prime number lesser than size of HASH TABLE : "))
                    hashvalue2 = (prime-(number % prime))
                    hashvalue3= (hashvalue1 + i* hashvalue2) % size
                    hashvalue1 = hashvalue3
                    comparision += 1
                    i= i+1
                if comparision < size:
                    print('The number', number, 'is found at location', hashvalue1, 'with comparisions', comparision+1)
                else:
                    print('The number is NOT found in the hashtable... with comparisions', comparision+1)
            if choice1 == 3:
                for i in range(size):
                    print('Hash Value ', i,' -> ',hashtable[i])
                    
    if choice == 3:
        exit()
