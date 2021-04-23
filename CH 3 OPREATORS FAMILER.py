#!/usr/bin/env python
# coding: utf-8

# # Chapter 3 opreators
# a smater way to learn python

# # (+,\\,-,*) are all opreators but familier

# In[6]:



(67+78)


# In[7]:


(566*55)


# In[9]:


#  this is direct method to perform opreastors 


# In[10]:


#  we also do it at indirect method
var1 = 55
var2 = 365
sum = var1 * var2
print(sum)


# In[15]:


var1 = 55
var2 = 365
sum = var1/ var2
print(sum)
# python by default floting divison  karti hn mgr agar floating nhi integer division chaie h
#  too double // lagao ga


# In[16]:


var1 = 55
var2 = 365
sum = var1// var2
print(sum)


# In[17]:


var1 = 100
var2 = 200
sum = var1/ var2
print(sum)


# In[19]:


var1 = 100
var2 = 200
sum = var1// var2
print(sum)


# In[21]:


var1 = 55
var2 = 365
sum = var1 + var2
print(sum)


# In[14]:


#  this all are indirect methods


# In[20]:


num = "ddxs"
num = "sdgs"
print(num+num)
#  string do not add but concatinate


# Practice_of_oprreators 

# In[2]:


num1 = 10 
num2 = 20
sum = num1 + num2 
print(sum)


# In[3]:


num1 = 49 
num2 = 60
sum = num1 * num2 
print(sum)


# In[4]:


num1 = 49 
num2 = 60
sum = num1 / num2 
print(sum)


# In[5]:


num1 = 49 
num2 = 60
sum = num1 // num2 
print(sum)


# In[8]:


num = 10
print(num == 10)


# In[9]:


num = 10
print(num > 10)


# In[10]:


num = '10'
print(num == 10)


# now we learn and and or opreators 

# * and opreator used when both condition are true 
# * or opreator is used when both condition are false 
# * not opreator is used for reverse the answer 

# In[13]:


# lets understand with example ..
age = 18
gpa = 3.6
result = age>=17 and gpa > 3.8
print(result)    # dekha firr and nay both conditions true chaiiee


# In[14]:


age = 18
gpa = 3.6
result = age>=17 or gpa > 3.8
print(result)    # or ko 1 con bhi true nil gai too true kar dia like age 


# In[20]:


age = 12
print( age  <=18)


# In[21]:


age = 12
print( not age  <=18)
agter putting not it reverse my answer


# In[22]:


# another example 
result = True 
print(result)


# In[24]:


result = True 
print(not result)


# Practice

# In[28]:


language = "python"
print("l",language =="python")


# In[29]:


language = "python"
print("l",not language =="python")


# In[36]:


age = 18
print("2",age >= 18)
print("3",age >18)
print("4", age>=18 and language == "java")


# In[ ]:




