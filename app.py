#!/usr/bin/env python
# coding: utf-8

# In[1]:


#app should be in the base folder, cos app script will call for templates
from flask import Flask, render_template, request


# In[2]:


#make sure that machine work as written by name (if any one can run = __main__)
app=Flask(__name__)


# In[3]:


#decorator - run program before actual program
#route (/) - - always the first directory that it goes to, root folder
#before entering post (i.e. enter) is always in the 'else' state    
#flask will run and throw in the html - - then look for the templates

import joblib 

@app.route("/",methods=["GET","POST"])
def index():
    if request.method =="POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression_DBS")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree_DBS")
        r2 = model2.predict([[rates]])
        return(render_template("index.html",result1=r1, result2 = r2)) 
    else:
        return(render_template("index.html",result1="waiting", result2 = "waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("80"))


# In[ ]:




