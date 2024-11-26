# Kubernetes Deployment Example

This document provides an example of creating a Kubernetes deployment using a YAML configuration file.

## Deployment YAML File

Create a file named `deployments.yaml` with the following content:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: myapp-deployment
    labels:
        tier: frontend
        app: nginx
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

## Commands to Create and Verify Deployment

1. **Create the Deployment:**

     ```sh
     kubectl create -f deployments.yaml
     ```

     Output:
     ```
     deployment.apps/myapp-deployment created
     ```

2. **Check the Deployment Status:**

     ```sh
     kubectl get deployments
     ```

     Output:
     ```
     NAME               READY   UP-TO-DATE   AVAILABLE   AGE
     myapp-deployment   3/3     3            3           22s
     ```

3. **List the Pods:**

     ```sh
     kubectl get pods
     ```

     Output:
     ```
     NAME                                READY   STATUS    RESTARTS   AGE
     myapp-deployment-66c866c4b8-6lvgp   1/1     Running   0          32s
     myapp-deployment-66c866c4b8-q69b6   1/1     Running   0          32s
     myapp-deployment-66c866c4b8-q78m6   1/1     Running   0          32s
     ```

4. **Get All Resources:**

     ```sh
     kubectl get all
     ```

     Output:
     ```
     NAME                                    READY   STATUS    RESTARTS   AGE
     pod/myapp-deployment-66c866c4b8-6lvgp   1/1     Running   0          50s
     pod/myapp-deployment-66c866c4b8-q69b6   1/1     Running   0          50s
     pod/myapp-deployment-66c866c4b8-q78m6   1/1     Running   0          50s

     NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
     deployment.apps/myapp-deployment   3/3     3            3           50s

     NAME                                          DESIRED   CURRENT   READY   AGE
     replicaset.apps/myapp-deployment-66c866c4b8   3         3         3       50s
     ```

This example demonstrates how to create a deployment in Kubernetes, verify its status, and list the associated pods and resources.