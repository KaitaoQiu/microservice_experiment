import cProfile
import pstats
from nameko.standalone.rpc import ClusterRpcProxy
config = {
    'AMQP_URI': "pyamqp://guest:guest@localhost"
}

def test():
    with ClusterRpcProxy(config) as cluster_rpc:
        rs=cluster_rpc.sync_service_y.enhance_data_redis()

if __name__ == '__main__':
    cProfile.run('test()', 'redis_output')
    p = pstats.Stats('redis_output')
    p.sort_stats('cumulative').print_stats(20)