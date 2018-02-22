import unittest
try:
    from unittest.mock import MagicMock, patch, ANY
except ImportError:
    import mock
    from mock import MagicMock, patch, ANY
import botocore
from botocore.exceptions import ClientError
import sys

config_client_mock = MagicMock()

class Boto3Mock():
    def client(self, client_name, *args, **kwargs):
        if client_name == 'config':
            return config_client_mock
        else:
            raise Exception("Attempting to create an unknown client")

sys.modules['boto3'] = Boto3Mock()

import ctraillfienabled as rule

class SampleTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_sample(self):
        self.assertTrue(True);

def build_lambda_event(ruleParameters='{}'):
    invoking_event = '{"messageType":"ScheduledNotification","notificationCreationTime":"2017-12-23T22:11:18.158Z"}'
    return {
        'executionRoleArn':'roleArn',
        'eventLeftScope': True,
        'invokingEvent': invoking_event,
        'ruleParameters': ruleParameters,
        'accountId': 'account-id',
        'configRuleArn': 'arn:aws:config:us-east-1:123456789012:config-rule/config-rule-8fngan',
        'resultToken':'token'
        }
