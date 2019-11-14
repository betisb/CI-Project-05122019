import base64
import json
import time
import os
import random
import googleapiclient.discovery
import requests
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

# Create the OS Login API object.
import SSH_Test

oslogin = googleapiclient.discovery.build('oslogin', 'v1')

# Identify the service account ID if it is not already provided.
# account = requests.get(
#     SSHM.SERVICE_ACCOUNT_METADATA_URL, headers=SSHM.HEADERS).text

# print(account)
# if not account.startswith('users/'):
#     account = 'users/' + account

# Create a new SSH key pair and associate it with the service account.
# private_key_file = SSHM.create_ssh_key(oslogin, account)
#Part Four List All VMS and Get Network Interface Information
#=============================================================================================================
compute = googleapiclient.discovery.build('compute', 'v1')
project = 'cloud-infrastucture-251118'
zone = 'us-central1-f'
bucket = 'ci_11142019'
instances = VMM.list_instances(compute, project, zone)
print('Instances in project %s and zone %s:' % (project, zone))
for instance in instances:
    print(' - ' + instance['name'])
    hostname = compute.instances().get(
        project=project,
        zone=zone,
        instance=instance['name'],
        fields='networkInterfaces/accessConfigs/natIP'
    ).execute()['networkInterfaces'][0]['accessConfigs'][0]['natIP']
    print(hostname)

#=============================================================================================================

#Part SSH
#=============================================================================================================
cmd = 'uname -a'
project = 'cloud-infrastucture-251118'
test_id = 'oslogin-test-{id}'.format(id=str(random.randint(0, 1000000)))
zone = 'us-central1-f'
image_family = 'projects/debian-cloud/global/images/family/debian-9'
machine_type = 'zones/{zone}/machineTypes/f1-micro'.format(zone=zone)
account_email = '{test_id}@{project}.iam.gserviceaccount.com'.format(
    test_id=test_id, project=project)

# Initialize the necessary APIs.
iam = googleapiclient.discovery.build(
    'iam', 'v1', cache_discovery=False)
compute = googleapiclient.discovery.build(
    'compute', 'v1', cache_discovery=False)
# service_account_key = SSH_Test.setup_resources(compute, iam, project, test_id, zone, image_family,machine_type, account_email)
# credentials = service_account.Credentials.from_service_account_info(
#     json.loads(base64.b64decode(
#         service_account_key['privateKeyData']).decode('utf-8')))

oslogin = googleapiclient.discovery.build(
    'oslogin', 'v1')
account = 'users/' + account_email
SSHM.main(cmd='uname -a',project='cloud-infrastucture-251118',instance='vm1',zone='us-central1-f',oslogin=oslogin,account=account,hostname='35.226.6.96')
# SSHM.execute(cmd='uname -a')

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