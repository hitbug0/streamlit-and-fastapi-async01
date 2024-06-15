cd /d "%~dp0"
call direnv\Scripts\activate.bat
start cmd /k "uvicorn src.main2:app --reload"
start cmd /k "streamlit run src/app2.py"
