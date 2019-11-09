import os


def Project_Creator(name=None):
    cmd = 'gcloud projects create '+name
    os.system(cmd)
    cmd = ' gcloud components update'
    os.system(cmd)
    return cmd


