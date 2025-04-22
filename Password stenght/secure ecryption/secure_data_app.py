import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Session state setup
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}  # {encrypted_text: {encrypted_text, passkey_hash}}
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "login_required" not in st.session_state:
    st.session_state.login_required = False

# Generate a fixed Fernet key (for demo purposes)
# In real scenarios, load this securely from a .env or config
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# Hashing function
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Encrypt
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

# Decrypt
def decrypt_data(encrypted_text, passkey):
    passkey_hash = hash_passkey(passkey)
    for stored_encrypted_text, stored_data in st.session_state.stored_data.items():
        if stored_encrypted_text == encrypted_text:
            if stored_data["passkey"] == passkey_hash:
                st.session_state.failed_attempts = 0
                return cipher.decrypt(encrypted_text.encode()).decode()
            else:
                st.session_state.failed_attempts += 1
                return None
    return None

# Login check
def require_login():
    st.session_state.login_required = True
    st.experimental_rerun()

# Navigation
st.title("🛡️ Secure Data Encryption System")
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

# Home Page
if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.markdown("Use this app to **securely store and retrieve data** using a passkey.")
    st.markdown("Built with 🔐 encryption and 🧠 in-memory storage.")

# Store Data
elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter your secret data:")
    passkey = st.text_input("Enter a passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            encrypted_text = encrypt_data(user_data)
            passkey_hash = hash_passkey(passkey)

            st.session_state.stored_data[encrypted_text] = {
                "encrypted_text": encrypted_text,
                "passkey": passkey_hash
            }

            st.success("✅ Data stored securely!")
            st.code(encrypted_text, language="text")
        else:
            st.error("⚠️ Both data and passkey are required!")

# Retrieve Data
elif choice == "Retrieve Data":
    if st.session_state.failed_attempts >= 3:
        require_login()

    st.subheader("🔍 Retrieve Your Data")
    encrypted_input = st.text_area("Enter the encrypted text:")
    passkey_input = st.text_input("Enter your passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_input and passkey_input:
            decrypted = decrypt_data(encrypted_input, passkey_input)
            if decrypted:
                st.success("✅ Decrypted successfully!")
                st.code(decrypted, language="text")
            else:
                attempts_left = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts remaining: {attempts_left}")
                if st.session_state.failed_attempts >= 3:
                    st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
                    st.session_state.login_required = True
                    st.experimental_rerun()
        else:
            st.error("⚠️ Both fields are required!")

# Login Page
elif choice == "Login":
    st.subheader("🔐 Reauthorization Required")
    login_pass = st.text_input("Enter master password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":  # Replace with environment check in real app
            st.session_state.failed_attempts = 0
            st.session_state.login_required = False
            st.success("✅ Login successful! You can now try again.")
        else:
            st.error("❌ Incorrect master password.")
