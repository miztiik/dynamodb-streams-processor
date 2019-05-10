
# -*- coding: utf-8 -*-
"""
.. module: Dynamodb-Stream-Processor
    :platform: AWS
    :copyright: (c) 2019 Mystique.,
    :license: Apache, see LICENSE for more details.
.. moduleauthor:: Mystique
.. contactauthor:: miztiik@github issues
"""

import boto3
import logging

# Initialize Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def set_global_vars():
    global_vars = {'status': False}
    try:
        global_vars['Owner']                    = "Mystique"
        global_vars['Environment']              = "Prod"
        global_vars['region_name']              = "us-east-1"
        global_vars['tag_name']                 = "Dynamodb-Stream-Processor"
        global_vars['status']                   = True
    except Exception as e:
        logger.error("Unable to set Global Environment variables. Exiting")
        global_vars['error_message']            = str(e)
    return global_vars


def lambda_handler(event, context):
    resp = {'status': False, 'TotalItems': {} , 'Items': [] }

    # global_vars = set_global_vars()

    if not 'Records' in event:
        resp = {'status': False, "error_message" : 'No Records found in Event' }
        return resp
    
    logger.debug(f"Event:{event}")
    for r in event.get('Records'):
        if r.get('eventName') == "INSERT":
            d = {}
            d['Username'] = r['dynamodb']['NewImage']['Username']['S']
            d['Timestamp'] = r['dynamodb']['NewImage']['Timestamp']['S']
            if 'Message' in r['dynamodb']['NewImage']:
                d['Message'] = r['dynamodb']['NewImage']['Message']['S']
            resp['Items'].append(d)

    if resp.get('Items'):
        resp['status'] = True
        resp['TotalItems'] = { 'Received': len( event.get('Records') ) , 'Processed': len( resp.get('Items') ) }
    
    logger.info(f"resp:{resp}")
    return resp


if __name__ == '__main__':
    lambda_handler(None, None)
