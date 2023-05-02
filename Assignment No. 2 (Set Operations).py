'''
Author - Ravindra Dayaram Bagul
College - SKNCOE, Pune
University - SPPU
'''
'''
To create ADT that implements the “set” concept
	a) Add (new element) - place a value into a set
	b) Remove (element) - remove the value
	c) Contains (element) - return true if element is in a collection
	d) Size () - return number of values in collection 
	e) Intersection of two sets.
	f) Union of two set 
	g) Difference between two sets
	h) Subset

'''

size=int(input("Enter size of set 1 : "))
size1=int(input("Enter size of set 2 : "))
print("\nFor set 1 :")
list1=[]
for i in range(size):
    element=int(input("   Enter element : "))
    list1.append(element)
print("set 1 = ",list1)
    
print("\nFor set 2 :")
list2=[]
for i in range(size1):
    element=int(input("   Enter element : "))
    list2.append(element)
print("set 2 = ",list2)

choice = 0
while choice != 10:
	print("\n---------------------")
	print("******* Menu ******* ")
	print("   1.Add             ")
	print("   2.Remove          ")
	print("   3.Contains        ")
	print("   4.Size            ")
	print("   5.Intersection    ")
	print("   6.Union           ")
	print("   7.Difference      ")
	print("   8.Subset          ")
	print("   9.Proper Subset   ")
	print("   10.Exit           ")
	print("---------------------\n")

	choice = int(input("Enter Choice : "))
	print()
	if choice==1:
		e = int(input("Enter Number to Add : "))
		list1.append(e)
		print("set 1 = ",list1)

	elif choice==2:
		e = int(input("Enter Number to Remove : "))
		if e in list1:
			list1.remove(e)
			print("set 1 = ",list1)
		else:
			print(e," is not in set 1")

	elif choice==3:
		e = int(input("Enter Number to Search in set 1: "))
		if e in list1:
			print("Number Present in Set 1 !!")
		else:
			print("Number is not Present in Set 1 !!")
		print("set 1 = ",list1)

	elif choice==4:
		print("Set 1 Contains {} elements !!".format(len(list1)))

	elif choice==5:		
		list3=[]		
		for element in list1:
			if element in list2:
				list3.append(element)
		print("Set 1= ",list1)
		print("Set 2 = ",list2)
		print("Intersection = ",list3)
	
	elif choice==6:		
		list3=[]		
		list3=list1.copy()
		for element in list2:
			if element not in list1:
				list3.append(element)
		print("Set 1 = ",list1)
		print("Set 2 = ",list2)
		print("Union = ",list3)

	elif choice==7:
		list3=[]
		for element in list1 :
			if element not in list2:
				list3.append(element)
		print("Set 1 = ",list1)
		print("Set 2 = ",list2)
		print("set1-set2 = ",list3)

	elif choice==8:
		print("Set 1= ",list1)
		print("Set 2 = ",list2)
		list3=[]		
		def sub():
			flag = 0
			for e in list2:
				if e in list1:
					flag = 1
				else:
					print("Set 2 is not a Subset of Set 1 !!")
					return
			if flag == 1:
				print("Set 2 is the Subset of Set 1 !!")
		sub()

	if choice==9:
		print("Set 1= ",list1)
		print("Set 2 = ",list2)
		if sorted(list1)==sorted(list2):
			print("Set 2 is the Proper Subset of Set 1 !!")
		else:
			print("Set 2 is not a Proper Subset of Set 1 !!")

	elif choice==10:
		print("Thanks for using this Program !!")
		break

	elif choice<1 or choice>10:
		print("Please Enter Valid Choice !!")