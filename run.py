import streamlit as st 
st.write("Hello world")
def toast_out():
    st.toast("Submitted",icon='👍')
option = st.selectbox("Countries",("India","United States","Saudi Arabia","Brazil","International"))

"You Selected: ", option

# Add a selectbox to the sidebar:
add_selectbox = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

"Sidebar Values", add_slider

st.button("Submit",type="primary",on_click=toast_out())