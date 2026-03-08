import streamlit as st

st.set_page_config(page_title="Ajaz Ahmad Mir", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.header{
background:linear-gradient(90deg,#1e3c72,#2a5298);
padding:25px;
border-radius:10px;
color:white;
}
.section{
background:#f4f6fb;
padding:15px;
border-radius:8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class='header'>
<h1>Ajaz Ahmad Mir</h1>
PhD Research Scholar — Water Resources Engineering
</div>
""", unsafe_allow_html=True)

col1,col2 = st.columns([1,3])

with col1:
    st.image("profile.png.png", width=200)

with col2:

    st.markdown("""
**Institution:** Dr B R Ambedkar National Institute of Technology Jalandhar  

📧 gid.ajaz@gmail.com  
📧 ajaz.2019mcivwr010@nitsri.net  
📧 Ajazam.ce.21@nitj.ac.in  
📧 ajaz1@ualberta.ca  

🔗 [Google Scholar](https://scholar.google.ca/citations?user=90WNMHwAAAAJ)  
🔗 [LinkedIn](https://www.linkedin.com/in/ajaz-mir-40342b1a8/)  
🆔 ORCID: 0000-0002-4164-4027  

Scopus Author ID: 57219854867  
Scopus Author ID: 58806681700
""")

# ---------------- AREAS OF INTEREST ----------------
st.subheader("🔬 Areas of Interest")

st.markdown("""
<div class='section'>

• Experimental Hydraulics  
• Sediment Transport  
• Steep Channels  
• Bedform Dynamics  
• Machine Learning in Hydraulics  

</div>
""", unsafe_allow_html=True)

# ---------------- OVDF FELLOWSHIP ----------------
st.subheader("🌍 Overseas Visiting Doctoral Fellowship")

st.markdown("""
<div class='section'>

**Overseas Visiting Doctoral Fellow (OVDF)**  
University of Alberta, Canada  

Funded by **Science and Engineering Research Board (SERB / ANRF)**  
Duration: Sept 2024 – Aug 2025  

Research collaboration on hydraulics, turbulence, and sediment transport modelling.

</div>
""", unsafe_allow_html=True)

# ---------------- EMPLOYMENT ----------------
with st.expander("Professional Background"):
    st.write("""
Research Scholar  
NIT Jalandhar (2022–Present)

Visiting Scholar  
University of Alberta, Canada (2024–2025)
""")

# ---------------- EDUCATION ----------------
with st.expander("Educational Details"):
    st.write("""
MTech – Water Resource Engineering  
NIT Srinagar (2019–2021)

BE – Civil Engineering  
University of Kashmir (2014–2019)
""")

# ---------------- PUBLICATIONS ----------------
with st.expander("Journal Publications"):

    st.write("""
1. Mir AA, Patel M (2025)  
Optimizing bed shear stress prediction in open flow channels.  
Natural Hazards  
DOI: https://doi.org/10.1007/s11069-025-07154-x  

2. Mir AA, Patel M (2024)  
Machine learning approaches for prediction of flow resistance in alluvial channels with bedforms.  
Water Science & Technology  
DOI: https://doi.org/10.2166/wst.2023.396  

3. Mir AA et al. (2024)  
A comparative ensemble approach to bedload prediction using metaheuristic machine learning.  
Scientific Reports  
DOI: https://doi.org/10.1038/s41598-024-75118-5  

4. Mir AA, Patel M (2024)  
Sediment transport and hazards in steep channels.  
Journal of Water Management Modeling  

5. Bassi A, Mir AA, Kumar B, Patel M (2023)  
Prediction of friction factor in mobile bed channels.  
Journal of Hydroinformatics  
DOI: https://doi.org/10.2166/hydro.2023.246  

6. Tabassum T, Mir AA (2023)  
3D printing technology for sustainable construction.  
Materials Today: Proceedings  
DOI: https://doi.org/10.1016/j.matpr.2023.08.013  

7. Mir AA et al. (2023)  
Methane gas and solid waste management in mountainous Srinagar city.  
Journal of Material Cycles and Waste Management  
DOI: https://doi.org/10.1007/s10163-022-01516-4  

8. Kumar R et al. (2024)  
Fly ash concrete modelling using machine learning.  
Asian Journal of Civil Engineering  
DOI: https://doi.org/10.1007/s42107-023-00922-9  
""")

# ---------------- REVIEWER ACTIVITY ----------------
with st.expander("Peer Review Activity"):
    st.write("""
Reviewer for the following journals:

• Physics of Fluids  
• Results in Engineering  
• Cold Regions Science and Technology  
• Biomass Conversion and Biorefinery  
• Additive Manufacturing
""")

# ---------------- CV ----------------
st.subheader("📄 Curriculum Vitae")

with open("ajaz_cv_2_page 30 dec 25.pdf","rb") as file:
    st.download_button(
        label="Download CV",
        data=file,
        file_name="Ajaz_Ahmad_Mir_CV.pdf",
        mime="application/pdf"
    )
