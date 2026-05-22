import uvicorn
import webbrowser
import threading
import time
import requests


def wait_for_server():
    url = "http://127.0.0.1:8000/health"

    while True:
        try:
            requests.get(url)
            break
        except:
            time.sleep(0.2)

    webbrowser.open("http://127.0.0.1:8000")


if __name__ == "__main__":

    print("🚀 Starting server...")

    threading.Thread(target=wait_for_server, daemon=True).start()

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )