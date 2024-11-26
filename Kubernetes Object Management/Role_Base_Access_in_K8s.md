# Add User in Kubernetes Cluster

## 1. Create Namespace
```sh
kubectl create namespace development
```

## 2. Create Private Key and CSR (Certificate Signing Request) for DevUser
```sh
cd ${HOME}/.kube
sudo openssl genrsa -out DevUser.key 2048
sudo openssl req -new -key DevUser.key -out DevUser.csr -subj "/CN=DevUser/O=development"
```
*The common name (CN) of the subject will be used as username for authentication request. The organization field (O) will be used to indicate group membership of the user.*

## 3. Provide CA Keys of Kubernetes Cluster to Generate the Certificate
```sh
sudo openssl x509 -req -in DevUser.csr -CA ${HOME}/.minikube/ca.crt -CAkey ${HOME}/.minikube/ca.key -CAcreateserial -out DevUser.crt -days 45
```

## 4. Get Kubernetes Cluster Config
```sh
kubectl config view
```

## 5. Add the User in the Kubeconfig File
```sh
kubectl config set-credentials DevUser --client-certificate=${HOME}/.kube/DevUser.crt --client-key=${HOME}/.kube/DevUser.key
```

## 6. Get Kubernetes Cluster Config
```sh
kubectl config view
```

## 7. Add a Context in the Config File
This will allow this user (DevUser) to access the development namespace in the cluster.
```sh
kubectl config set-context DevUser-context --cluster=minikube --namespace=development --user=DevUser
```

# Create a Role for the DevUser

## 1. Test Access by Attempting to List Pods
```sh
kubectl get pods --context=DevUser-context
```

## 2. Create a Role Resource Using Below Manifest
```sh
vi pod-reader-role.yml
```

## 3. Create the Role
```sh
kubectl apply -f pod-reader-role.yml
```

## 4. Verify Role
```sh
kubectl get role -n development
```

# Bind the Role to the DevUser and Verify Your Setup Works

## 1. Create the RoleBinding Spec File
```sh
vi pod-reader-rolebinding.yml
```

## 2. Create Role Binding
```sh
kubectl apply -f pod-reader-rolebinding.yml
```

## 3. Test Access by Attempting to List Pods
```sh
kubectl get pods --context=DevUser-context
```

## 4. Create Pod
```sh
kubectl run nginx --image=nginx --context=DevUser-context
```
