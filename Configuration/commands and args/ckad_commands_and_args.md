## Checking for Existing Pods in the Default Namespace

To check if any pods exist in the default namespace, you can use the following command:

```sh
kubectl get pods
```

If there are no resources found in the default namespace, you will see the following output:

```sh
No resources found in default namespace.
```
## Creating a Pod with a Sleep Command

To create a pod with a sleep command, you can use the following YAML configuration:

```yaml
apiVersion: v1
kind: Pod
metadata:
    name: ubuntu-sleeper-2
spec:
    containers:
        - name: ubuntu
            image: ubuntu
            command: ["sleep"]
            args: ["5000"]
```

Apply the configuration using the `kubectl create` command:

```sh
kubectl create -f ubuntu-sleeper-2.yaml
```

To describe the newly created pod, use the following command:

```sh
kubectl describe pod ubuntu-sleeper-2
```

You should see output similar to the following:

```sh
Name:             ubuntu-sleeper-2
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 27 Nov 2024 05:17:47 +0000
Labels:           <none>
Annotations:      <none>
Status:           Running
IP:               10.244.0.4
IPs:
    IP:  10.244.0.4
Containers:
    ubuntu:
        Container ID:  docker://7407b7a03166fd1a523c3cd85ac6adbcf4dac5e4a02008c25ea51c072c31238a
        Image:         ubuntu
        Image ID:      docker-pullable://ubuntu@sha256:278628f08d4979fb9af9ead44277dbc9c92c2465922310916ad0c46ec9999295
        Port:          <none>
        Host Port:     <none>
        Command:
            sleep
        Args:
            5000
        State:          Running
            Started:      Wed, 27 Nov 2024 05:17:54 +0000
        Ready:          True
        Restart Count:  0
        Environment:    <none>
        Mounts:
            /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-kpdx7 (ro)
Conditions:
    Type                        Status
    PodReadyToStartContainers   True 
    Initialized                 True 
    Ready                       True 
    ContainersReady             True 
    PodScheduled                True 
Volumes:
    kube-api-access-kpdx7:
        Type:                    Projected (a volume that contains injected data from multiple sources)
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
    Normal  Scheduled  38s   default-scheduler  Successfully assigned default/ubuntu-sleeper-2 to minikube
    Normal  Pulling    38s   kubelet            Pulling image "ubuntu"
    Normal  Pulled     32s   kubelet            Successfully pulled image "ubuntu" in 6.102s (6.102s including waiting). Image size: 78118185 bytes.
    Normal  Created    31s   kubelet            Created container ubuntu
    Normal  Started    31s   kubelet            Started container ubuntu
```