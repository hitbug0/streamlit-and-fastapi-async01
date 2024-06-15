# awaitは、async関数の実行結果が確定するまで待つためのキーワード
# 複数タスクを投げっぱなしにする→最後だけ揃えるというデザインパターンをすると、簡単に並列化っぽいことができる

import asyncio
import time

import requests
import streamlit as st


def main():
    st.subheader("UIレンダリングにおける同期/非同期")
    st.write(
        """
        UIレンダリングの方式(同期/非同期)による動作の違いを実演する.
        - UI要素$E_1, E_2, E_3$の表示命令を、この順に$dt$ [s]間隔で実行する.
        - $E_i$の表示所要時間は$t_i$ [s]とする.
        """
    )

    col_setting, _, col_result = st.columns([3, 1, 2])
    col_setting.write("### 設定")
    col_result.write("### 実行結果")
    mode = col_setting.radio(
        "実行モードの選択",
        [
            "同期",
            ":rainbow[非同期]",
        ],
    )
    t1 = col_setting.slider(
        "$t_1$ [s]", min_value=0.0, max_value=10.0, value=4.0, step=0.5
    )
    t2 = col_setting.slider(
        "$t_2$ [s]", min_value=0.0, max_value=10.0, value=5.0, step=0.5
    )
    t3 = col_setting.slider(
        "$t_3$ [s]", min_value=0.0, max_value=10.0, value=0.5, step=0.5
    )
    dt = col_setting.slider(
        "$dt$ [s]", min_value=0.0, max_value=5.0, value=1.0, step=0.5
    )

    button = col_setting.button("レンダリング開始")

    if button:
        if mode == "同期":
            start = time.time()
            disp("$E_1$", t1, col_result)
            time.sleep(dt)
            disp("$E_2$", t2, col_result)
            time.sleep(dt)
            disp("$E_3$", t3, col_result)
        else:
            start = time.time()
            asyncio.run(runner({"$E_1$": t1, "$E_2$": t2, "$E_3$": t3}, dt, col_result))
            # disp(4, col_result)

        t_total = time.time() - start
        col_result.write(f"実行モード: {mode}")
        col_result.write(f"所要時間: {t_total:.2f} s")


def disp(e, t, div):
    e_ = processing(e, t)
    div.write(e_)


async def disp_async(e, t, div):
    e_ = await processing_async(e, t)
    div.write(e_)


def processing(e, t):
    time.sleep(t)
    return e


async def processing_async(e, t):
    await asyncio.sleep(t)
    return e


async def runner(dict_, dt, div):
    tasks = []
    for e, t in dict_.items():
        task = asyncio.create_task(disp_async(e, t, div))
        tasks.append(task)
        await asyncio.sleep(dt)

    await asyncio.gather(*tasks)


async def send_request(x):
    url = "http://localhost:8000/calculate"
    response = requests.post(url, json={"x": x})
    if response.status_code == 200:
        result = response.json().get("result")
        st.write(f"The result for {x} is {result}")
    else:
        st.write("Failed to get a response")


if __name__ == "__main__":
    main()
