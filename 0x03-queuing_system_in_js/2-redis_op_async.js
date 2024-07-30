import redis from 'redis'
import { promisify } from 'util';

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

function setNewSchool(schoolName, value) {
    // Set the value for the specified key
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.error(`Error setting value for ${schoolName}: ${err}`);
        } else {
            console.log(`Value set for ${schoolName}: ${value}`);
        }
    });
}

// Promisify client.get method
const getAsyn = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsyn(schoolName);
        console.log(`Value for ${schoolName}: ${value}`);
    } catch (err) {
        console.error(`Error getting value for ${schoolName}: ${err}`);
    }
}

// Calling the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
