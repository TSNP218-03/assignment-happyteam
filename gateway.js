var http = require('http').Server();
var port = 55555; 

var io = require('socket.io')(http);

http.listen(port, function() {
    console.log("debug: gateway is running on :" + port);
});

io.on('connect', function(socket) {
    console.log("client: <" + socket.id + "> is connected.");

    socket.emit('msg1', "This is a message 1.");

    socket.on('disconnect', function() {
        console.log("client: <" + socket.id + "> is disconnected.");
    });
});