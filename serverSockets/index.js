const WebSocket = require('ws').Server;
const http = require('http').createServer(),
      io = require('socket.io')(http)
const wss = new WebSocket({ port: 8999 });
 
wss.on('connection', function connection(ws) {
  console.log('new connection detect')
  ws.on('message',(data)=>{
    const dataParse = JSON.parse(data)   
    console.log(data)
    io.emit(dataParse.ipAddress,data)
  });
});



http.listen(5000)

