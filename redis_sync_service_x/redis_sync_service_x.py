from nameko.rpc import rpc
import redis

class RedisSyncServiceX:
    name = "redis_sync_service_x"
    
    def __init__(self) -> None:
        self.redis_db = None
    
    @rpc
    def process_data(self):
        self.redis_db = redis.Redis(host='localhost', port=6379, db=0)
        processed_data = ''
        for key in self.redis_db.scan_iter():
            value = self.redis_db.get(key)
            processed_data += f'Key: {key}, Value: {value}\n'
        # print(processed_data)
        return processed_data