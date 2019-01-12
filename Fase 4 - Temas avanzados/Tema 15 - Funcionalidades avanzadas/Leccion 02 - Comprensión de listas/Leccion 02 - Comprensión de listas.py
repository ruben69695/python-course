
# coding: utf-8

# # Comprensión de listas

# In[5]:


# Traditional method
cadena = "hello world!"
letters = []
for char in cadena:
    letters.append(char)
letters


# In[6]:


# Understanding lists
letters = [char for char in "hello world!"]
letters


# In[7]:


# Traditional method
numbers = []
for number in range(0, 11):
    numbers.append(number)
numbers


# In[8]:


# Understanding lists
numbers = [number for number in range(0, 11)]
numbers


# In[9]:


# Traditional method
multiple = []
for number in range(0, 11):
    multiple.append(number ** 2)
multiple


# In[10]:


# Understanding lists
multiple = [number ** 2 for number in range(0, 11)]
multiple


# In[24]:


# Traditional method
multiple = []
for number in range(0, 11):
    multiple.append(number ** 2)

pair = []
for number in multiple:
    if number % 2 == 0:
        pair.append(number)
pair


# In[19]:


# Understanding lists
pair_numbers = [number for number in [n ** 2 for n in range(0, 11)] if number % 2 == 0]
pair_numbers

