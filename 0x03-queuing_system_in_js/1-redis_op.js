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
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.error(`Error retrieving value for ${schoolName}: ${err}`);
        } else {
            console.log(`Value for ${schoolName}: ${reply}`);
        }
    })
}

// Calling the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
