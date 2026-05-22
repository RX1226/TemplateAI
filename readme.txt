
FastAPI控制橋梁
安裝fast api
pip install fastapi uvicorn
安裝fast dotenv
pip install python-dotenv

AI功能
Google Ai Studio
https://aistudio.google.com/api-keys
pip install langchain_google_genai
範例在chat.py, 然後去呼叫ai資料夾的模型

DB功能
https://supabase.com/
pip install supabase
創建Table
create table chat_logs (
  id bigint generated always as identity primary key,
  message text,
  reply text,
  created_at timestamp default now()
);
範例在repo.py, 去呼叫db內的功能

Line功能-暫時分開架
https://railway.com/
pip install line-bot-sdk
放另一個檔案

前端Frontend
index.html 是頁面
app.js是串後端範例
ui.py是寫來和前端互動範例

啟動
uvicorn main:app --reload

看結果跟測試
http://127.0.0.1:8000/docs