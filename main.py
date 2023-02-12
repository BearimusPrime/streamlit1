import streamlit as st
st.set_page_config(
    page_title="Misiowy Miszmasz",

)

st.title('Misiowy Miszmasz')
st.write("Zamiast rozwalać naukę na kilka/nascie mikro projektow, zrobie z tego swego rodzaju playground")
st.sidebar.success("Wybierz podstrone/subprojekt")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Wpisz tu cokolwiek i zatwierdz przyciskiem. Powinno sie to pojawic na stronie Variable Transfer", st.session_state["my_input"])
submit = st.button("Przycisk")
czysc = st.button("Wyczyść")

if czysc:
    st.session_state["my_input"]=""
    my_input=""

if submit:
    st.session_state["my_input"]=my_input
    st.write("Teraz sprawdz Variable Transfer")