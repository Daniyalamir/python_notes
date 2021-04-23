#!/usr/bin/env python
# coding: utf-8

# # chapter 5  list
# A smater way too learn python
# 

# a list is an mutable(changable) means changable list is a data structure in python each value 
# in a that is inside in a list is called item 
# list sign []
# The benifit of list u stor multiple type of data in list and u eassily get this data by just 
# calling list and u get ther items by its index                                       
#                                        

# 
# **we can acess the list
# **we can add the value in the end of list 
# *find the index of a value of a list
# *we also delete and removing element in list last , beech, start teeno tareeqoo sey
# *we also assign one list in another list we also copy of list
# *we also slicing in list
# *pooping
# 

# # simply list store buntch of values

# In[4]:


alist = ["daniyal","amir","hadi"]
#  index    0         1    2        


# In[5]:


alist[1]   # get value by this method


# In[7]:


len(alist)


# # imp point
#   len() 
#  kisi bhi cheez ki len check karni hoo too len( variable ) beech mey hoo too check hoo gi  
#  

# # adding a member in  list by using append

# In[8]:


alist.append("ayan")


# In[9]:


alist


# In[11]:


alist.append(56)


# In[12]:


alist


# In[13]:


alist.append(23.6)


# In[14]:


alist


# now one keep on ur mind append function just append means add memeber in end of the list 

# # adding a member in list and we decided where we want to append and what we appended by using insert function
# 

# In[15]:


alist


# In[16]:


alist.insert(2,"kami")
#       index    value for new add


# In[18]:


alist


# # adding a member in  list by using extend but it is diffrent from append and insert because 
# # its add two or more values in list but append and insert do not add it like this

# In[28]:


alist.append(["dani","chachoo"])
# list bana kar 2 ya doo sey ziada values add kar saktay hn


# In[27]:


alist


# In[29]:


alist.append("dani","chachoo")


# In[25]:


alist.insert(3,"bhai","boy")


# In[33]:


alist.insert([3,"bhai","boy"])   
#  insert mey list ki form mey bhi values add nhi hoo gii and dosrii form mey bhi nhi


# In[30]:


alist.extend(["irtaza","bilal","ali"])


# In[31]:


alist


# # now we learn count function count fun count funb counts in list how many time value exsist in list
# 

# In[34]:


alist.count("dani")
#  iss nay 0 iss ley show kia kuu kay dani aik aur liust mey hn


# In[35]:


alist.count("amir")


# # index function checks kay kon sey sey number par yeh index hn

# In[41]:


alist.index("dani")
# so list kay andar list check karnay kay ley
alist.index(["dani","chachoo"])


# In[40]:


alist.index(["dani","chachoo"])


# In[43]:


alist.index("irtaza")


# # clear function remove all the elements in list permermentaly

# In[1]:


alist.clear()


# In[45]:


alist


# soo al elements deleted in list

# # now we learn copy() function copy function make a copy 
#     

# In[2]:


fruits = ["banana ","apple","cherry"]
fruits


# In[5]:


fruitslist= fruits.copy()    # by value
fruitslist


# In[7]:


#  so we see copy() makes a copy in other variable but this copy by value copy means like
fruits1= fruits       # by refrence
fruits1


# In[10]:


fruits.append("orange")
fruits


# In[11]:


fruitslist  # by value no share refrence


# In[13]:


fruits1    # by refrence


# # deleting item in a list by using del statement and one thing keep on ur mind del stat takes 
# # index to remove not value

# In[14]:


fruits1


# In[16]:


del fruits1[3]
# also del as a slicing form [3:5]


# In[17]:


fruits1


# In[18]:


# so its rempove orange in list


# # now we learn remove function to del item in list and it takes
# # value not index

# In[21]:


fruits1


# In[24]:


fruits1.remove("orange")


# In[26]:


fruits1


# # now we learn pop() function it removes item in the last of list by default and also remove by indexing

# In[27]:


cities = ["khi","lahore","islamabad","rawalpindi"]


# In[28]:


cities


# In[31]:


pooping=cities.pop()
print(f"The city is popped from the list {pooping}")
print(f"The remaining cities are{cities}")      


# In[32]:


