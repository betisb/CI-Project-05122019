import base64
import json
import time
import os
import random
import googleapiclient.discovery
from google.oauth2 import service_account
import GC_Project_Creator as PC
import googleapiclient
import GC_VM_Manager as VMM
import GC_Bucket_Creator as BC
import GC_SSH_Manager as SSHM

#Part One Create Project
#=============================================================================================================
# PC.Project_Creator('ci12122019-2')
#=============================================================================================================



#Part Two Create Bucket
#=============================================================================================================
# BC.Bucket_Creator('cloud-infrastucture-251118','ci12122019-2')
#=============================================================================================================



#Part Three Create VM Instances
#=============================================================================================================
# compute = googleapiclient.discovery.build('compute', 'v1')
# project = 'cloud-infrastucture-251118'
# zone = 'us-central1-f'
# instance_name = 'vm1'
# bucket = 'ci_11142019'
# operation = VMM.create_instance(compute, project, zone, instance_name, bucket)
# VMM.wait_for_operation(compute, project, zone, operation['name'])
#=============================================================================================================


#Part Four List All VMS and Get Network Interface Information
#=============================================================================================================
# compute = googleapiclient.discovery.build('compute', 'v1')
# project = 'cloud-infrastucture-251118'
# zone = 'us-central1-f'
# bucket = 'ci_11142019'
# instances = VMM.list_instances(compute, project, zone)
# print('Instances in project %s and zone %s:' % (project, zone))
# for instance in instances:
#     print(' - ' + instance['name'])
#     hostname = compute.instances().get(
#         project=project,
#         zone=zone,
#         instance=instance['name'],
#         fields='networkInterfaces/accessConfigs/natIP'
#     ).execute()['networkInterfaces'][0]['accessConfigs'][0]['natIP']
#     print(hostname)

#=============================================================================================================

#Part SSH
#=============================================================================================================



#=============================================================================================================

#Part Five Delete All VMs After Docker Job is Done
#=============================================================================================================
# compute = googleapiclient.discovery.build('compute', 'v1')
# project = 'cloud-infrastucture-251118'
# zone = 'us-central1-f'
# bucket = 'ci_11142019'
# instances = VMM.list_instances(compute, project, zone)
# for instance in instances:
#     operation = VMM.delete_instance(compute, project, zone, instance['name'])
#     VMM.wait_for_operation(compute, project, zone, operation['name'])
#=============================================================================================================