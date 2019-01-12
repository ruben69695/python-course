
# coding: utf-8

# # Operadores encadenados

# In[3]:


# Traditional method
1 < 2 and 2 < 3


# In[4]:


# Chained operator method
1 < 2 < 3


# In[6]:


# Traditional method
numero = 25
if numero >= 0 and numero <= 100:
    print("Okay")


# In[7]:


# Chained operator method
numero = 25
if 0 <= numero <= 100:
    print("Okay")

