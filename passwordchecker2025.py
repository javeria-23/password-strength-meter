import re
import streamlit as st

st.set_page_config(page_title="Password Strength Checker by Javeria Tariq",page_icon="🌘",layout="centered")
st.markdown("""
<style> 
        .main {text-align:center;}
        .stTextInput{width:60% !important; margin:auto;} 
        .stButton button{width:50%; background-color #4CAF50; color: white; font-size:18px;}
        .stButton button:hover{background-color:#45a049;} 
</style> 
    """,unsafe_allow_html=True)

#page title and desciption
st.title("Password Strength Generator:")
st.write("Enter your password below to check its security level. 🔍")

def check_password_strength(password):
    score=0
    Feedback=[]
    if len (password )>=8:
        score+=1
    else:
        Feedback.append(" ❌ Password should be ** atleast 8 character ** long")

        if re.search(r"[A to Z]",password) and re.search(r"[a to z]",password):
            score+=1
        else:
            Feedback.append(" ❌ Password should include **both uppercase[A-Z] and lowercase [a-z] letters**")
        if re.search(r"\d",password):
            score+=1
        else:
            Feedback.append(" ❌ Password should include **atleast one number (0-9)**")

#Special Character
        if re.search(r"[!@#$%^&*]",password):
            score+=1
        else:
            Feedback.append(" ❌ Password should include ""atleast one Special character [!@#$%^&*]**")

#Display password Strength result
        if score==4:
            st.success("✔️ ""Strong password"" - Your password is secure")
        elif score==3:
            st.info(" ⚠️ ** Moderate password** - Consider improving security by adding more feature")
        else:
            st.error(" ❌ ""Week password"" - Follow the suggestion below to strength it")
        #feedback
        if Feedback:
            with st.expander(" 🔍 **improve your Password**c"):
                for item in Feedback:
                    st.write(item)
    password =st.text_input("Enter your Password:",type="password",help="Ensure your password is strong🔐")
    #Button Working
    if st.button("Check Strength"):
     if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first")
