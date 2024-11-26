```markdown
# Kubernetes Deployment Updates

## Creating a Deployment

```sh
ubuntu@ip-172-31-37-190:~$ kubectl create -f deployments.yaml 
deployment.apps/myapp-deployment created
```

## Checking Rollout Status

```sh
ubuntu@ip-172-31-37-190:~$ kubectl rollout status deployment.apps/myapp-deployment
Waiting for deployment "myapp-deployment" rollout to finish: 0 of 6 updated replicas are available...
Waiting for deployment "myapp-deployment" rollout to finish: 1 of 6 updated replicas are available...
Waiting for deployment "myapp-deployment" rollout to finish: 2 of 6 updated replicas are available...
Waiting for deployment "myapp-deployment" rollout to finish: 3 of 6 updated replicas are available...
Waiting for deployment "myapp-deployment" rollout to finish: 4 of 6 updated replicas are available...
Waiting for deployment "myapp-deployment" rollout to finish: 5 of 6 updated replicas are available...
deployment "myapp-deployment" successfully rolled out
```

## Viewing Rollout History

```sh
ubuntu@ip-172-31-37-190:~$ kubectl rollout history deployment.apps/myapp-deployment
deployment.apps/myapp-deployment 
REVISION  CHANGE-CAUSE
1         <none>
```

## Deleting the Deployment

```sh
ubuntu@ip-172-31-37-190:~$ kubectl delete deployment myapp-deployment
deployment.apps "myapp-deployment" deleted
```

## Listing Pods

```sh
ubuntu@ip-172-31-37-190:~$ kubectl get pods
NAME                     READY   STATUS    RESTARTS   AGE
myapp-replicaset-6dr2v   1/1     Running   0          36m
myapp-replicaset-6vv52   1/1     Running   0          30m
myapp-replicaset-rkxgp   1/1     Running   0          38m
myapp-replicaset-rw5c5   1/1     Running   0          30m
myapp-replicaset-vgbp5   1/1     Running   0          38m
myapp-replicaset-zs8vt   1/1     Running   0          30m
nginx                    1/1     Running   0          4h43m
```

## Creating a Deployment with Record Flag

```sh
ubuntu@ip-172-31-37-190:~$ kubectl create -f deployments.yaml --record
Flag --record has been deprecated, --record will be removed in the future
deployment.apps/myapp-deployment created
```

## Checking Rollout Status Again

```sh
ubuntu@ip-172-31-37-190:~$ kubectl rollout status deployment.apps/myapp-deployment
deployment "myapp-deployment" successfully rolled out
```

## Viewing Rollout History with Change Cause

```sh
ubuntu@ip-172-31-37-190:~$ kubectl rollout history deployment.apps/myapp-deployment
deployment.apps/myapp-deployment 
REVISION  CHANGE-CAUSE
1         kubectl create --filename=deployments.yaml --record=true
```

## Describing the Deployment

```sh
ubuntu@ip-172-31-37-190:~$ kubectl describe deployment myapp-deployment
Name:                   myapp-deployment
Namespace:              default
CreationTimestamp:      Tue, 26 Nov 2024 12:28:31 +0000
Labels:                 tier=frontend
Annotations:            deployment.kubernetes.io/revision: 1
                        kubernetes.io/change-cause: kubectl create --filename=deployments.yaml --record=true
Selector:               env=myapp
Replicas:               6 desired | 6 updated | 6 total | 6 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  env=myapp
  Containers:
   nginx:
    Image:         nginx
    Port:          <none>
    Host Port:     <none>
    Environment:   <none>
    Mounts:        <none>
  Volumes:         <none>
  Node-Selectors:  <none>
  Tolerations:     <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   myapp-deployment-6b49c87889 (6/6 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  76s   deployment-controller  Scaled up replica set myapp-deployment-6b49c87889 to 6
```