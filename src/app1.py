import concurrent.futures
import threading
import time

import requests
import streamlit as st
from streamlit.runtime.scriptrunner import add_script_run_ctx

SERVER_URL = "http://127.0.0.1:8000"


def button1_action(c):
    response = requests.get(f"{SERVER_URL}/get1")
    c.write(response.json())  # 表示できない。サブプロセスの処理だからと思われる
    print(response.json())  # こっちはコマンドプロンプトに表示される


def button2_action(c):
    response = requests.get(f"{SERVER_URL}/get2")
    c.write(response.json())  # 表示できない。サブプロセスの処理だからと思われる
    print(response.json())  # こっちはコマンドプロンプトに表示される


if __name__ == "__main__":
    b1 = st.empty()
    b2 = st.empty()
    c1 = st.empty()
    c2 = st.empty()
    if b1.button("Button 1"):
        thread1 = threading.Thread(target=button1_action, args=(c1,))
        add_script_run_ctx(thread1)
        thread1.start()
    if b2.button("Button 2"):
        thread2 = threading.Thread(target=button2_action, args=(c2,))
        add_script_run_ctx(thread2)
        thread2.start()
