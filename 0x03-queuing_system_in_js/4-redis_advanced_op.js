import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function(error) {
  console.log(`Redis client not connected to the server: ${error}`);
});

// set hash key-value
client.hset('HolbertonSchools', 'Portland', 50, print);
client.hset('HolbertonSchools', 'Seattle', 80, print);
client.hset('HolbertonSchools', 'New York', 20, print);
client.hset('HolbertonSchools', 'Bogota', 20, print);
client.hset('HolbertonSchools', 'Cali', 40, print);
client.hset('HolbertonSchools', 'Paris', 2, print);

// display all the client
client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
        console.error(`Error getting the hash: ${err}`);
    } else {
        console.log(reply);
    }
});
