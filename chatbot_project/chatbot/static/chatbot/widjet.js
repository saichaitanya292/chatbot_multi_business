


(function () {
    const business = document.currentScript.getAttribute("data-business") || "coffee";

    // Create chat button
    const button = document.createElement("div");
    button.innerHTML = "💬";
    button.style.position = "fixed";
    button.style.bottom = "20px";
    button.style.right = "20px";
    button.style.background = "#007bff";
    button.style.color = "white";
    button.style.padding = "15px";
    button.style.borderRadius = "50%";
    button.style.cursor = "pointer";
    button.style.zIndex = "9999";

    // Create chat box
    const chatBox = document.createElement("div");
    chatBox.style.position = "fixed";
    chatBox.style.bottom = "80px";
    chatBox.style.right = "20px";
    chatBox.style.width = "300px";
    chatBox.style.height = "400px";
    chatBox.style.background = "white";
    chatBox.style.border = "1px solid #ccc";
    chatBox.style.display = "none";
    chatBox.style.flexDirection = "column";

    chatBox.innerHTML = `
        <div style="padding:10px;background:#007bff;color:white;">Chatbot</div>
        <div id="messages" style="flex:1;overflow:auto;padding:10px;"></div>
        <input id="input" placeholder="Type..." style="width:100%;padding:10px;" />
    `;

    document.body.appendChild(button);
    document.body.appendChild(chatBox);

    // Toggle chat
    button.onclick = () => {
        chatBox.style.display = chatBox.style.display === "none" ? "flex" : "none";
    };

    // Send message
    chatBox.querySelector("#input").addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
            const msg = this.value;
            this.value = "";

            fetch(`http://127.0.0.1:8000/${business}/chat/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ message: msg })
            })
            .then(res => res.json())
            .then(data => {
                const messages = chatBox.querySelector("#messages");
                messages.innerHTML += `<div><b>You:</b> ${msg}</div>`;
                messages.innerHTML += `<div><b>Bot:</b> ${data.bot}</div>`;
                messages.scrollTop = messages.scrollHeight;
            });
        }
    });
})();