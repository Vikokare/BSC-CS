import streamlit as st
import cyphers.add_cypher

cyphers_options = [ 
    "Additive Cypher", 
    "Muliplicative Cypher", 
    "Addition Multiplication Cypher", 
    "Columner Cypher", 
    "Colmunar Cypher 1", 
    "Playfair Cypher",
    "Vigenere Cypher"
]



cypher_selected_algo = st.selectbox("Select Cipher Algorithm", cyphers_options, key="encrypt_algo")
cypher_message = st.text_input("Enter Message", key="encrypt_message")
cypher_key = st.number_input("Enter Key", min_value=0, step=1, format="%d", key="encrypt_key")

if st.button("Encrypt"):
    if cypher_message and cypher_key:
        try:
            if cypher_selected_algo == "Additive Cypher":
                result = cyphers.add_cypher.cypher(cypher_message, cypher_key, "cypher")
            
            st.write("Result:", result)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both a message and a key.")




decypher_selected_algo = st.selectbox("Select Cipher Algorithm", cyphers_options, key="decrypt_algo")
decypher_message = st.text_input("Enter Message", key="decrypt_message")
decypher_key = st.number_input("Enter Key", min_value=0, step=1, format="%d", key="decrypt_key")

if st.button("Decrypt"):
    if decypher_message and decypher_key:
        try:
            # Call the appropriate function based on the selected algorithm
            if decypher_selected_algo == "Additive Cypher":
                result = cyphers.add_cypher.cypher(decypher_message, decypher_key, "decypher")
            
            st.write("Result:", result)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both a message and a key.")

