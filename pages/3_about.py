import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="About Us - Kelompok 1 NEO",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="auto",
)

# Judul halaman 
st.title("🌟 About Us - Kelompok 1 NEO 🌟")
st.write("Mari kita kenali anggota-anggota hebat dalam kelompok kami👀")
st.markdown("<br>", unsafe_allow_html=True) 

# Informasi anggota
members = [
    {"nama": "YULIZCHIA MALICA PINKAN T", "ID MSIB": "6467091", "NIM": "4611421040", "Asal Universitas" : "Universitas Negeri Semarang", "Program Studi": "Teknik Informatika", "Role": "Data Engineer", "foto": "yulizz.JPG"},
    {"nama": "SAIDATUL KHALIDAH", "ID MSIB": "6514031", "NIM": "4611421024","Asal Universitas" : "Universitas Negeri Semarang", "Program Studi": "Teknik Informatika", "Role": "ML Engineer", "foto": "lidaa.jpg"},
    {"nama": "KHILWA ANNIDA", "ID MSIB": "6385703", "NIM": "24010120120022","Asal Universitas" : "Universitas Diponegoro", "Program Studi": "Matematika", "Role": "Frontend Engineer", "foto": "khilwa.jpg"},
    {"nama": "NURUL INAYAH", "ID MSIB": "5934750", "NIM": "4401420093", "Asal Universitas" : "Universitas Negeri Semarang", "Program Studi": "Pendidikan Biologi","Role": "Backend Engineer", "foto": "nurull.jpg"},
    {"nama": "NGESTI RAHAYU", "ID MSIB": "7150272", "NIM": "4201420025", "Asal Universitas" : "Universitas Negeri Semarang", "Program Studi": "Pendidikan Fisika", "Role": "Technical Writter", "foto": "NGESTII.jpg"},
    {"nama": "ADITYA SAMASTHA", "ID MSIB": "7167365", "NIM": "4201420078", "Asal Universitas" : "Universitas Negeri Semarang", "Program Studi": "Pendidikan Fisika", "Role": "UI/UX Designer", "foto": "adityaa.jpg"},
]


# Menampilkan informasi anggota
for member in members:
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"### {member['nama']}")
        st.write(f"**ID MSIB:** {member['ID MSIB']}")
        st.write(f"**NIM:** {member['NIM']}")
        st.write(f"**Asal Universitas:** {member['Asal Universitas']}")
        st.write(f"**Program Studi:** {member['Program Studi']}")
        st.write(f"**Role:** {member['Role']}")

    with col2:    
        image = Image.open(member['foto'])
        st.image(image, caption=member['nama'], use_column_width=True, output_format='auto')
    

         # Garis pemisah antar anggota
        col1.markdown("---")
