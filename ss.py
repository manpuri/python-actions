import json, requests
res = requests.post("https://18.236.126.102:32222/dkube/v2/users/ocdkube/jobs/",
headers={'Authorization':'eyJTZXNzaW9uIjp0cnVlLCJUb2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpqY21WaGRHVmtJam94TlRjek1EVXdNVFV6TENKeWIyeGxJam9pYjNCbGNtRjBiM0lpTENKMWMyVnlibUZ0WlNJNkltOWpaR3QxWW1VaWZRLlBGRFJTcC1UbXJNeUJRMXRLWm1EX0FmaHFCMVVOZkYtQW9wbjBVTjVFUXcifQ==',
'Content-Type':'application/keyauth.api.v1+json'},
data=json.dumps({"name":"commit-"+os.environ['GITHUB_SHA'],"parameters":{"class":"training","training":{"executor":{"choice":"dkube","dkube":{"framework":{"choice":"tensorflow","details":{"tfversion":"v1.14"}}}},"workspace":{"program":"ocdkube:mnist","script":"python model.py"},"models":[],"datasets":["ocdkube:mnist"],"tags":[],"hyperparams":{"epochs":1,"steps":100,"batchsize":1,"custom":[],"file":{"body":"","name":""}},"nworkers":0,"ngpus":0,"rdma":False,"gpus_override":False,"view":{"ready":False}}}}), verify=False)

print (res)
