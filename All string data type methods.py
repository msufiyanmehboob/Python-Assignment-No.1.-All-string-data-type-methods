#!/usr/bin/env python
# coding: utf-8

# In[1]:


import this


# In[2]:


5 + 8 # Operation
#Opertors
    # +, - ,/ , * , , $, **
    # = , +=, -=, /=, *=, %=
    # == , >, <, >=, <=
# 5, 8 Operads


# In[3]:


#PEMDAS
5 + 7 - 8 * (2//2)  +200
#5 + 7 - 8 * (1)  +200
#5 + 7 - 8   +200
#12 - 8 +208
#212 -9
#204


# In[4]:


a = 8
b = 8

print(a)
print(b)

print(id(a))
print(id(b))

b += 1
print(id(a))
print(id(b))


# In[5]:


a = 7 
type(a)


# In[6]:


a = 20.7
type(a)


# In[7]:


a = True
type(a)


# In[8]:


a = False
type(a)


# In[9]:


5 /5


# In[10]:


a ="1"
type(a)


# In[11]:


a = """1"""
type(a)


# In[12]:


"1" + "1"


# In[13]:


int ("1") + int ("1")


# In[14]:


a = 20
type(a)


# In[15]:


a= "Pakistan"
a * 2


# In[16]:


1+7


# In[17]:


'1' + '7'


# In[18]:


names = {"Muhammad", "sufiyan", "Mehboob", 200}
print(type(names))


# In[19]:


names = ["Muhammad", "sufiyan", "Mehboob", 200]
print(type(names))


# In[20]:


#index       0          1        2      3
names = ("Muhammad", "sufiyan", "Mehboob", 200)
#index      -0          -1      -2      -3
print(type(names))
print(names[0])
print(names[1])
print(names[2])
print(names[3])


# In[21]:


names = {"Muhammad", "sufiyan", "Mehboob", 200, "Sufiyan"}
names = list(names)

print(names[0])
print(type(names))


# In[22]:


data = {
    #key : Value
    'names':"Muhammad Sufiyan Mehboob",
    'fnames':"Ghulam Samdani",
    'names':"MSM",
     5     : 'Pakistan',
    "a"    :[True, "Pakistan", 20, 3.0]
}

data['a']


# In[23]:


a = "Muhammad Sufiyan Mehboob"
dir(a)


# In[24]:


a = "Muhammad Sufiyan Mehboob"
print(a.upper())
print(a)


# In[25]:


a = "Muhammad Sufiyan Mehboob"
print(a.upper())
a


# In[26]:


a = "Muhammad Sufiyan Mehboob"
print(a.title())


# In[27]:


a = "Muhammad Sufiyan Mehboob"
a


# In[28]:


a = "Muhammad Sufiyan Mehboob"
print(a.capitalize())


# In[29]:


a = "                                 Muhammad Sufiyan Mehboob                                        "
a


# In[30]:


a = "                                 Muhammad Sufiyan Mehboob                                        "
print(len(a))
print(a.strip())
print(len(a.lstrip()))
print(len(a.rstrip()))


# In[31]:


a = "                                 Muhammad Sufiyan Mehboob                                        "
a


# In[32]:


b= a.split()
b


# In[33]:


" ".join(b)


# In[34]:


a ="we are pakistan we love our country!"
a


# In[35]:


#List[start:end:step]
#aTuples[start:end:step]
#String[start:end:step]

print(a)
print(a[::])
print(a[7:15:])
print(a[::-1])


# In[37]:


print(a)
print(a.index("pakistan"))


# In[38]:


str.isnumeric('5A')


# In[39]:


a = "drgsretsveghsjfhgf-dskgvsbvksv-3-3xmfbg f/3gshd"
" ".join([i for i in a if str.isnumeric(i)])


# In[40]:


card = """
Bahria University Islamabad
name: Muhammad Sufiyan Mehboob
Father_name: Ghulam Samdani
Program: PIAIC
"""

print(card)


# In[48]:


name = "Muhammad Sufiyan Mehboob"
fname = "Ghulam Samdani"
program = "PIAIC"
s = 200

card = """
Bahria University Islamabad
name: %s
Father_name: %s
Program: %s
Score: %d
"""

print(card%(name,fname,program,s))


# In[43]:


name = "Muhammad Sufiyan Mehboob"
fname = "Ghulam Samdani"
program = "PIAIC"
s = 200

card = """
Bahria University Islamabad
name: {}
Father_name: {}
Program: {}
Score: {}
"""

print(card.format(name,fname,program,s))


# In[44]:


name = "Muhammad Sufiyan Mehboob"
fname = "Ghulam Samdani"
program = "PIAIC"
s = 200

card = """
Bahria University Islamabad
name: {3}
Father_name: {1}
Program: {2}
Score: {0}
"""

print(card.format(name,fname,program,s))


# # Python Assignment No. 1 will be start declare all string data type methods

# 

# In[50]:


s ='Muhammad Sufiyan Mehboob'
dir(s)


# In[55]:


name ='Muhammad Sufiyan Mehboob'
print(name)
print(name.capitalize()) #Only capitalize 1 character of string


# In[54]:


name ='Muhammad Sufiyan Mehboob'
print(name.casefold()) #lower all character of string


# In[53]:


name ='Muhammad Sufiyan Mehboob'
print(name.center(40)) #taking space of 40 character and pring name in the middle


# In[56]:


name='Muhammad Sufiyan Mehboob'
print(name.count('a')) #print total number of a character like 'a'


# In[57]:


name='Muhammad Sufiyan Mehboob'
print(name.encode()) #encode the string


# In[58]:


name='Muhammad Sufiyan Mehboob'
print(name.endswith('l')) #compare with end character of string and reture true or false


# In[75]:


name ='S\tufiyan Mehboob'
print(name.expandtabs(3)) #space between the character


# In[79]:


name='Muhammad Sufiyan Mehboob'
print(name.find('m')) #return the index of find character


# In[80]:


name='My Name is {fname} {lname}'
print(name.format(fname='Muhammad',lname='Sufiyan Mehboob')) #Insert the fname and lname inside the placeholder{}, the fname and lname should be in fixed point


# In[81]:


name={'fname':'Muhammad', 'lname':'Sufiyan Mehboob'}
print('{fname} {lname}'.format_map(name))


# In[83]:


name='Muhammad Sufiyan Mehboob' 
print(name.index('S'))  #return the index of specific character


# In[84]:


name='Sufiyan039' 
print(name.isalnum()) #return if string is alphanumeic or not e.g character and number


# In[85]:


name='MuhammadSufiyanMehboob' 
print(name.isalpha()) #return true of false if string have all alphabets without space


# In[86]:


name='Muhammad Sufiyan Mehboob' 
print(name.isascii())


# In[87]:


name='Muhammad Sufiyan Mehboob' 
print(name.isdecimal()) #return if string have any decimal value


# In[94]:


name='Muhammad Sufiyan Mehboob' 
print(name.isdigit()) #return if string have any digits


# In[89]:


name='MuhammadSufiyanMehboob' 
print(name.isidentifier()) #return true or false if string have some identifier like start with _,or no space between word


# In[92]:


name='Muhammad Sufiyan Mehboob'
print(name.islower()) #return true or false if string have all characters are lower case


# In[93]:


name='Muhammad Sufiyan Mehboob'
print(name.isnumeric())
number='15'
print(number.isnumeric()) #return true or false if string have all characters are numeric


# In[95]:


name='Muhammad Sufiyan Mehboob'
print(name.isprintable()) #return true or false if string have all characters are printable


# In[96]:


name='Muhammad Sufiyan Mehboob'
print(name.isspace())
name='  '
print(name.isspace())  #returns True if all the characters in a string are whitespaces, otherwise False


# In[97]:


name='Muhammad Sufiyan Mehboob'
print(name.istitle()) #return true or false if each word start with an upper case letter


# In[99]:


name='muhammad sufiyan mehboob'
print(name.isupper())
name='MUHAMMAD SUFIYAN MEHBOOB'
print(name.isupper())  #return true or false if whole string will have upper case letter


# In[100]:


name={'Muhammad','Sufiyan Mehboob'}
print('  '.join(name)) #method takes all items in an iterable and joins them into one string. A string must be specified as the separator.


# In[101]:


name='Muhammad '
name1=name.ljust(20)
print(name1,"Sufiyan Mehboob")  #return 20 character space from left justified


# In[102]:


name='Muhammad Sufiyan Mehboob'
print(name.lower())  #return all character in lower case


# In[103]:


name='   Muhammad Sufiyan Mehboob   '
print(name)
name='   Muhammad Sufiyan Mehboob   '
print(name.lstrip())   #remove space for letf side


# In[104]:


name='Muhammad Sufiyan Mehboob'
print(name.partition('Sufiyan Mehboob'))  #return a tuple


# In[105]:


name='Muhammad Sufiyan Mehboob'
print(name.replace('Sufiyan','Sufi'))  #replace the word to another word


# In[109]:


name='Muhammad Sufiyan Mehboob'
print(name.rfind('b')) #return the index almost rindex(),if value not found return -1


# In[108]:


name='Muhammad Sufiyan Mehboob'
print(name.rindex('i')) #return the index almost rindex(),if value not found return error


# In[110]:


name='Muhammad Sufiyan Mehboob'
print(name.rjust(30)) #return a justified version of string


# In[111]:


name='Muhammad Sufiyan Mehboob'
print(name.rpartition('Sufiyan'))


# In[112]:


name='Muhammad Sufiyan Mehboob'
print(name.rsplit()) #return in list


# In[113]:


name='Muhammad Sufiyan Mehboob'
print(name.rstrip())


# In[114]:


name='Muhammad Sufiyan Mehboob'
print(name.split())


# In[115]:


name='Muhammad Sufiyan Mehboob'
print(name.splitlines()) #return a single work list


# In[118]:


name='Muhammad Sufiyan Mehboob'
print(name.startswith('S'))
name='Muhammad Sufiyan Mehboob'
print(name.startswith('M')) #return true or false if the given character are starting character of whole string


# In[119]:


name='Muhammad Sufiyan Mehboob'
print(name.strip())


# In[120]:


name='Muhammad Sufiyan Mehboob'
print(name.swapcase())  #return first character of every work in lower and other whole string will be UPPER case


# In[123]:


name='muhammad sufiyan mehboob'
print(name.title()) #convert the first character of every word in UPPER Case


# In[124]:


name='Muhammad Sufiyan Mehboob'
print(name.upper()) #return the whole string in upper case


# In[129]:


name='MUHAMMAD SUFIYAN MEHBOOB'
print(name.zfill(25)) #add zeros after the total character of string with includes spaces


# # Now i will use 20 oprands with different oprators

# In[130]:


4*7 - 8*3 + 2*9*7 / 6*10 + 4**9 - 3**7//4*5 - 9*12 + 22*13*7 / 8*7 + 15**9 - 5**9


# In[131]:


7 + 3 - 5 * 0 / 16 + (17 * 34) + 13 - (28 ^ 21) + (14 ** 19) / 15 + 9 - 5 * 2 - 5 + 3 * 10 / 17 + 2 + 18


# In[132]:


9 * 3 + 6 / 4 ** 20 // (12-14)**19/(15+7)**(11/12)


# In[ ]:




