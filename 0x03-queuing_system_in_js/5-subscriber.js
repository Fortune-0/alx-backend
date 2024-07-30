import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function(error) {
  console.log(`Redis client not connected to the server: ${error}`);
});

client.subscribe('holberton school channel');

client.on('message', function(channel, message) {
  console.log(`Received message from channel "${channel}": ${message}`);

  if (message === 'KILL_SERVER') {
    // unsubscribe and quit
    client.unsubscribe('holberton school channel', () => {
        console.log('Unsubscribed from channel: holberton school channel');
        client.quit();
    });
  }
});
