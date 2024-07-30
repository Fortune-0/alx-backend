import redis from 'redis'

// Create a new Redis client
const client = redis.createClient();

// Connect to the Redis server
client.on('connect', () => {
    console.log('Redis client connected to the server ');
});

// Handle connection errors
client.on('error', (err) => {
    console.error(`Error connecting to Redis server: ${err}`);
});
