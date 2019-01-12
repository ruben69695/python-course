
# coding: utf-8

# # Ámbitos y funciones decoradoras

# #### NOTA: Antes de realizar esta lección debes reiniciar Jupyter Notebook para vaciar la memoria.

# In[4]:


def Hola():
    
    number = 89
    
    def Bienvenido():
        return ("Welcome")
    
    print(locals())
    
    return Bienvenido()

Hola()
print(globals())


# ## Funciones decoradoras

# In[21]:


def execute_message(function):
    
    def decorate():
        print("Message executed > {}".format(function()))
    
    return decorate

def sayHello():
    return "Hello"
def sayGoodbye():
    return "Goodbye"
def omg():
    return "OMG!"
def cloudySkies_lilSkies_lyrics():
    return '''
        [Intro]
        Girl, never lie to me
        Ayy, girl, never lie to me
        Duck from the flashin' lights, watch out when the tide comin'
        All these people judgin'
        Take a sip out the double cup, can't tell me nothin'
        I know it's all for the better and I'm never stuntin'
        I just want a girl who gon' really tell me somethin', ayy

        [Chorus]
        Ayy, girl, never lie to me
        Girl would you ride for me? Pull up on the side for me
        Duck from the flashin' lights, and watch out when the tide comin'
        I know it's hard to be yourself when all these people judgin'
        Take a sip out the double cup, can't tell me nothin'
        I know it's all for the better and I'm never stuntin'
        I just want a girl who gon' really show me somethin'
        Give you the time of your life if you would stop frontin'
    '''
execute_message(sayHello)()


# In[23]:


@execute_message
def sayHello():
    return "Hello"

@execute_message
def sayGoodbye():
    return "Goodbye"

@execute_message
def omg():
    return "OMG!"

@execute_message
def cloudySkies_lilSkies_lyrics():
    return '''
        [Intro]
        Girl, never lie to me
        Ayy, girl, never lie to me
        Duck from the flashin' lights, watch out when the tide comin'
        All these people judgin'
        Take a sip out the double cup, can't tell me nothin'
        I know it's all for the better and I'm never stuntin'
        I just want a girl who gon' really tell me somethin', ayy

        [Chorus]
        Ayy, girl, never lie to me
        Girl would you ride for me? Pull up on the side for me
        Duck from the flashin' lights, and watch out when the tide comin'
        I know it's hard to be yourself when all these people judgin'
        Take a sip out the double cup, can't tell me nothin'
        I know it's all for the better and I'm never stuntin'
        I just want a girl who gon' really show me somethin'
        Give you the time of your life if you would stop frontin'

    '''


# In[19]:


sayGoodbye()


# In[24]:


cloudySkies_lilSkies_lyrics()


# ## Pasando argumentos al decorador

# In[25]:


def execute_message(function):
    
    def decorate(*args, **kwargs):
        print("Message executed > {}".format(function(*args, **kwargs)))
    
    return decorate


# In[26]:


sayGoodbye()


# In[27]:


@execute_message
def sayGoodbye(name):
    return "Goodbye {}".format(name)


# In[28]:


sayGoodbye("Ruben")

