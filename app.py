#Libraries
import streamlit as st

#Configure the page
st.set_page_config(page_title="EncryptX", page_icon="fingerprint", layout="wide")

#Functions
def encryptor(phrase):
    encrypted_phrase = ""
    for letter in phrase:
        n = ord(letter)
        n2 = n + key
        encrypted_c = chr(n2)
        encrypted_phrase = encrypted_phrase + encrypted_c
    return encrypted_phrase

def decryptor(phrase):
    decrypted_phrase = ""
    for letter in phrase:
        n = ord(letter)
        n2 = n - key
        decrypted_c = chr(n2)
        decrypted_phrase = decrypted_phrase + decrypted_c
    return decrypted_phrase

#Variables
key = 555

#Main
st.title("Phrase Encryptor/Decryptor :fingerprint")

password = st.text_input('Password')
if password == "key555":
    eord = st.text_input('What do you want to do:(E/D)')
    if eord == "E":
        user_word = st.text_area('Type something to encrypt:')

        encrypted_word = encryptor(user_word)
        st.success(encrypted_word)
    elif eord == "D":
        user_word = st.text_area('Type an encrypted phrase/word to decrypt it:')
        decrypted_word = decryptor(user_word)
        st.success(decrypted_word)


    else:
        st.warning('Please enter a valid action (E = Encrypt, D = Decrypt)')
elif password == "":
    st.warning('Please enter a password')
else:
    st.error('Wrong Password')
