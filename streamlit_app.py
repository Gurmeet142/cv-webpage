import streamlit as st

st.title("My new app🤡", anchor=False)
st.header("Ich bin eine neue Überschrift💀", anchor=False, )
st.subheader("Noch eine kleinere Überschrift🗿", anchor=False, )
st.write("Das ist meine Streamlit app🍷")

st.markdown("<p>Ich bin ein Text</p>", unsafe_allow_html=True)

st.markdown("<a href='https://www.google.at>Link<a/>", unsafe_allow_html=True)
st.header("IT-Kompetenzen", anchor=False, divider="blue")

st.write("""
         - 💻 Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework) 
         - Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
         - Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
        - Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
         - Schulprojekte: Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen            
            """, unsafe_allow_html=True)

st.header("Arbeitserfahrung", anchor=False, divider="blue")
st.write("Berufspraktische Tage 1: Bei XYZ von 18. bis 22. Nov. 2024")
st.write("Berufspraktische Tage 2: Bei XYZ von 24. bis 28. Feb. 2025")


st.header("Zusätzliche Qualifikationen", anchor=False, divider="blue")
st.write("Schnelle Auffassungsgabe für neue Softwareanwendung und Technologien")
st.write("Große Interesse an der kontinuierlichen Weiterentwicklung im IT-Bereich")
st.write("Teamfähigkeit und Kommunikationsstärke bei gemeinsamen Coding-Projekten")

st.header("Interessen und Hobbys",anchor=False, divider="blue")
st.write("Fußball:Mitglied in einem Fußball-Klub")
st.write("Lesen: Begeisterte Leser verschiedenster Literatur")
st.write("Schach: Engagiert im Schachklub")