import streamlit as st 
import trigram as tg

if __name__=='__main__':
    st.title("Restore Vietnamese accent marks")
    instruction = 'Please enter the unaccented sentence'
    #st.write(instruction)
    
    input = st.text_input("Your text:")

    st.write(tg.trigram(input))

    
