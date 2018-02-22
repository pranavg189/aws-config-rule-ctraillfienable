#    Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at
#
#        http://aws.amazon.com/apache2.0/
#
#    or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

import json
from rule_util import *

def evaluate_compliance(configuration_item):

    print("Hello this is the ctraillfienabled rule for testing:")
    # ctrail = boto3.client('cloudtrail')
    # trail_arn = configuration_item["configuration"]["trailARN"]
    # try:
    #     trail_status = ctrail.get_trail_status(Name = trail_arn)
    #     #print (trail_status)
    #     if configuration_item["configuration"]["logFileValidationEnabled"] and (not trail_status["IsLogging"]):        
    #         return 'COMPLIANT'
    #     elif configuration_item["configuration"]["logFileValidationEnabled"] and (not "LatestDeliveryError" in trail_status):
    #         return 'COMPLIANT'
    #     else:
    #         return 'NON_COMPLIANT'
    # except:
    #     #print ('Caught an exception')
    #     return 'NOT_APPLICABLE'

    evaluations = []

    eval = {}
    eval["ComplianceResourceId"] = configuration_item["resourceId"]
    eval["ComplianceResourceType"] = configuration_item["resourceType"]
    eval["OrderingTimestamp"] = configuration_item["configurationItemCaptureTime"]
    eval["ComplianceType"] = "COMPLIANT"
    eval["Annotation"] = "Hello This is a sample annotation from Pranav"
    evaluations.append(eval)
    return evaluations

    ###############################
    # Add your custom logic here. #
    ###############################

# USE AS IS
# This is the handler that's invoked by Lambda
#@rule_handler
def lambda_handler(event, context):
    # invoking_event = json.loads(event['invokingEvent'])

    # configuration_item = None
    # if 'configurationItem' in invoking_event:
    #     configuration_item = invoking_event['configurationItem']

    # rule_parameters = {}
    # if 'ruleParameters' in event:
    #     rule_parameters = json.loads(event['ruleParameters'])
    # return evaluate_compliance(configuration_item, rule_parameters)

    invoking_event      = json.loads(event['invokingEvent'])
    configuration_item  = invoking_event["configurationItem"]
    #evaluation          = evaluate_compliance(configuration_item)
    config              = boto3.client('config')
    
    result_token = "No token found."
    if "resultToken" in event:
        result_token = event["resultToken"]
    
    return config.put_evaluations(Evaluations=evaluate_compliance(configuration_item),ResultToken=event["resultToken"])
