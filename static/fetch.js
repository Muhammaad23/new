let socket = new WebSocket("ws://127.0.0.1:8000/ws/chat/");

socket.onopen = function () {
    console.log("WebSocket ochildi");
    socket.send(JSON.stringify({ message: "Salom, WebSocket!" }));
};

socket.onmessage = function (event) {
    console.log("Qabul qilindi:", event.data);
};

socket.onclose = function () {
    console.log("WebSocket yopildi");
};
