import streamlit as st
import streamlit.components.v1 as com
#import libraries
from transformers import AutoModelForSequenceClassification,AutoTokenizer, AutoConfig
import numpy as np
#convert logits to probabilities
from scipy.special import softmax
from transformers import pipeline


#Set the page configs
st.set_page_config(page_title='TWEET SENTIMENT ANALYSIS',page_icon='🤗',layout='wide')

#welcome Animation
com.iframe("https://lottie.host/?file=8c9ae0c8-e9fc-4fc7-954e-16f922db889b/0BlrGUjJxw.json")
st.markdown("<h1 style='text-align: center'> TWEET SENTIMENT FOR COVID VACCINATION </h1>",unsafe_allow_html=True)
st.write("<h2 style='font-size: 24px;'> Text Classification Models developed to ascertain public perception of covid vaccines </h2>",unsafe_allow_html=True)

#Create a form to take user inputs
with st.form(key='tweet',clear_on_submit=True):
    #input text
    text=st.text_area('Please enter tweet of vaccine perception')
    #Set examples
    alt_text=st.selectbox("Choose any of the sample tweets",('-select-', 'Vaccines have been good so far', 'Had a bad experience with the vaccine', 'Covid is human made. The vaccines are deadly', 'Unqualified people administered  vaccine', 'Vaccine is dangerous to women', 'Vaccine can kill people with anaemia', 'Vaccine protects us from the deadly virus'))
    #Select a model
    models={'Bert':'elvis-d/elvis_bert_base',
        'Roberta': 'elvis-d/elvis_roberta'}
    model=st.selectbox('Select preferred model',('Bert','Roberta'))
     #Submit
    submit=st.form_submit_button('Predict','Continue processing input')
    
selected_model=models[model]

#create columns to show outputs
col1,col2,col3=st.columns(3)
col1.write('<h2 style="font-size: 24px;"> Sentiment Emoji </h2>', unsafe_allow_html=True)
col2.write('<h2 style="font-size: 24px;"> Vaccine Perception of User </h2>', unsafe_allow_html=True)
col3.write('<h2 style="font-size: 24px;"> Model Prediction Confidence </h2>', unsafe_allow_html=True)

if submit:
    #Check text
    if text=="":
        text=alt_text
        st.success(f"input text is set to '{text}'")    
    else:
        st.success('Hey, tweet received', icon='👍🏼')
        
    #import the model
    pipe=pipeline(model=selected_model)
    
    
    #pass text to model
    output=pipe(text)
    output_dict=output[0]
    lable=output_dict['label']
    score=output_dict['score']
    
        #output
    if lable=='NEGATIVE' or lable=='LABEL_0':
        with col1:
            com.iframe("https://lottie.host/?file=c8010531-31de-4dc8-8952-1aa854314455/NQNXZWPduv.json")
        col2.write('NEGATIVE')
        col3.write(f'{score*100:.2f}%')
    elif lable=='POSITIVE'or lable=='LABEL_2':
        with col1:
            com.iframe("https://lottie.host/?file=51ba274f-064a-4d67-877b-159f4490a944/pBBe4CCH8e.json")
        col2.write('POSITIVE')
        col3.write(f'{score*100:.2f}%')
    else:
        with col1:
            com.iframe("https://lottie.host/?file=4e8f4b09-bafb-4ff8-9749-2470c459dce1/v5FATJ9QVm.json")
        col2.write('NEUTRAL')
        col3.write(f'{score*100:.2f}%')