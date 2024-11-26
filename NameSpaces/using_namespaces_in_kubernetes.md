# Using Namespaces in Kubernetes

Namespaces in Kubernetes provide a mechanism for isolating groups of resources within a single cluster. Here are some common commands to interact with namespaces and pods.

## Listing Namespaces

To list all namespaces in your Kubernetes cluster, use the following command:

```sh
kubectl get namespaces
```

Example output:

```
NAME              STATUS   AGE
default           Active   126m
kube-node-lease   Active   126m
kube-public       Active   126m
kube-system       Active   126m
```

## Listing Pods in a Namespace

To list all pods in the default namespace, use:

```sh
kubectl get pods
```

Example output:

```
No resources found in default namespace.
```

To list all pods in a specific namespace, such as `kube-system`, use:

```sh
kubectl get pods --namespace kube-system
```

Example output:

```
NAME                               READY   STATUS    RESTARTS   AGE
coredns-6f6b679f8f-n7xp8           1/1     Running   0          126m
etcd-minikube                      1/1     Running   0          127m
kube-apiserver-minikube            1/1     Running   0          127m
kube-controller-manager-minikube   1/1     Running   0          127m
kube-proxy-lxqgj                   1/1     Running   0          126m
kube-scheduler-minikube            1/1     Running   0          127m
storage-provisioner                1/1     Running   0          127m
```

## Listing Pods Across All Namespaces

To list all pods across all namespaces, use:

```sh
kubectl get pods --all-namespaces
```

Example output:

```
NAMESPACE     NAME                               READY   STATUS    RESTARTS   AGE
kube-system   coredns-6f6b679f8f-n7xp8           1/1     Running   0          127m
kube-system   etcd-minikube                      1/1     Running   0          128m
kube-system   kube-apiserver-minikube            1/1     Running   0          128m
kube-system   kube-controller-manager-minikube   1/1     Running   0          128m
kube-system   kube-proxy-lxqgj                   1/1     Running   0          127m
kube-system   kube-scheduler-minikube            1/1     Running   0          128m
kube-system   storage-provisioner                1/1     Running   0          128m
```

Namespaces are a powerful feature in Kubernetes that help manage and organize resources efficiently within a cluster.
## Creating a Namespace

To create a new namespace in your Kubernetes cluster, use the following command:

```sh
kubectl create namespace <namespace-name>
```

For example, to create a namespace called `levelup360`, use:

```sh
kubectl create namespace levelup360
```

Example output:

```
namespace/levelup360 created
```

To verify that the namespace has been created, list all namespaces again:

```sh
kubectl get namespaces
```

Example output:

```
NAME              STATUS   AGE
default           Active   129m
kube-node-lease   Active   129m
kube-public       Active   129m
kube-system       Active   129m
levelup360        Active   8s
```