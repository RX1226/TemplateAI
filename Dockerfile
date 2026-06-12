FROM python:3.12-slim

WORKDIR /app
#指定時區, python內建有搞定
#ENV TZ=Asiz/Taipei \
#    LANG=C.UTF-8 \
#    PYTHONUNBUFFERED=1

# 安裝依賴
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 複製整個專案, 因為Docker架構每個大寫是一層, 所以這樣寫改code不用重裝之前所有的
COPY . .

# FastAPI 必備 port
EXPOSE 8000

# 啟動 server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]