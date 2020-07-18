const WebSocket = require('ws');
 
const ws = new WebSocket('ws://192.168.1.67:8999/');
 
ws.on('open', function open() {
  console.log('connected');
  ws.send('Juan Ama a pia, y se van a casar');
});
 
ws.on('close', function close() {
  console.log('disconnected');
});
 
ws.on('message', function incoming(data) {
  console.log(data);
});