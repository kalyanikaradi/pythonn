#!/usr/bin/env python
# coding: utf-8

# In[6]:


#list methods
#replacing multiple values
list=[2,3,4,84,32,11,89,34,65]


# In[7]:


list[2:4]=[56,90]


# In[8]:


list


# In[15]:


#count method specify the number of repeated values
points=[1,2,34,56,77,77,89,4,77]
x=points.count(77)
print(x)


# In[18]:


#sort method arrange values in ascending order
numbers=[3,1,5,6,21,78,9]
numbers.sort()
print(numbers)


# In[ ]:





# In[26]:


#reverse method is used to reverse the order of list
numbers=[7,3,4,2,11,56,78,90]
numbers.reverse()
print(numbers)


# In[31]:


#copy the list
numbers=[4,3,2,6]
x=numbers.copy()
print(x)


# In[39]:


x=max(5,4,3)
print(x)


# In[1]:


#tuple  methods
#count(returns number of count of a specified value )
t3=(2,3,3,4,5,6,7,7,8)
t3


# In[2]:


t3.count(7)


# In[3]:


t3.count(3)


# In[4]:


t3.count(8)


# In[5]:


#index(specify index value)
t3


# In[6]:


t3.index(4)


# In[7]:


t3.index(7)


# In[8]:


#set methods
#add(adding elements to set)
myset7={'abc','xyz','pqr'}
myset7.add('klm')




# In[9]:


myset7


# In[10]:


#clear(removes all elements)
myset7


# In[13]:


myset7.clear()


# In[14]:


myset7


# In[15]:


#difference(specify difference elemnts in set)
A={3,4,5,6,7,8}
B={4,9,0,1,3}
A.difference(B)


# In[18]:


#discard(remove particular elements)
A={9,5,6,3}
A.remove(3)


# In[19]:


A


# In[22]:


#intersection(return the common element from sets)
A={3,45,7,8}
B={4,5,6,9,7}
A.intersection(B)


# In[23]:


#union(return combination of two sets)
A={4,5,7,8}
B={7,9,0,4,8}
A.union(B)


# In[26]:


#update(change the set)
X={4,5,7,8}
X.update([10])


# In[27]:


X


# In[32]:


#issubset
x={'a','b','c'}
y={'f','e'}
x.issubset(y)


# In[ ]:


#dictinary methods


# In[1]:


#clear (remove elements from dictionary)
mydict={'name':'abc','id':4567,'address':'pune' }


# In[2]:


mydict


# In[3]:


mydict.clear()


# In[4]:


mydict


# In[ ]:


#copy(returns copy of dictionary)


# In[6]:


car={"brand":'ford','model':'mustang','year':1964}


# In[7]:


car


# In[8]:


car.copy()


# In[ ]:


#fromkeys (returns dictionary from specified key)


# In[9]:


x={'key1','key2','key3'}


# In[10]:


x


# In[11]:


y=0
dict.fromkeys(x,y)


# In[12]:


#get (returns the value of specified value)
car.get('model')


# In[ ]:


#keys(returns a list containing the dictionary's keys)


# In[13]:


car.keys()


# In[14]:


#values
car.values()


# In[15]:


#update(update dictionary with specified key value pairs)
car.update({'color':'black'})
car
    


# In[16]:


#pop(remove the element with specified key)
car.pop('year')


# In[17]:


car


# In[ ]:




