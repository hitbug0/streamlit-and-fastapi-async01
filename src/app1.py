import threading

import requests
import streamlit as st
from streamlit.runtime.scriptrunner import add_script_run_ctx

SERVER_URL = "http://127.0.0.1:8000"


def button_action(time_, words_):
    response = requests.get(f"{SERVER_URL}/wait/{time_}/{words_}")
    st.session_state["response" + words_[-1]] = response.json()
    print(response.json())  # こっちはコマンドプロンプトに表示される


thread1 = None
thread2 = None
if __name__ == "__main__":

    if "response1" not in st.session_state:
        st.session_state["response1"] = ""

    if "response2" not in st.session_state:
        st.session_state["response2"] = ""

    col1, col2 = st.columns(2)
    b1 = col1.empty()
    t1 = col1.empty()

    b2 = col2.empty()
    t2 = col2.empty()

    time1 = t1.slider("wait time 1", 0.02, 5.0, step=0.01)
    time2 = t2.slider("wait time 2", 0.02, 5.0, step=0.01)

    if b1.button("Button 1"):
        thread1 = threading.Thread(target=button_action, args=(time1, "Button 1"))
        add_script_run_ctx(thread1)
        thread1.start()

    if b2.button("Button 2"):
        thread2 = threading.Thread(target=button_action, args=(time2, "Button 2"))
        add_script_run_ctx(thread2)
        thread2.start()

    if thread1:
        thread1.join()
        st.rerun()

    if thread2:
        thread2.join()
        st.rerun()

    col1.write(st.session_state.response1)

    col2.write(st.session_state.response2)
