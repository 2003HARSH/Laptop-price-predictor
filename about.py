from pathlib import Path

import streamlit as st
from PIL import Image

def app():
    # --- PATH SETTINGS ---
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir  / "main.css"
    profile_pic = current_dir  / "profile-pic.jpg"


    # --- GENERAL SETTINGS ---
    NAME = "Harsh Gupta"
    DESCRIPTION = """
    BCA 5th Semester Student at M.L.K. P.G. College, Balrampur
    """
    EMAIL = "harshnkgupta@gmail.com"
    SOCIAL_MEDIA = {
        "PyPi": "https://pypi.org/user/2003harsh/",
        "LinkedIn": "https://linkedin.com/in/harsh-gupta-2021/",
        "GitHub": "https://github.com/2003HARSH"
    }
    PROJECTS = {
        "🏆 MyFiglet - Figlet Font In Python": "https://pypi.org/project/myfiglet/",
        "🏆 Py4Math- Math help for non math coders": "https://pypi.org/project/py4math/",
        "🏆 Base Changer - A basic number system convereter": "https://pypi.org/project/base-changer/",
    }


    # --- LOAD CSS, PDF & PROFIL PIC ---
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    profile_pic = Image.open(profile_pic)


    # --- HERO SECTION ---
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.write("📫", EMAIL)


    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qulifications")
    st.write(
        """
    - ✔️ 5+ Years Programming Experience
    - ✔️ Strong hands on experience and knowledge in Python
    - ✔️ Good understanding of statistical principles and their respective applications
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """
    )


    # --- SKILLS ---
    st.write('\n')
    st.subheader("Hard Skills")
    st.write(
        """
    - 👩‍💻 Programming: Python (Scikit-learn, Pandas, Tkinter, BeautifulSoup), PHP , C , C++ , JavaScript
    - 📊 Cyber Sceurity : Offensive Penetration Testing , Scripting , Malware Analysis
    - 📚 Modeling: Logistic regression, linear regression, decision trees
    - 🗄️ AI: Deep Learning , Machine Learning , Soft Computing , Fuzzy Logic
    """
    )


    # --- Projects & Accomplishments ---
    st.write('\n')
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")