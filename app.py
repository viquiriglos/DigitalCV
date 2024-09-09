from pathlib import Path
import streamlit as st
from PIL import Image

#---- PATH SETTINGS---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"CV.pdf"
profile_pic = current_dir/"assets"/"Picture.png"

#---GENERAL SETTINGS----
PAGE_TITLE = "Digital CV | MV CASTRO-R"
PAGE_ICON = ":wave:"
NAME = "Maria Victoria Castro Riglos"
DESCRIPTION = """
PhD in Physics, Researcher, TEM Microscopist, Jr. Data Analyst/Scientist and Developer
"""
EMAIL = "mv.castro@protonmail.com"

SOCIAL_MEDIA = {
    "E-mail" : "mailto:mv.castro@protonmail.com",
    "LinkedIn" : "https://www.linkedin.com/in/victoria-castro-a8b31556/",
    "GitHub" : "https://github.com/viquiriglos",
    "Jovian" : "https://jovian.ai/viquiriglos",
}

PROJECTS = {
    " 📊 Would we survive our development?" : "EDA. Interactive dashboard performed using python: Dash-Plotly, pandas, numpy and matplotlib libraries. The data was obtained from World Bank. The project repository is available on GitHub. The dashboard is deployed in render.com. https://development-vs-co2.onrender.com",
    " 📈 Which Autonomous Community in Spain is more adequate for remote workers in terms of housing opportunities?" : "Interactive BI Dashboard: Data obtained from Kaggle and Photovoltaic Information System. https://public.tableau.com/app/profile/victoria.castro5625/viz/Rents_in_Spain/Dashboard1?publish=yes",
    " 🤖 Yearly income in the US in 1994" : "Machine Learning: In this work it was predicted whether the citizens income in USA in1994 exceeded fifty thousand dollars a year, so it is a binary classification task. The census dataset contained 142521 rows and 12 columns. Libraries used: pandas, numpy, plotly.express, scikit learn. Tasks performed: cleaning, identifying numerical and categorical features, imputing missing values and scaling numerical features, encoding categorical features, splitting the data (train and validation sets), fit and train 3 models, tuning hyperparameters. Accuracy Obtained: around 95%. https://jovian.ai/viquiriglos/us-census-1994",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#----LOAD CSS, PDF AND PROFILE PICTURE
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#--- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "Download Resume",
        data = PDFbyte,
        file_name = resume_file.name,
        mime = "application/octet-stream",
    )
    #st.write("e-Mail", EMAIL)
    #for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    #    st.write(f"[{platform}]({link})")


# ---SOCIAL LINKS ----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
st.write("---")

# ---PROGRAMMING SKILLS ---
st.write("#")
st.subheader("Programming Skills")
st.write(
    """
    -	Languages: Python, SQL, Javascript
    -	Web Development: Git & GitHub, Django, Flask, HTML, CSS, Bootstrap, Jupyter Lab, Google Colab, Replit.
    -	Visualization Tools: Dash, Streamlit, Plotly Express, Matplotlib, Seaborn, Tableau 
    -	Data Analysis and Machine Learning: pandas, numpy, Scikit Learn, Pytorch. Experience with classification, regression and GANs.

    """
)

# --- PROJECTS ---
st.write("#")
st.subheader("Projects")
# cols = st.columns(len(PROJECTS))
# for index, (project, link) in enumerate(PROJECTS.items()):
#     cols[index].write(f"[{project}]({link})")

#---Proy 1
#st.write("#")
st.write("📊","**EDA. Interactive dashboard: 'Would we survive our development?'**")
st.write("""
- Libraries and tools: python, Dash-Plotly, pandas, numpy and matplotlib. 
- Data: obtained from World Bank. The project repository is available on my GitHub.
- Link: https://development-vs-co2.onrender.com"
""")

#---Proy 2
st.write("#")
st.write("📈", "**Interactive BI Dashboard:'Which Autonomous Community in Spain is more adequate for remote workers in terms of housing opportunities?'**")
st.write("""
- Tools: Tableau Public
- Data: obtained from Kaggle and Photovoltaic Information System.
- Link: https://public.tableau.com/app/profile/victoria.castro5625/viz/Rents_in_Spain/Dashboard1?publish=yes
""")

#---Proy 3
st.write("#")
st.write("🤖", "**Machine Learning (Notebook):'Yearly income in the US in 1994'**")
st.write("""
- Problem: Binary classification problem. 
- Tools: pandas, numpy, plotly.express, scikit learn.
- Data: The census dataset contained 142521 rows and 12 columns.  
- Tasks performed: cleaning, identifying numerical and categorical features, imputing missing values and scaling numerical features, encoding categorical features, splitting the data (train and validation sets), fit and train 3 models, tuning hyperparameters. 
- Accuracy Obtained: around 95%. 
- Link: https://jovian.ai/viquiriglos/us-census-1994
""")

#---Proy 4
st.write("#")
st.write("🌐", "**Web Page: 'Astroworld'**")
st.write("""
- Tools: Git, HTML, CSS, Bootstrap, python, Flask.
- Code: Code hosted on GitHub (https://github.com/viquiriglos/Astro-page)
- Link: https://astroworld.onrender.com/
""")


# ---- EXPERIENCE AND QUALIFICATIONS ---
st.write("#")
st.subheader("Experience as a Researcher")
st.write(
    """
    -	Researcher at Argentinean National Council of Science and Technology, Conicet (2013 – 2021). 
    -	Specialist in Transmission Electron Microscopy (TEM) and other characterization techniques for Material Science Research.
    -	Experience in teaching, publishing and managing research projects.
    """
)

# --- LANGUAGES ---
st.write("#")
st.subheader("Languages")
st.write(
    """
    - High level of English (C1 certified), Spanish (native).
    - Fluent communication in Portuguese (not certified).
    - Basic knowledge in German and French (A1 certification in both).
    """
)