pooping=cities.pop()
print(f"The city is popped from the list {pooping}")
print(f"The remaining cities are{cities}")      


# In[33]:


pooping=cities.pop()
print(f"The city is popped from the list {pooping}")
print(f"The remaining cities are{cities}")      


# In[34]:


pooping=cities.pop()
print(f"The city is popped from the list {pooping}")
print(f"The remaining cities are{cities}")      


# In[35]:


pooping=cities.pop()
print(f"The city is popped from the list {pooping}")
print(f"The remaining cities are{cities}")      


# In[9]:


# we also pop by indexing pop(index no like 3)


# In[36]:


cities = ['khi', 'lahore', 'islamabad', 'rawalpindi']


# In[37]:


cities


# In[39]:


#  by indexing
citypooped = cities.pop(1)


# In[40]:


cities


# # finding values in list 
# no1 by indexing
# no2 in opreator

# In[41]:


cities


# In[43]:


"rawalpindi" in cities


# In[44]:


fruits1 = ['banana ', 'apple', 'cherry', 'orange', 'orange']


# In[45]:


fruits1


# In[47]:


"cherry" in fruits1


# In[48]:


"cherry " in fruits1


# keep on ur mind python is k sensitive language so upar space cheery kay baad denay sey false 
# aa gia hn

# # slicing

# In[1]:


# index       -5      -4     -3       -2       -1
Names = [ "Daniyal","Amir","hadi","murtaza","bilal"]
# index      0         1    2        3        4


# In[4]:


Names


# In[5]:


Names[0:]


# In[6]:


Names[::]


# In[7]:


Names[0::2]


# # Thats it

# # Practice of list 

# In[1]:


cloths = ["pent","shirt","shilwar kameez","nikar shirt"]


# In[2]:


type(cloths)


# In[3]:


len(cloths)


# using of append

# In[4]:


cloths.append("binyan")


# In[5]:


cloths


# In[8]:


cloths.insert(2,"troozer")


# In[9]:


cloths


# In[15]:


cloths.extend("lihaf")


# In[17]:


# extend ka rule hain kay agar koi 2 items karwani hain too [] lagani hoo gii
cloths.extend(["soccz","moflar"])
cloths


# In[19]:


# index checking
cloths.index("soccz")


# In[23]:


cloths.index(["moflar","soccz"])


# In[24]:


cloths.index("moflar")


# In[27]:


# clear is used to delete all list 
cloths.clear()
cloths
# so alll cloth list are deleted now


# In[28]:


# copy() 
mobile = ["huawai","oppo","qmobile","samsung"]


# In[29]:


mobile


# In[32]:


mobile_makers_brands = mobile.copy()
mobile_makers_brands 


# In[35]:


# =
mobilelist = mobile
mobilelist


# In[36]:


mobile.insert(2,"techno")


# In[42]:


mobilelist


# In[43]:


mobile


# In[40]:


mobile_makers_brands


# In[ ]:


# del function takes a index to to remove a value


# In[44]:


del mobile[4]


# In[45]:


mobile


# In[46]:


mobile_makers_brands


# In[47]:


mobilelist


# In[48]:


# remove function used to remove item in a list and it takes item to remove value
mobile.remove("oppo")


# In[49]:


mobile


# In[50]:


mobile.pop(2)


# In[51]:


mobile


# In[54]:


mobile.pop(0)
# this is is not a right method of pooping lets understand with example 


# In[55]:


mobile


# In[56]:


# first of all make alist 
mobile.extend(["oppo","techno","qmobile","infinix"])


# In[57]:


mobile 


# In[60]:


#pooping kay ley hamsesha sey pop() kisi variable mey store karna parta hain
mobile_tech = mobile.pop()
print(f"this brand pop from  the {mobile_tech}")
print(f"The remaining brands are {mobile}")      
                         


# In[61]:


# finding values in a list 
mobile 


# In[64]:


"oppo" in mobile


# In[65]:


# slicing
mobile


# In[66]:


mobile.extend(["samsung","qmobile","huawaie","infinix","techno","nokia"])


# In[67]:


mobile


# In[69]:


# now we doing slicing 
mobile[0:3]


# In[70]:


mobile[::3]


# In[ ]:




