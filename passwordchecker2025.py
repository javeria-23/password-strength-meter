import re
import streamlit as st

# Page config and styling
st.set_page_config(page_title="Password Strength Checker by Javeria Tariq", page_icon="🌘", layout="centered")
st.markdown("""
<style> 
    .main {text-align:center;}
    .stTextInput{width:60% !important; margin:auto;} 
    .stButton button{width:50%; background-color: #4CAF50; color: white; font-size:18px;}
    .stButton button:hover{background-color:#45a049;} 
</style> 
""", unsafe_allow_html=True)

# Page title and description
st.title("Password Strength Generator:")
st.write("Enter your password below to check its security level. 🔍")

# Password input
password = st.text_input("Enter your Password:", type="password", help="Ensure your password is strong 🔐")

# Function to check password strength
def check_password_strength(password):
    score = 0
    Feedback = []

    if len(password) >= 8:
        score += 1
    else:
        Feedback.append("❌ Password should be **at least 8 characters** long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        Feedback.append("❌ Password should include **both uppercase [A-Z] and lowercase [a-z] letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        Feedback.append("❌ Password should include **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        Feedback.append("❌ Password should include **at least one special character [!@#$%^&*]**.")

    # Display password strength result
    if score == 4:
        st.success("✔️ Strong password - Your password is secure.")
    elif score == 3:
        st.info("⚠️ Moderate password - Consider improving it by adding missing elements.")
    else:
        st.error("❌ Weak password - Please follow the suggestions below to strengthen it.")

    # Display feedback suggestions
    if Feedback:
        with st.expander("🔍 Improve your Password"):
            for item in Feedback:
                st.write(item)

# Button to trigger strength check
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first.")
