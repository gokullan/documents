# Redis

- `set key value`
- `exists key`
- `get key`
- `del key`
- `flushall`
- `keys regex`
- `ttl key`
  - TTL -1 implies no expiry; -2 means key not found
- `expire key timeInSec`
- `setex key timeInSec value`
- `KEYS *` to list all keys

## Lists
-   `lpush`
-   `lrange`
-   `rpush`
-   `lpop`
-   `rpop`
## Sets
-   `sadd`
-   `smembers`
-   `srem`
## Hashes
-   `hset`
-   `hget`
-   `hgetall`
-   `hdel`
-   `hexists`
