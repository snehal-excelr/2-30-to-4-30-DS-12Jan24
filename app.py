# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:30:25 2023

@author: excel
"""

import pickle
import streamlit as st

# open model in read binary mode
load = open('clf.pkl','rb')
model = pickle.load(load)


# Define predict function 
def predict(preg,plas,pres,skin,test,mass,pedi,age):
    prediction = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]]) 
    # pass arguments in 2 dimensions using 2 square brackets
    return prediction

def main():
    st.title('Pima Indian Diabetese')
    # Accept values from user through browser
    preg = st.number_input('Pregnancy: ')
    plas = st.number_input('Plasma: ')    
    pres = st.number_input('Pres: ')
    skin = st.number_input('Skin: ')
    test = st.number_input('Test: ')
    mass = st.number_input('Mass: ')
    pedi = st.number_input('Pedigree: ')
    age = st.number_input('Age: ')

#    if st.button('Predict'):
#        result = predict(preg,plas,pres,skin,test,mass,pedi,age)
#        st.success('Diabetic:  {} '.format(result))

    if st.button('Predict'): # if predict button is clicked then execute below code
         result = predict(preg,plas,pres,skin,test,mass,pedi,age)
         if result==0:
             st.success("Non-Diabetic Person")
         else:
             st.success("Diabetic Person")


# When we create app.py file in the backend python will give default global name to this python script file as "__name__"
# 
if __name__ == '__main__': # it will always be true so calls the main() function
    main()
        
        

        
        
        
        
        
        
        