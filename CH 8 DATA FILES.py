#!/usr/bin/env python
# coding: utf-8

# # DATA FILES

# In[1]:


# with open("file.txt",mode)as handlee:


# In[2]:


with open("hellofile.txt","w")as file:
    file.write("MY NAME IS DANIYAL")
#  write mode
    


# In[3]:


#  so new file is created 


# In[5]:


with open("hellofile.txt","r")as file:
    content=file.read()
print(content)
# read mode


# In[9]:


with open("hellofile.txt","a")as f:
    f.write("   And my father name is Amir  ")
#  append mode     


# In[10]:


#  so APPEND MODE DO NOT overwrite to previous data 


# # r+ and w+ mode

# In[14]:


with open("nonexsisting file","w+")as file:
    file.write("hello my name is crismisharry")
    print(file.read())   
#  so iss nay write too karva dia magar read nhi karvaia isss ley ku kay W+ and r+ mey 
#  write kay baad read karna shoro karta isss ley ham iss ko seek ka fun laga kar 0 index par
#  laye gaye


# In[17]:


with open("nonexsisting file","w+")as file:
    file.write("hello my name is crismisharry")
    file.seek(0)
    print(file.read())
    


# In[20]:


with open("non file","r+")as file:
    file.write("hello my name is crismisharry")
    file.seek(0)
    print(file.read())
    
#  so r+ and r dono tab read ya write karay gay jab woo  exsist karti hooo   


# In[22]:


with open("nonexsisting file","r+")as file:
    file.write("hello my name is crismisharry")
    file.seek(0)
    print(file.read())
    


# In[ ]:




