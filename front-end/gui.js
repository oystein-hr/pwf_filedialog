var ws = new WebSocket("ws://127.0.0.1:5001");

ws.onmessage = function (event) {
    recieve.textContent = event.data;
}

function buttonClick() {
    ws.send('click');
}