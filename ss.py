
from dkube.sdk.dkube import *

#res = requests.post("https://18.236.126.102:32222/dkube/v2/users/ocdkube/jobs/",
#headers={'Authorization': sys.argv[1],
#'Content-Type':'application/keyauth.api.v1+json'},
#data=json.dumps({"name":"commit-"+os.environ['GITHUB_SHA'],"parameters":{"class":"training","training":{"executor":{"choice":"dkube","dkube":{"framework":{"choice":"tensorflow","details":{"tfversion":"v1.14"}}}},"workspace":{"program":"ocdkube:mnist","script":"python model.py"},"models":[],"datasets":["ocdkube:mnist"],"tags":[],"hyperparams":{"epochs":1,"steps":100,"batchsize":1,"custom":[],"file":{"body":"","name":""}},"nworkers":0,"ngpus":0,"rdma":False,"gpus_override":False,"view":{"ready":False}}}}), verify=False)

#print (res)

env = Environment(scheme='https', host='18.236.126.102', user='ocdkube', token=sys.argv[1], port=32222)
launch_training_job("test", autogenerate=True, environ=env.external, 
                    workspace='mnist', script='python model.py',
                    datasets=['mnist'])
