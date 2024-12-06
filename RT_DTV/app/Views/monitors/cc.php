<?= $this->extend('template') ?>



<?= $this->section('content') ?>

    <input type = 'button' value = 'cc' onclick = "ccc()"></input>
    <script>
        $(document).ready(function() {
            console.log("Hello World!");

        })
        var socket
        connectWebSocket();
        function ccc()
        {
            if (socket.readyState === WebSocket.OPEN) {
                console.log("向後端發送啟動訊號");
                socket.send("start");
            }
        }
        function connectWebSocket()
        {
            socket = new WebSocket("ws://100.78.179.98:6789");

            socket.onopen = () => {
                console.log("WebSocket 已連線");
            };

            socket.onmessage = (event) => {
                alert('cc')
                const data = JSON.parse(event.data);
                console.log("接收到事件通知:", data);

                if (data.event === "ccc") {
                    console.log('cc')
                }
            };

            socket.onclose = () => {
                console.log("WebSocket 已關閉");
            };

            socket.onerror = (error) => {
                console.error("WebSocket 錯誤:", error);
            };

                    }
    </script>
<?= $this->endSection() ?>
