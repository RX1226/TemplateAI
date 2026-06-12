
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
上架的
uvicorn main:app --host 0.0.0.0 --port $PORT

看結果跟測試
http://127.0.0.1:8000/docs

docker
build image
docker build -t image-app:1.0 .
#下面左邊的port是本機的, 右邊是對外的
docker run -p 8000:8000 image-app:1.0

如果要弄多核如下
requirements.txt
內要多安裝gunicorn
Dockfile內要改成
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "-b", "0.0.0.0:8000"]
參數	意思
gunicorn #production server
-w 4 #4 個 worker（CPU 多核心）
uvicorn.workers.UvicornWorker #用 uvicorn 跑 FastAPI
main:app #你的 FastAPI app
-b 0.0.0.0:8000	#對外開 port