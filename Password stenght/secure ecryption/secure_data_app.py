import streamlit as st
from cryptography.fernet import Fernet
import uuid, base64, hashlib, json, os
from datetime import datetime

# —— Page Config ——
st.set_page_config(page_title="Developer Name", page_icon="🌟", layout="centered")

# —— Header with Highlighted Name ——
header_html = """
<h1 style='text-align: center;'>
  👨‍💻 <span style='color: #FF5733;'>Develope </span> <span style='color: #28B463;'>By, </span>
  <span style='color: #FF5733;'>ASAD </span> <span style='color: #28B463;'> SHABIR </span>
</h1>
...
"""
st.markdown(header_html, unsafe_allow_html=True)


# ——— Constants & Setup ———
VAULT_FILE = "vault.json"
KEY_FILE   = "vault.key"
MASTER_PW_HASH = hashlib.sha256("admin123".encode()).hexdigest()  # change in prod!

# 1) Generate or load encryption key
if os.path.exists(KEY_FILE):
    key = open(KEY_FILE, "rb").read()
else:
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f: f.write(key)
cipher = Fernet(key)

# 2) Load/save vault data
def load_vault():
    if os.path.exists(VAULT_FILE):
        txt = open(VAULT_FILE,"r").read().strip()
        return json.loads(txt) if txt else {}
    return {}
def save_vault(d):
    with open(VAULT_FILE,"w") as f:
        json.dump(d, f, indent=4)

vault = load_vault()

# 3) Helpers
def hash_passkey(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

def encrypt_text(plain: str) -> str:
    return cipher.encrypt(plain.encode()).decode()

def decrypt_text(enc: str) -> str:
    return cipher.decrypt(enc.encode()).decode()

# ——— UI ———
st.title("🔐 SecureVault – Encrypted Data Storage")

choice = st.sidebar.selectbox("Navigation", ["Home", "Store Data", "Retrieve Data", "Admin"])

if choice == "Home":
    st.write("""
    Welcome to SecureVault!  
    Use **Store Data** to encrypt & save,  
    **Retrieve Data** to decrypt with your passkey,  
    and **Admin** (master password) to view all entries.
    """)

# —— Store Data ——
elif choice == "Store Data":
    st.subheader("📂 Store Data")
    secret = st.text_area("Enter your secret data")
    pw     = st.text_input("Choose a passkey (to decrypt later)", type="password")

    if st.button("Encrypt & Save"):
        if secret and pw:
            # generate a unique ID for this record
            uid = str(uuid.uuid4())
            rec_id = base64.urlsafe_b64encode(uid.encode()).decode()
            enc_text = encrypt_text(secret)
            vault[rec_id] = {
                "encrypted": enc_text,
                "passkey_hash": hash_passkey(pw)
            }
            save_vault(vault)
            st.success("✅ Data encrypted and stored!")
            st.code(rec_id, language="text")
            st.caption("🆔 Keep this Record ID safe to retrieve your data later.")
        else:
            st.error("⚠️ Both fields are required.")

# —— Retrieve Data ——
elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Data")
    rec_id = st.text_input("Enter your Record ID")
    pw     = st.text_input("Enter your passkey", type="password")

    if st.button("Decrypt"):
        entry = vault.get(rec_id)
        if not entry:
            st.error("❌ Invalid Record ID.")
        elif hash_passkey(pw) != entry["passkey_hash"]:
            st.error("❌ Wrong passkey.")
        else:
            plain = decrypt_text(entry["encrypted"])
            st.success("✅ Decrypted successfully!")
            st.code(plain, language="text")

# —— Admin View ——
elif choice == "Admin":
    st.subheader("🛡️ Admin Login")
    master = st.text_input("Enter master password", type="password")
    if st.button("Login"):
        if hash_passkey(master) == MASTER_PW_HASH:
            st.success("🔓 Admin access granted")
            st.write("### All Stored Records")
            for rid, rec in vault.items():
                st.write(f"- **ID:** `{rid}`  • encrypted: `{rec['encrypted']}`")
        else:
            st.error("❌ Incorrect master password.")

