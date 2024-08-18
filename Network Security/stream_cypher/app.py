import streamlit as st
from cyphers.add_cypher import cypher
from cyphers.add_multi_cypher import cypher
from cyphers.colmuner1_cypher import cypher
from cyphers.columner_cypher import cypher
from cyphers.multi_cypher import cypher
from cyphers.playfair_cypher import cypher
from cyphers.vigenere_cypher import cypher

cyphers_options = [ "Additive Cypher", "Muliplicative Cypher", "Addition Multiplication Cypher", "Columner Cypher", "Colmunar Cypher 1", "Playfair Cypher", "Vigenere Cypher"]
selected_algo = st.selectbox("Select Cipher Algorithm", algo_options)

message = st.text_input("Enter Message")
key = st.text_input("Enter Key")
