import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Ajaz Ahmad Mir | Research Portfolio",
    page_icon="👤",
    layout="centered"
)

# ================= SIDEBAR =================
with st.sidebar:
    st.header("📬 Contact")

    st.write("📧 gid.ajaz@gmail.com")
    st.write("📱 +91-7006231956")
    st.write("📍 NIT Jalandhar, Punjab, India")

    st.markdown("---")
    st.header("🔗 Research Profiles")

    st.markdown(
        "[🎓 Google Scholar]"
        "(https://scholar.google.ca/citations?user=90WNMHwAAAAJ&hl=en&oi=ao)"
    )

# ================= HEADER =================
col1, col2 = st.columns([1, 2])

with col1:
    try:
        st.image("profile.jpg", width=180)
    except:
        st.image("https://via.placeholder.com/180", width=180)

with col2:
    st.title("Ajaz Ahmad Mir")
    st.markdown("### Ph.D. Research Scholar")

    st.write("Dr B R Ambedkar National Institute of Technology Jalandhar")
    st.write("Visiting Doctoral Fellow — University of Alberta")

st.markdown("---")

# ================= EDUCATION =================
st.header("🎓 Education")

st.markdown("""
**University of Alberta, Canada**  
Overseas Visiting Doctoral Fellow (ANRF/OVDF)  
*Sept 2024 – Aug 2025*

**NIT Jalandhar, Punjab, India**  
Ph.D. in Water Resources Engineering  
*2022 – Ongoing*

**NIT Srinagar, J&K, India**  
M.Tech in Water Resource Engineering — CGPA: 7.23  
*2019 – 2021*

**University of Kashmir, J&K, India**  
B.E. in Civil Engineering — 76.6%  
*2014 – 2019*
""")

# ================= PUBLICATIONS =================
st.header("📚 Publications")

st.markdown("""
• Optimizing bed shear stress prediction in open flow channels: heuristic ML techniques. *Natural Hazards*, 2025.  
• Comparative ensemble approach to bedload prediction using metaheuristic ML. *Scientific Reports*, 2024.  
• ML approaches for prediction of flow resistance in alluvial channels. *Water Science and Technology*, 2024.  
• Review on sediment transport and hazards in steep channels. *Journal of Water Management Modeling*, 2024.  
• Methane gas and solid waste management in Srinagar city. *Journal of Material Cycles and Waste Management*, 2022.  
• Friction factor prediction in mobile bed channels. *Journal of Hydroinformatics*, 2023.  
• Flow of fly ash and slag-based concrete using ML. *Asian Journal of Civil Engineering*, 2023.  
• Flexural strength prediction in recycled aggregate concrete. *Iranian Journal of Science and Technology*, 2024.
""")

# ================= PATENT =================
st.header("🧪 Patent & Industrial Design")

st.markdown("""
**Next-Gen Hydraulic Lab Trolley with Precision Control and Instrument Integration**  
Design No.: 475322-001 (Class 10-04)  
Registered with Patent Office, Government of India  
Date of Registration: 29 Sept 2025 | Issue: 24 Dec 2025  

Co-inventors: Shakeel Ahmad Rather, Mahesh Patel, Satyender Singh, Shailza Sharma  
Institutional Collaboration: NIT Jalandhar & ADK Instruments
""")

# ================= PROJECTS =================
st.header("🚀 Projects Assisted")

st.markdown("""
**SPARC, MHRD Govt. of India**  
AI/ML-driven flood prediction and hazard mapping in Himalayan regions  
Funding: ₹60 Lakhs
""")

# ================= PRESENTATIONS =================
st.header("🖼 Poster Presentations")

st.markdown("""
• University of Alberta (2025): Water Quality Index using PCA + hybrid ML  
• CSCE, University of Alberta (2025): Sediment transport modelling using ensemble ML
""")

# ================= CONFERENCES =================
st.header("🎤 Conferences & Workshops")

st.markdown("""
• IAHR-APD, IIT Madras (2022)  
• IAHR Young Professionals Congress (2022)  
• Hydraulics Measurement Techniques — NIT Rourkela (2024)  
• Urban Water Management — GNDEC Ludhiana (2023)  
• Machine Learning with Python — NIT Jalandhar (2022)
""")

# ================= BOOK CHAPTERS =================
st.header("📖 Book Chapters")

st.markdown("""
• Springer Nature (2025): Technological developments in river morphology  
• Geoenvironmental Engineering (2025): Hydrogeological study of soil and water contamination
""")

# ================= ACHIEVEMENTS =================
st.header("🏆 Achievements & Fellowships")

st.markdown("""
• GATE Qualified (2019) — Score: 463  
• ANRF / SERB Overseas Fellowship — $2000/month  
• PhD Fellowship — NIT Jalandhar (₹42,000/month)  
• MTech GATE Fellowship — NIT Srinagar  
• Minority Scholarship — University of Kashmir  
• Session Chair — ICIDEAIA-2025
""")

# ================= SKILLS =================
st.header("🛠 Skills")

st.markdown("""
**Technical:** Machine Learning, Hydraulics, ANSYS, MATLAB, WaterGems  
**Programming:** Python, MATLAB  
**Soft Skills:** Teaching, Project Writing, Team Work
""")

# ================= CV DOWNLOAD =================
st.header("📄 Download CV")

try:
    with open("Ajaz_Ahmad_Mir_CV.pdf", "rb") as file:
        st.download_button(
            label="⬇️ Download Full CV",
            data=file,
            file_name="Ajaz_Ahmad_Mir_CV.pdf",
            mime="application/pdf",
        )
except:
    st.info("Upload your CV PDF to enable download.")

# ================= FOOTER =================
st.markdown("---")
st.caption("© 2026 Ajaz Ahmad Mir | Streamlit Research Portfolio")
