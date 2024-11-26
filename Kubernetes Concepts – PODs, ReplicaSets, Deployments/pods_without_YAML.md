# Kubernetes Pods Without YAML

This document demonstrates how to create and manage Kubernetes pods without using YAML files.

## Steps

1. **Check for existing pods:**

    ```sh
    kubectl get pods
    ```

    Output:
    ```
    No resources found in default namespace.
    ```

2. **Create a new pod using the `kubectl run` command:**

    ```sh
    kubectl run nginx --image=nginx
    ```

    Output:
    ```
    pod/nginx created
    ```

3. **Verify the pod status:**

    ```sh
    kubectl get pods
    ```

    Output:
    ```
    NAME    READY   STATUS              RESTARTS   AGE
    nginx   0/1     ContainerCreating   0          2s
    ```

4. **Check the pod status again after a few seconds:**

    ```sh
    kubectl get pods
    ```

    Output:
    ```
    NAME    READY   STATUS              RESTARTS   AGE
    nginx   0/1     ContainerCreating   0          14s
    ```

5. **Check the pod status once more:**

    ```sh
    kubectl get pods
    ```

    Output:
    ```
    NAME    READY   STATUS              RESTARTS   AGE
    nginx   0/1     ContainerCreating   0          67s
    ```

6. **Describe the pod to get detailed information:**

    ```sh
    kubectl describe pod nginx
    ```

    Output:
    ```
    Name:             nginx
    Namespace:        default
    Priority:         0
    Service Account:  default
    Node:             minikube/192.168.49.2
    Start Time:       Tue, 26 Nov 2024 11:27:47 +0600
    Labels:           run=nginx
    Annotations:      <none>
    Status:           Pending
    IP:               
    IPs:              <none>
    Containers:
      nginx:
        Container ID:   
        Image:          nginx
        Image ID:       
        Port:           <none>
        Host Port:      <none>
        State:          Waiting
          Reason:       ContainerCreating
        Ready:          False
        Restart Count:  0
        Environment:    <none>
        Mounts:
          /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-fdclz (ro)
    Conditions:
      Type                        Status
      PodReadyToStartContainers   False 
      Initialized                 True 
      Ready                       False 
      ContainersReady             False 
      PodScheduled                True 
    Volumes:
      kube-api-access-fdclz:
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
      Normal  Scheduled  75s   default-scheduler  Successfully assigned default/nginx to minikube
      Normal  Pulling    75s   kubelet            Pulling image "nginx"
    ```

This process shows how to create and manage Kubernetes pods using `kubectl` commands without the need for YAML configuration files.

7. **Get detailed pod information with wide output:**

    ```sh
    kubectl get pods -o wide
    ```

    Output:
    ```
    NAME    READY   STATUS    RESTARTS   AGE     IP           NODE       NOMINATED NODE   READINESS GATES
    nginx   1/1     Running   0          5m10s   10.244.0.4   minikube   <none>           <none>
    ```

