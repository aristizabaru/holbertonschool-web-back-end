import redis from 'redis';

const cli = redis.createClient();
const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const val = [50, 80, 20, 20, 40, 2];
keys.forEach((key, index) => {
  cli.hset('HolbertonSchools', key, val[index], redis.print);
});

cli.hgetall('HolbertonSchools', (err, res) => {
  console.log(res);
});
