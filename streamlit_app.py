import streamlit as st



st.markdown("<style> .stAppHeader {display:none;} ul {list-style-type: none; } </style>", unsafe_allow_html=True)

from pathlib import Path

def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Pfad zur PDF-Datei
file_path = 'LebensLauf2.pdf'

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)

left,right = st.columns(2)

left.image("Dad.png", width=250)

right.markdown("""
               <h3>Gurmeet GAMKHIL </h3>
                <em>Ich interessiere mich für KI und wie schnell es sich weiterentwickelt.</em>
           """, unsafe_allow_html=True)

right.download_button(label="📄 Download Lebenslauf",
        data=file_bytes,
        file_name=file_path,
        mime='application/pdf')

st.write("📩", "gamkhilg@gmail.com")


st.header("IT-Kompetenzen", anchor=False, divider="blue")

st.write("""
         - 💻 Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit
         - 📱 Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
         - 🏢 Office-Suite: Versierter Umgang mit Microsoft Word, und PowerPoint
        - 📽️ Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting           
            """, unsafe_allow_html=True)

st.header("Arbeitserfahrung", anchor=False, divider="blue")
st.write(" 💼 Berufspraktische Tage 1: Bei Namaste Store von 15. bis 19. Jän. 2024")
st.write(" 💼 Berufspraktische Tage 2: Bei Namaste Store von 18. bis 22. Nov. 2024")


st.header("Zusätzliche Qualifikationen", anchor=False, divider="blue")
st.write(" 🤓 Schnelle Auffassungsgabe für neue Softwareanwendung und Technologien")
st.write(" 😲 Große Interesse an der kontinuierlichen Weiterentwicklung im IT-Bereich")
st.write(" 🥇 Teamfähigkeit und Kommunikationsstärke bei gemeinsamen Coding-Projekten")
st.write(" 🤵‍♂️ Höfflickeit entgegen Kunden und Mitarbeiter")
st.write(" 🎯 Auf die Genauigkeit achten")

st.header("Interessen und Hobbys",anchor=False, divider="blue")
st.write("🖥️ Computerspiele spielen")
st.write(" 🙂 Neue Erfahrungen erleben")
st.write(" 😀 Etwas neues über Computertechnik lernen")

