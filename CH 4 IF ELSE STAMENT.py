#!/usr/bin/env python
# coding: utf-8

# # chapter 4 if else statement 
# A smarter way to learn python

# In[5]:


a = 10
b = 20
if a<b == True:
    print("30 is ur result")
    
elif a > b == False:
        print("something is wrong")
        


# In[7]:


a = 10
b = 20
if a<b:
    print("30 is ur result")
else:
    print("wrong output")
    


# In[8]:


a = 10
b = 20
if a>b:
    print("30 is ur result")
else:
    print("wrong output")
    


# # imp information

# In[17]:


input()


# In[16]:



#  input user sey koi input lanay kay ley isttamal kia jata hn like 
daniyal = input(("enter ur fav number "))


# but anything enter u in input() fun its store as a string like mey nay upar 5 lya hn mey kho 
# iss 5 ko 10 mey add kara doo too yeh nhi hoo ga because string concatinate hota hain agar ham
# integer form mey chatay hn takay ussn koo add ya us par koi opreation kia jaaa sakay too we 
# typecast like this
# 

# In[14]:


dani = int(input("enter ur fav number "))


# Practice_of_if_statement:

# In[3]:


marks = int(input("Ente ur marks"))
if marks>=50:
    print("u are passed in exams")
    print("congratulations")    


# In[4]:


marks = int(input("Ente ur marks"))
if marks>=50:
    print("u are passed in exams")
    print("congratulations")    
    


# In[5]:


#this is not run bcz ham nay 50 sey nechay ka patya hoa hee nhi tha
marks = int(input("Enter ur marks"))
if marks>=50:
    print("u are passed in exams")
    print("congratulations")    
if marks<50:
    print("u are fail")
    


# In[6]:


# agr number pouchay na jayee input dey kar or phelay hee day dey jaye or sirf pass ya fail ka mssg show karwana hoo 
# iss kay ley ham else ko use karay gaye
# for example 
score = 37
if marks>=50:
    print("u are passed in exams")
    print("congratulations")    
if marks<50:
    print("u are fail")
# iss tarha bhi answer aa jayee ga mgr right way below


# In[9]:


score = 46
if marks>=50:
    print("u are passed in exams")
    print("congratulations")    
else :
    print("u are fail")
    


# In[19]:


# now we using elif statemwnt elif used when u put a else stement and u have more than two if
marks = -1
if marks>=50 or marks <=100:
    print("u are passed in exams")
    print("congratulations")    
elif marks<50:
    print("u are fail")
else:
    print("Daniyal amir")


# In[27]:



num = 19

# Try these two variations as well. 
# num = -5
# num = 0


num = 3

# Try these two variations as well. 
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")


# In[30]:


num =-33
if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")


# In[31]:


# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")


# In[32]:


num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = 1   # upar -1 tha and ham nay condition lagai thi kay num 0 sey bara hona chaiee hn upar -1 tha and - is small to 0
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")


# In[33]:


'''In this program, 
we check if the number is positive or
negative or zero and 
display an appropriate message'''

num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# In[34]:




num = 0

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# In[35]:



num = -3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# In[36]:


num = int(input("Please enter the number"))

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# In[40]:


num = int(input("please enter the number"))
        

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# Python Nested if Example

# In[43]:



# This time we use nested if statement''
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
    
    


# In[44]:


num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
    
    


# In[48]:


num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")


# if_elif_else statement using

# In[52]:


a = 24
b = 88
if a > b :
    print("a is greater than b")
elif a >= b:
    print("a is less than b")
elif a==b:
    print("a and b are equal")
else:
    print("a and b are not equal")


# In[ ]:




