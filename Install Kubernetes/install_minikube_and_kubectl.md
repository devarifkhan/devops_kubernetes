# Install Minikube and Kubectl

Follow these steps to install Minikube and Kubectl on your system.

## Update and Install Dependencies

```sh
sudo apt update
sudo apt install -y curl wget apt-transport-https
```

## Install Minikube

1. Download the latest version of Minikube:

    ```sh
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    ```

2. Install Minikube:

    ```sh
    sudo install minikube-linux-amd64 /usr/local/bin/minikube
    ```

3. Verify the installation:

    ```sh
    minikube version
    ```

## Install Kubectl

1. Download the latest version of Kubectl:

    ```sh
    curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
    ```

2. Make the binary executable:

    ```sh
    chmod +x kubectl
    ```

3. Move the binary to your PATH:

    ```sh
    sudo mv kubectl /usr/local/bin/
    ```

4. Verify the installation:

    ```sh
    kubectl version -o yaml
    ```

## Start Minikube

1. Start Minikube with Docker driver:

    ```sh
    minikube start --driver=docker
    ```

2. If you encounter issues, force start Minikube:

    ```sh
    minikube start --driver=docker --force
    ```

3. Check Minikube status:

    ```sh
    minikube status
    ```

## Verify Kubernetes Cluster

1. Get cluster information:

    ```sh
    kubectl cluster-info
    ```

2. List nodes in the cluster:

    ```sh
    kubectl get nodes
    ```
