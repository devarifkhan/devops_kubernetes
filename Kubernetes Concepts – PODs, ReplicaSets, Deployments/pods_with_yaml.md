# Kubernetes PODs with YAML

## Creating a Pod

To create a Pod in Kubernetes, you can use a YAML file. Below is an example of a simple Pod configuration:

```yaml
apiVersion: v1
kind: Pod
metadata:
    name: nginx
    labels:
        app: nginx
        tier: frontend
spec:
    containers:
    - name: nginx
        image: nginx
```

Save this configuration to a file named `pod.yaml`.

## Applying the Pod Configuration

To create the Pod defined in the `pod.yaml` file, use the following command:

```sh
kubectl apply -f pod.yaml
```

You should see an output similar to:

```
pod/nginx created
```

## Describing the Pod

To get detailed information about the Pod, use the `kubectl describe pod` command:

```sh
kubectl describe pod nginx
```

This will provide detailed information about the Pod, including its status, IP address, container details, and events. Here is an example output:

```
Name:             nginx
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 26 Nov 2024 07:44:50 +0000
Labels:           app=nginx
                                    tier=frontend
Annotations:      <none>
Status:           Running
IP:               10.244.0.7
IPs:
    IP:  10.244.0.7
Containers:
    nginx:
        Container ID:   docker://bfa41d9839c0957bc8aa1da04a30638a54709784de293e78948a1f915132c063
        Image:          nginx
        Image ID:       docker-pullable://nginx@sha256:bc5eac5eafc581aeda3008b4b1f07ebba230de2f27d47767129a6a905c84f470
        State:          Running
            Started:      Tue, 26 Nov 2024 07:44:52 +0000
        Ready:          True
        Restart Count:  0
        Environment:    <none>
        Mounts:
            /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-lqkqm (ro)
Conditions:
    Type                        Status
    Initialized                 True 
    Ready                       True 
    ContainersReady             True 
    PodScheduled                True 
Volumes:
    kube-api-access-lqkqm:
        Type:                    Projected
        TokenExpirationSeconds:  3607
        ConfigMapName:           kube-root-ca.crt
        ConfigMapOptional:       <nil>
        DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                                                         node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
    Type    Reason     Age   From               Message
    ----    ------     ----  ----               -------
    Normal  Scheduled  17s   default-scheduler  Successfully assigned default/nginx to minikube
    Normal  Pulling    17s   kubelet            Pulling image "nginx"
    Normal  Pulled     15s   kubelet            Successfully pulled image "nginx" in 1.977s
    Normal  Created    15s   kubelet            Created container nginx
    Normal  Started    14s   kubelet            Started container nginx
```

This output provides a comprehensive overview of the Pod's state and events.