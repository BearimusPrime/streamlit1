import streamlit as st

def zrob_checki(boxy):
    for i in boxy:
        st.checkbox(i, key='kkk' + i)

def get_selected_checkboxes():
    return [str(i) for i in st.session_state.keys() if i.startswith('kkk') and st.session_state[i]]



st.header('checkboxy:')

boxy = ['jeden', 'dwa', 'trzy', 'cztery', 'pięć']
zrob_checki(boxy)


st.write(st.session_state)
st.write(st.session_state.keys())
st.write(get_selected_checkboxes())
print(get_selected_checkboxes()[2])
