cd /d "%~dp0"
call direnv\Scripts\activate.bat
start cmd /k "uvicorn src.main1:app --reload"
start cmd /k "streamlit run src/app1.py"
