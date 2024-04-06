from nameko.rpc import rpc, RpcProxy
from datetime import datetime

class SyncServiceY:
    name = "sync_service_y"

    service_x = RpcProxy("sync_service_x")
    redis_sync_service_x = RpcProxy("redis_sync_service_x")

    @rpc
    def enhance_data(self, data):
        start_time = datetime.now()

        for i in range(100):
            processed_data = self.service_x.process_data(data)

        end_time = datetime.now()
        time_difference = end_time - start_time
        print("Time difference:", time_difference.total_seconds(), "seconds")
        return processed_data

    @rpc
    def enhance_data_redis(self):
        processed_data = self.redis_sync_service_x.process_data()
        return processed_data
