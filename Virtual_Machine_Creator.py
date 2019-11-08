# Copyright 2015, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import numpy as np
import googleapiclient
import json
from gcp_devrel.testing.flaky import flaky

from create_instance import main

import create_instance as cr
from googleapiclient import discovery
from gcloud import client,connection,resource_manager
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

compute = googleapiclient.discovery.build('compute', 'v1')
project = 'cloud-infrastucture-251118'
zone = 'us-central1-f'
instance_name = 'vm4'
bucket = 'ci_11142019'
# operation = cr.create_instance(compute,project,zone,instance_name,bucket)
#cr.wait_for_operation(compute, project, zone, operation['name'])
instances = cr.list_instances(compute, project, zone)
print('Instances in project %s and zone %s:' % (project, zone))
for instance in instances:
    print(' - ' + instance['name'])
    str1 = str(instance['networkInterfaces'])
    json_acceptable_string = str1.replace("'", "\"")
    str2 = json.loads(json_acceptable_string)
    print(str2)
print("""
Instance created.
It will take a minute or two for the instance to complete work.
Check this URL: http://storage.googleapis.com/{}/output.png
Once the image is uploaded press enter to delete the instance.
""".format(bucket))
result = cr.list_instances(compute,project,zone)
print(result)

# PROJECT = os.environ['cloud-infrastucture-251118']
# BUCKET = os.environ['ci_11142019']
#
# @flaky
# def test_main(capsys):
#     main(
#         PROJECT,
#         BUCKET,
#         'us-central1-f',
#         'test-instance',
#         wait=False)
#
#     out, _ = capsys.readouterr()
#
#     expected_output = re.compile(
#         (r'Instances in project .* and zone us-central1-.* - test-instance'
#          r'.*Deleting instance.*done..$'),
#         re.DOTALL)
#
#     assert re.search(expected_output, out)