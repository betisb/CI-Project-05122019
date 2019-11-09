import json

import GC_Project_Creator as PC
import googleapiclient
import GC_VM_Manager as VMM
import GC_Bucket_Creator as BC

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
# instance_name = 'vm2'
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
#     str1 = str(instance['networkInterfaces'])
#     json_acceptable_string = str1.replace("'", "\"")
#     str2 = json.loads(json_acceptable_string)
#     print(str2)
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