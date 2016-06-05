import boto3
from random import uniform
from datetime import datetime

__version__ = '0.0.1'
__author__ = 'apapantonatos@gmail.com'


#--- Sample output of some values
# Jun  5 18:59:44 localhost collectd[5533]: Configuring Stuff
# Jun  5 18:59:44 localhost collectd[5533]: initing stuff
# Jun  5 18:59:44 localhost collectd[5533]: Initialization complete, entering read-loop.
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_octets): 14937973.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_octets): 1255355.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_packets): 24603.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_packets): 16422.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_errors): 0.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_errors): 0.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_octets): 3535546.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_octets): 1535404.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_packets): 38804.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_packets): 7708.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_errors): 0.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_errors): 0.000000
# Jun  5 18:59:44 localhost collectd[5533]: memory (memory): 98357248.000000
# Jun  5 18:59:44 localhost collectd[5533]: memory (memory): 77824.000000
# Jun  5 18:59:44 localhost collectd[5533]: memory (memory): 294739968.000000
# Jun  5 18:59:44 localhost collectd[5533]: memory (memory): 61349888.000000
# Jun  5 18:59:44 localhost collectd[5533]: memory (memory): 25804800.000000
# Jun  5 18:59:44 localhost collectd[5533]: memory (memory): 32796672.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_octets): 15300.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_octets): 15300.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_packets): 180.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_packets): 180.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_errors): 0.000000
# Jun  5 18:59:44 localhost collectd[5533]: interface (if_errors): 0.000000
# Jun  5 18:59:44 localhost collectd[5533]: load (load): 0.000000
# Jun  5 18:59:44 localhost collectd[5533]: load (load): 0.010000
# Jun  5 18:59:44 localhost collectd[5533]: load (load): 0.050000

class CloudWatch(Object):
    def __init__(self):
        self.ERROR = 6
        self.WARNING = 5
        self.NOTICE = 4
        self.INFO = 3
        self.DEBUG = 2
        self.aws_cloudwatch = None
        self.loglevel = self.INFO

    def log(self, severity=self.INFO, message):
        if severity > self.loglevel:
            if severity = self.ERROR:
                collectd.error("Cloudwatch: %s" % message)
            elif severity = self.WARNING:
                collectd.warning("Cloudwatch: %s" % message)
            elif severity = self.NOTICE:
                collectd.notice("Cloudwatch: %s" % message)
            elif severity = self.INFO:
                collectd.info("Cloudwatch: %s" % message)
            elif severity = self.DEBUG:
                collectd.debug("Cloudwatch: %s" % message)
            else:
                collectd.error("Cloudwatch: log message of unknown severity %s (%s)" % (severity, message))
                return(-1)

        return(0)

    def config_callback(self, config_block):
        self.log(self.DEBUG, "Reading config...")
        if 'aws_access_key_id' in config_block.children:
            self.aws_access_key_id = config_block.children['aws_access_key_id']
            self.log(self.DEBUG, "configuring aws_access_key_id...")
        else:
            self.log(self.ERROR, 'No aws_access_key_id defined in the module config')
            exit(0)

        if 'aws_secret_access_key' in config_block.children:
            self.aws_secret_access_key = config_block.children['aws_secret_access_key']
            self.log(self.DEBUG, "configuring aws_secret_access_key...")
        else:
            self.log(self.ERROR, 'No aws_secret_access_key defined in the module config')
            exit(0)

        if 'loglevel' in config_block.children:
            level = config_block['loglevel']
            if level = 'error':
                self.loglevel = self.ERROR
            elif level = 'warning':
                self.loglevel = self.WARNING
            elif level = 'notice':
                self.loglevel = self.NOTICE
            elif level = 'info':
                self.loglevel = self.INFO
            elif level = 'debug':
                self.loglevel = self.DEBUG
            else:
                self.log(self.ERROR, "unknown logging level %s in config" % level)
                exit(0)
        # for item in config_block.children:
        #      collectd.info('cloudwatch: %s = %s' % (item.key, item.values)) 

    def init_callback(self):
        self.log(self.DEBUG, "Initializing...")
        #self.aws_cloudwatch = boto3.client('cloudwatch', self.aws_access_key_id, self.aws_secret_access_key)

    def read_callback(self, input_data=None):
        metric = collectd.Values();
        metric.plugin = 'python_plugin_test'
        metric.type = 'gauge'
        metric.values = [100]
        metric.host = 'OverwritenHostname'
        metric.dispatch()

    def write_callback(self, vl, data=None):
        for i in vl.values:
            #print "%s (%s): %f" % (vl.plugin, vl.type, i)
            collectd.info("cloudwatch: %s (%s): %f" % (vl.plugin, vl.type, i))

    def post_metrics(self):
        if not self.aws_cloudwatch
            collectd.error('cloudwatch: invalid connection to aws cloudwatch')
            return(-1)


if __name__ == '__main__':
    Print("This is the collectd plugin for AWS cloudwatch")

    exit(0)
else:
    import collectd

    cloudwatch = CloudWatch()

    # Hook Callbacks, Order is important!
    collectd.register_config(cloudwatch.config_callback)
    collectd.register_init(cloudwatch.init_callback)
    #collectd.register_read(read_callback)
    collectd.register_write(cloudwatch.write_callback)

response = aws_cloudwatch.put_metric_data(
    Namespace='collects/test1',
    MetricData=[
        {
            'MetricName': 'test1',
            'Dimensions': [
                {
                    'Name': 'dimension1',
                    'Value': 'seconds'
                },
            ],
            'Timestamp': datetime.utcnow(),
            'Value': uniform(100.0, 200.0),
            # 'StatisticValues': {
            #     'SampleCount': 10.0,
            #     'Sum': 1.0,
            #     'Minimum': 100.0,
            #     'Maximum': 1200.0
            # },
            'Unit': 'Count/Second'
        },
    ]
)