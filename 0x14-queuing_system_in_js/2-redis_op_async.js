import redis from 'redis';
import { promisify } from 'util';

const cli = redis.createClient();
const get = promisify(cli.get).bind(cli);

cli.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

cli.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  cli.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  try {
    console.log(await get(schoolName));
  } catch (error) {
    console.log(error);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
