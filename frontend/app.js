// 1️⃣ 先載入 UI config
async function loadUI() {
    const res = await fetch("/ui/config");
    const data = await res.json();

    document.getElementById("title").innerText = data.title;
    document.getElementById("msg").placeholder = data.placeholder;
}

// 2️⃣ chat API
async function send() {
    const message = document.getElementById("msg").value;

    const res = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    });

    const data = await res.json();
    document.getElementById("result").innerText = data.reply;
}

// 3️⃣ 頁面載入時先抓 UI config
loadUI();