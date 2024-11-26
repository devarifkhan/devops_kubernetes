# Kubernetes `kubectl` Commands

## Creating a Pod

To create a pod, you can use the following YAML configuration:

```yaml
apiVersion: v1
kind: Pod
metadata:
    name: draining-node-test-pod
    labels:
        tier: frontend
spec:
    containers:
    - name: nginx
      image: nginx:latest
      ports:
      - containerPort: 80
    restartPolicy: OnFailure
```

Save the above configuration in a file named `pod.yml` and run the following command to create the pod:

```sh
kubectl create -f pod.yml
```

## Getting Pod Information

To get the list of pods, use:

```sh
kubectl get pods
```

To get detailed information about a specific pod, use:

```sh
kubectl get pods <pod-name>
```

For example:

```sh
kubectl get pods draining-node-test-pod
```

To get detailed information in a wide format:

```sh
kubectl get pods draining-node-test-pod -o wide
```

To get detailed information in JSON format:

```sh
kubectl get pods draining-node-test-pod -o json
```

Example JSON output:

```json
{
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
        "creationTimestamp": "2024-11-26T06:58:06Z",
        "labels": {
            "tier": "frontend"
        },
        "name": "draining-node-test-pod",
        "namespace": "default",
        "resourceVersion": "2950",
        "uid": "e5158106-c6df-4229-b579-064ca962fb71"
    },
    "spec": {
        "containers": [
            {
                "image": "nginx:latest",
                "imagePullPolicy": "Always",
                "name": "nginx",
                "ports": [
                    {
                        "containerPort": 80,
                        "protocol": "TCP"
                    }
                ],
                "resources": {},
                "terminationMessagePath": "/dev/termination-log",
                "terminationMessagePolicy": "File",
                "volumeMounts": [
                    {
                        "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                        "name": "kube-api-access-ldqxk",
                        "readOnly": true
                    }
                ]
            }
        ],
        "dnsPolicy": "ClusterFirst",
        "enableServiceLinks": true,
        "nodeName": "minikube",
        "preemptionPolicy": "PreemptLowerPriority",
        "priority": 0,
        "restartPolicy": "OnFailure",
        "schedulerName": "default-scheduler",
        "securityContext": {},
        "serviceAccount": "default",
        "serviceAccountName": "default",
        "terminationGracePeriodSeconds": 30,
        "tolerations": [
            {
                "effect": "NoExecute",
                "key": "node.kubernetes.io/not-ready",
                "operator": "Exists",
                "tolerationSeconds": 300
            },
            {
                "effect": "NoExecute",
                "key": "node.kubernetes.io/unreachable",
                "operator": "Exists",
                "tolerationSeconds": 300
            }
        ],
        "volumes": [
            {
                "name": "kube-api-access-ldqxk",
                "projected": {
                    "defaultMode": 420,
                    "sources": [
                        {
                            "serviceAccountToken": {
                                "expirationSeconds": 3607,
                                "path": "token"
                            }
                        },
                        {
                            "configMap": {
                                "items": [
                                    {
                                        "key": "ca.crt",
                                        "path": "ca.crt"
                                    }
                                ],
                                "name": "kube-root-ca.crt"
                            }
                        },
                        {
                            "downwardAPI": {
                                "items": [
                                    {
                                        "fieldRef": {
                                            "apiVersion": "v1",
                                            "fieldPath": "metadata.namespace"
                                        },
                                        "path": "namespace"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    },
    "status": {
        "conditions": [
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2024-11-26T06:58:14Z",
                "status": "True",
                "type": "PodReadyToStartContainers"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2024-11-26T06:58:06Z",
                "status": "True",
                "type": "Initialized"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2024-11-26T06:58:14Z",
                "status": "True",
                "type": "Ready"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2024-11-26T06:58:14Z",
                "status": "True",
                "type": "ContainersReady"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2024-11-26T06:58:06Z",
                "status": "True",
                "type": "PodScheduled"
            }
        ],
        "containerStatuses": [
            {
                "containerID": "docker://477f26de77a0cffe43d6f1b1fbef2921198aa7610fab57f5f0b68467cac9a452",
                "image": "nginx:latest",
                "imageID": "docker-pullable://nginx@sha256:bc5eac5eafc581aeda3008b4b1f07ebba230de2f27d47767129a6a905c84f470",
                "lastState": {},
                "name": "nginx",
                "ready": true,
                "restartCount": 0,
                "started": true,
                "state": {
                    "running": {
                        "startedAt": "2024-11-26T06:58:14Z"
                    }
                },
                "volumeMounts": [
                    {
                        "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                        "name": "kube-api-access-ldqxk",
                        "readOnly": true
                    }
                ]
            }
        ],
        "hostIP": "192.168.49.2",
        "podIP": "10.244.0.5",
        "startTime": "2024-11-26T06:58:06Z"
    }
}
```
## Describing a Pod

To get detailed information about a specific pod, use the `describe` command:

```sh
kubectl describe pods <pod-name>
```

For example:

```sh
kubectl describe pods draining-node-test-pod
```

This command provides detailed information about the pod, including its status, containers, volumes, and events.
kubectl exec draining-node-test-pod -c nginx~ -- cat /etc/nginx/nginx .conf

## Executing Commands in a Pod

To execute a command inside a running pod, use the `exec` command:

```sh
kubectl exec <pod-name> -c <container-name> -- <command>
```

For example, to view the Nginx configuration file inside the `draining-node-test-pod` pod, run:

```sh
kubectl exec draining-node-test-pod -c nginx -- cat /etc/nginx/nginx.conf
```

The output will be:

```plaintext
user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}
```

## Deleting a Pod

To delete a pod, use the `delete` command:

```sh
kubectl delete pod <pod-name>
```

For example, to delete the `draining-node-test-pod` pod, run:

```sh
kubectl delete pod draining-node-test-pod
```

After deleting the pod, you can verify that it has been removed by listing the pods:

```sh
kubectl get pods
```

If the pod has been successfully deleted, you should see a message indicating that no resources are found in the default namespace.