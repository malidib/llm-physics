import openai
import os
import pandas as pd
import numpy as np


persona="""
You are a useful coding assistant for a scientist. 
"""
prompt_basic="""You help solve specific physics problem by writing python code that makes use of domain-specialized python packages, as requested by the scientist. 
Your code is thoroughly commented for clarity and to provide descriptions of the various physics and coding choices made in your solution. 
You should always follow precisely the given instructions without omissions. 

Prompt:
""" 

questionslist=[] # Questions go here (please refer to the list in the paper)

for prompt_specific in questionslist:


    prompt = prompt_basic+ prompt_specific
    print ("Input to LLM: " , prompt)

    

    messages = [ {
        "role": "system",
        "content": persona
      },
      {
        "role": "user",
        "content": prompt
      }
    ]

    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages,
    temperature=0.,
    )

    
    
    #print ("LLM: ",response.choices[0].message["content"]) 
    print ("Output of LLM:\n",response.choices[0].message["content"]) 

    print('-----------------------------------------------------------------------')
    print('-----------------------------------------------------------------------')
    print('-----------------------------------------------------------------------')

