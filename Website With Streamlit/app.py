import streamlit as st

# --------- Page Config ---------
st.set_page_config(page_title="My Portfolio", page_icon="🌟", layout="centered")

# --------- Header Section ---------
st.title("👨‍💻 Asad's Portfolio")
st.subheader("Python Developer | Tech Learner | Project Explorer")

# --------- About Section ---------
st.markdown("---")
st.header("📌 About Me")
st.write("""
Hey there! I'm Asad, a passionate learner and developer who loves solving problems with code.
I've been exploring Python, building apps, and working on awesome beginner projects.
""")

# --------- Skills Section ---------
st.markdown("---")
st.header("🧠 Skills")
st.write("""
- 💻 Python (Basics, Projects)
- 🐍 Streamlit Apps
- 🧮 Problem Solving
- 📚 Constant Learning
""")

# --------- Projects Section ---------
st.markdown("---")
st.header("🚀 Projects")
st.write("""
- ✅ BMI Calculator  
- ✅ To-Do List App  
- ✅ Guess the Number Game  
- ✅ Rock Paper Scissors  
- ✅ Contact Book  
""")

# --------- Contact Form ---------
st.markdown("---")
st.header("📬 Contact Me")
st.write("Got an idea or want to connect? Send me a message!")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send")

    if submit:
        st.success("Message sent! I'll get back to you soon 🚀")

# --------- Footer ---------
st.markdown("---")
st
