#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Back-end for index.html front-end
#Common back-end technology: Flask, Django, Node.js
#Common front-end technology: React (Facebook), Angular (Google)


# In[2]:


from flask import Flask, render_template, request
import joblib


# In[3]:


app = Flask(__name__)


# In[4]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        print(rate)
        model = joblib.load("DBS_Prediction")
        pred = model.predict([[rate]])
        return(render_template("index.html", result = "SGD$ " + str(pred)))
    else:
        return(render_template("index.html", result ="waiting")) 


# In[5]:


if __name__ == "__main__":
    app.run()


# In[ ]:




