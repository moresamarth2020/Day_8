#!/usr/bin/env python
# coding: utf-8

# # String methods
# - Python provides a set of built-in methods that we can use to alter and modify the strings. 
# - String is immutable in python
# - It will convert into new string but not change existing string
# ### upper() :
# - The upper() method converts a string to upper case.
# - Example:

# In[1]:


a = "Samarth"
print(a.upper()) #it will convert into new string but not change existing string


# ### lower()
# - The lower() method converts a string to lower case.
# - Example:

# In[2]:


b = "Samarth"
print(b.lower())#it will convert into new string but not change existing string


# ### rstrip() :
# - The rstrip() removes any trailing characters. Example:

# In[3]:


a = "Samarth!!!!!"
print(a.rstrip("1"))


# ### replace() :
# - The replace() method replaces all occurences of a string with another string. 
# - Example:

# In[1]:


a = "Samarth"
print(a.replace("Samarth","More"))


# In[3]:


a = """Samarth is a dedicated student who always strives to do his best. 
Samarth enjoys learning new things and takes every opportunity to grow. 
Whether it’s studying for exams or working on projects,
Samarth stays focused and motivated. 
Samarth believes that hard work and consistency are the keys to success.
With a positive attitude and strong determination, Samarth continues to improve every day. 
Samarth’s teachers appreciate his curiosity and discipline, making Samarth a role model among peers."""
print(a.replace("Samarth","More"))


# ### split() :
# - The split() method splits the given string at the specified instance and returns the separated strings as list items.
# - Example:

# In[5]:


Full_name = "More Samarth Nagesh"
print(Full_name.split(" "))


# ### capitalize() :
# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

# In[6]:


Blog_heading = "introduction to python"
print(Blog_heading.capitalize())


# In[7]:


Blog_heading = "introduction tO pyTHon"
print(Blog_heading.capitalize())


# ### center() :
# - The center() method aligns the string to the center as per the parameters given by the user.
# - Example:

# In[32]:


Str1 = "Wellcome to Samarths Home"
len(Str1)
print(len(Str1))


# In[33]:


Str1 = "Wellcome to Samarths Home"
len(Str1)
print(Str1.center(50))


# In[34]:


Str1 = "Wellcome to Samarths Home"
len(Str1)
print(len(Str1.center(50)))


# ### count() :
# - The count() method returns the number of times the given value has occurred within the given string.
# - Example:

# In[35]:


a = """Samarth is a dedicated student who always strives to do his best. 
Samarth enjoys learning new things and takes every opportunity to grow. 
Whether it’s studying for exams or working on projects,
Samarth stays focused and motivated. 
Samarth believes that hard work and consistency are the keys to success.
With a positive attitude and strong determination, Samarth continues to improve every day. 
Samarth’s teachers appreciate his curiosity and discipline, making Samarth a role model among peers."""
print(a.count("Samarth"))


# ### endswith() :
# - The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
# - Example :

# In[36]:


a = "Samarth More !!!!"
print(a.endswith("!!"))


# In[38]:


b = "Samarth More !!!!"
print(b.endswith("??"))


# In[42]:


c = "Samarth More"
print(c.endswith("th",3,7))


# ### find() :
# - The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
# - Example:

# In[46]:


N = """Samarth is a dedicated student who always strives to do his best. 
Samarth enjoys learning new things and takes every opportunity to grow. 
Whether it’s studying for exams or working on projects,
Samarth stays focused and motivated. 
Samarth believes that hard work and consistency are the keys to success.
With a positive attitude and strong determination, Samarth continues to improve every day. 
Samarth’s teachers appreciate his curiosity and discipline, making Samarth a role model among peers."""
print(N.find("is"))


# ### isalnum() :
# - The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
# - Example:

# In[49]:


str1 = "SamarthMore001"
print(str1. isalnum())


# ### isalpha() :
# - The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

# In[50]:


str2 = "SamarthMore001"
print(str2.isalpha())


# In[51]:


str2 = "SamarthMore"
print(str2.isalpha())


# ### islower() :
# - The islower() method returns True if all the characters in the string are lower case, else it returns False.

# In[54]:


str3 = "Samarth More"
print(str3.islower())


# In[55]:


str3 = "samarth more"
print(str3.islower())


# ### isprintable() :
# - The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
# - Example :

# In[57]:


str4 = "Samarth More\n"
print(str4.isprintable())


# In[58]:


str4 = "Samarth More"
print(str4.isprintable())


# ### isspace() :
# - The isspace() method returns True only and only if the string contains white spaces, else returns False.
# - Example:

# In[59]:


str5 = "          "
print(str5.isspace())


# ### istitle() :
# - The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
# - Example:

# In[73]:


d = "Samarth is a dedicated student who always strives to do his best."
print(d.istitle())


# In[74]:


d = "Samarth Is A Dedicated Student Who Always Strives To Do His Best."
print(d.istitle())


# ### isupper() :
# - The isupper() method returns True if all the characters in the string are upper case, else it returns False.
# - Example :

# In[76]:


e = "SAMARTH NAGESH MORE"
print(e.isupper())


# ### startswith() :
# - The endswith() method checks if the string starts with a given value. If yes then return True, else return False.
# - Example :

# In[79]:


str6 = "Samarth Nagesh More"
print(str6.startswith("Samarth"))


# ### swapcase() :
# - The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

# In[82]:


e = "SAMARTH NAGESH MORE"
print(e.swapcase())


# In[83]:


e = "samarth nagesh more"
print(e.swapcase())


# ### title() :
# - The title() method capitalizes each letter of the word within the string.
# - Example:

# In[85]:


str = "Well come to More groups"
print(str.title())


# In[ ]:




