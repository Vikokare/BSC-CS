import streamlit as st

import cyphers.add_cypher
import cyphers.multi_cypher
import cyphers.add_multi_cypher
import cyphers.columner_cypher
import cyphers.colmuner1_cypher
import cyphers.playfair_cypher
import cyphers.vigenere_cypher

cyphers_options = [ 
    "Additive Cypher", 
    "Muliplicative Cypher", 
    "Addition Multiplication Cypher", 
    "Columner Cypher", 
    "Colmunar Cypher 1", 
    "Playfair Cypher",
    "Vigenere Cypher"
]

st.markdown("""
    <style>
    .block-container {
        padding-top: 10vh;  /* Adjust top padding for vertical centering */
        padding-bottom: 10vh;  /* Adjust bottom padding for vertical centering */
        padding-left: 8rem;
        padding-right: 8rem;
        max-width: 100%;
    }
    .css-18e3th9 {
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .stColumn > div {
        padding: 0 2rem;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

selected_algo = st.selectbox("Select the Cypher", cyphers_options)

col1, col2 = st.columns(2)

with col1:
    st.header("Encryption")

    if selected_algo == cyphers_options[0]:
        message = st.text_input("Enter a message", key="cy_msg")
        key = st.number_input("Enter a key number", step=1, key="cy_key")

        if st.button("Cypher"):
            print("----------", list(message), key)
            result = cyphers.add_cypher.cypher(list(message), key, "cypher")
            st.write("Cyphered message: ", result)


    elif selected_algo == cyphers_options[1]:
        message = st.text_input("Enter a message", key="cy_msg").upper()
        key = st.selectbox("Select a key", [3, 5, 7, 9], key="cy_key")

        if st.button("Cypher"):
            print("----------", list(message), key)
            result = cyphers.multi_cypher.cypher(list(message), key, "cypher")
            st.write("Cyphered message: ", result)


    elif selected_algo == cyphers_options[2]:
        message = st.text_input("Enter a message", key="cy_msg").upper()
        add_key = st.number_input("Enter a key number", step=1, key="cy_key1")
        mul_key = st.selectbox("Select a key", [3, 5, 7, 9], key="cy_key2")

        if st.button("Cypher"):
            print("----------", list(message), add_key, mul_key)
            result = cyphers.add_multi_cypher.cypher(list(message), add_key, mul_key, "cypher")
            st.write("Cyphered message: ", result)


    elif selected_algo == cyphers_options[3]:
        message = st.text_input("Enter a message", key="cy_msg")
        key = st.number_input("Enter a key number", max_value=len(message),step=1, key="cy_key")

        if st.button("Cypher"):
            print("----------", list(message), key)
            result = cyphers.columner_cypher.cypher(list(message), key, "cypher")
            st.write("Cyphered message: ", result[0])
            st.write("Decypher key: ", result[1])


    elif selected_algo == cyphers_options[4]:
        message = st.text_input("Enter a message", key="cy_msg")
        key = st.text_input("Enter a key", max_chars=len(message), key="cy_key")

        if st.button("Cypher"):
            print("----------", list(message), list(key), len(key) )
            result = cyphers.colmuner1_cypher.cypher(list(message), list(key), len(key), "cypher")
            st.write("Cyphered message: ", result[0])
            st.write("Decypher key: ", result[1])


    elif selected_algo == cyphers_options[5]:
        message = st.text_input("Enter a message", key="cy_msg")
        key = st.text_input("Enter a key", key="cy_key")

        if st.button("Cypher"):
            print("----------", list(message), key)
            result = cyphers.playfair_cypher.cypher(list(message), key, "cypher")
            st.write("Cyphered message: ", result)


    elif selected_algo == cyphers_options[6]:
        message = st.text_input("Enter a message", key="cy_msg").upper()
        key = st.text_input("Enter a key", key="cy_key").upper()

        if st.button("Cypher"):
            print("----------", list(message), list(key))
            result = cyphers.vigenere_cypher.cypher(list(message), list(key), "cypher")
            st.write("Cyphered message: ", result)




with col2:
    st.header("Decryption")

    if selected_algo == cyphers_options[0]:
        message = st.text_input("Enter a message", key="decy_msg")
        key = st.number_input("Enter a key number", step=1, key="decy_key")

        if st.button("Decypher"):
            print("----------", list(message), key)
            result = cyphers.add_cypher.cypher(message, key, "decypher")
            st.write("Decyphered message: ", result)


    elif selected_algo == cyphers_options[1]:
        message = st.text_input("Enter a message", key="decy_msg")
        key = st.selectbox("Select a key", [3, 5, 7, 9], key="decy_key")

        if st.button("Decypher"):
            print("----------", list(message), key)
            result = cyphers.multi_cypher.cypher(message, key, "decypher")
            st.write("Decyphered message: ", result)


    elif selected_algo == cyphers_options[2]:
        message = st.text_input("Enter a message", key="decy_msg")
        add_key = st.number_input("Enter a key number", step=1, key="decy_key1")
        mul_key = st.selectbox("Select a key", [3, 5, 7, 9], key="decy_key2")

        if st.button("Decypher"):
            print("----------", list(message), add_key, mul_key)
            result = cyphers.add_multi_cypher.cypher(message, add_key, mul_key, "decypher")
            st.write("Decyphered message: ", result)


    elif selected_algo == cyphers_options[3]:
        message = st.text_input("Enter a message", key="decy_msg")
        key = st.number_input("Enter a key number", max_value=len(message),step=1, key="decy_key")

        if st.button("Decypher"):
            print("----------", list(message), key)
            result = cyphers.columner_cypher.cypher(message, key, "decypher")
            st.write("Decyphered message: ", result[0])


    elif selected_algo == cyphers_options[4]:
        message = st.text_input("Enter a message", key="decy_msg")
        key = st.text_input("Enter a key number", max_chars=len(message), key="decy_key")

        if st.button("Decypher"):
            print("----------", list(message), list(key), len(key))
            result = cyphers.colmuner1_cypher.cypher(list(message), list(key), len(key), "decypher")
            st.write("Decyphered message: ", result[0])


    elif selected_algo == cyphers_options[5]:
        message = st.text_input("Enter a message", key="decy_msg")
        key = st.text_input("Enter a key", key="decy_key")
    
        if st.button("Decypher"):
            print("----------", list(message), key)
            result = cyphers.playfair_cypher.cypher(message, key, "decypher")
            st.write("Decyphered message: ", result)


    elif selected_algo == cyphers_options[6]:
        message = st.text_input("Enter a message", key="decy_msg").upper()
        key = st.text_input("Enter a key", key="decy_key").upper()
    
        if st.button("Decypher"):
            print("----------", list(message), list(key))
            result = cyphers.vigenere_cypher.cypher(list(message), list(key), "decypher")
            st.write("Decyphered message: ", result)