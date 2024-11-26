# Kubernetes ReplicaSet Example

This document provides an example of how to create and manage a ReplicaSet in Kubernetes.

## ReplicaSet YAML Configuration

Create a file named `replicasets.yml` with the following content:

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
    name: myapp-replicaset
    labels:
        app: myapp
spec:
    selector:
        matchLabels:
            env: myapp
    replicas: 3
    template:
        metadata:
            name: nginx
            labels:
                env: myapp
        spec:
            containers:
                - name: nginx
                    image: nginx
```

## Commands

1. **Create the ReplicaSet:**

        ```sh
        kubectl create -f replicasets.yml
        ```

2. **Get the list of Pods:**

        ```sh
        kubectl get pods
        ```

3. **Get the ReplicaSet:**

        ```sh
        kubectl get replicaset
        ```

4. **Delete a specific Pod:**

        ```sh
        kubectl delete pod myapp-replicaset-hj546
        ```

5. **Get the ReplicaSet again to see the changes:**

        ```sh
        kubectl get replicaset
        ```

6. **Scale the ReplicaSet to 6 replicas:**

        ```sh
        kubectl scale replicaset myapp-replicaset --replicas=6
        ```

This example demonstrates how to create, manage, and scale a ReplicaSet in Kubernetes.