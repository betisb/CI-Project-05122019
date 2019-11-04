import googleapiclient

import Bucket as BK
import create_instance as CR
# import Virtual_Machine_Creator as VMC
# BK.create_bucket("ci_11142019")

compute = CR.main("cloud-infrastucture-251118", "ci_11142019","us-east1-b","civm3")
print(compute)
# CR.delete_instance(VMC.CR,"cloud-infrastucture-251118","us-east1-b","civm2")