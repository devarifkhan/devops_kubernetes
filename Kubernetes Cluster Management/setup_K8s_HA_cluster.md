# Kubernetes Installation Process

**Note:** Latest Ubuntu 22.04 and above is not compatible with Kubeadm, installation will end up with error. Please use Ubuntu OS 20.04.

## Install Kubernetes on Master Node

1. **Upgrade apt packages:**
    ```bash
    sudo apt-get update
    ```

2. **Create a configuration file for containerd:**
    ```bash
    cat <<EOF | sudo tee /etc/modules-load.d/containerd.conf
    overlay
    br_netfilter
    EOF
    ```

3. **Load modules:**
    ```bash
    sudo modprobe overlay
    sudo modprobe br_netfilter
    ```

4. **Set system configurations for Kubernetes networking:**
    ```bash
    cat <<EOF | sudo tee /etc/sysctl.d/99-kubernetes-cri.conf
    net.bridge.bridge-nf-call-iptables = 1
    net.ipv4.ip_forward = 1
    net.bridge.bridge-nf-call-ip6tables = 1
    EOF
    ```

5. **Apply new settings:**
    ```bash
    sudo sysctl --system
    ```

6. **Install containerd:**
    ```bash
    sudo apt-get update && sudo apt-get install -y containerd
    ```

7. **Create a default configuration file for containerd:**
    ```bash
    sudo mkdir -p /etc/containerd
    ```

8. **Generate default containerd configuration and save to the newly created default file:**
    ```bash
    containerd config default | sudo tee /etc/containerd/config.toml
    ```

9. **Restart containerd to ensure new configuration file usage:**
    ```bash
    sudo systemctl restart containerd
    ```

10. **Verify that containerd is running:**
    ```bash
    sudo systemctl status containerd
    ```

11. **Disable swap:**
    ```bash
    sudo swapoff -a
    ```

12. **Disable swap on startup in /etc/fstab:**
    ```bash
    sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
    ```

13. **Install dependency packages:**
    ```bash
    sudo apt-get update && sudo apt-get install -y apt-transport-https ca-certificates curl
    ```

14. **Download and add the GPG key:**
    ```bash
    sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
    ```

15. **Add Kubernetes to the repository list:**
    ```bash
    echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
    ```

16. **Update package listings:**
    ```bash
    sudo apt-get update
    ```

17. **Install Kubernetes packages:**
    ```bash
    sudo apt-get install -y kubelet=1.24.0-00 kubeadm=1.24.0-00 kubectl=1.24.0-00
    ```

18. **Turn off automatic updates:**
    ```bash
    sudo apt-mark hold kubelet kubeadm kubectl
    ```

19. **Log into both Worker Nodes to perform previous steps 1 to 18.**

20. **Initialize the Cluster:**
    ```bash
    sudo kubeadm init --pod-network-cidr 192.168.0.0/16
    ```

21. **Set kubectl access:**
    ```bash
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config
    ```

22. **Test access to cluster:**
    ```bash
    kubectl get nodes
    ```

23. **Install the Calico Network Add-On:**
    ```bash
    kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.24.5/manifests/tigera-operator.yaml
    kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.24.5/manifests/custom-resources.yaml
    ```

24. **Confirm that all of the pods are running:**
    ```bash
    watch kubectl get pods -n calico-system
    ```

25. **Wait for 2-4 minutes and check the status of the control plane node:**
    ```bash
    kubectl get nodes
    ```

26. **Join the Worker Nodes to the Cluster:**
    - **In the Control Plane Node, create the token and copy the kubeadm join command:**
        ```bash
        kubeadm token create --print-join-command
        ```
    - **In both Worker Nodes, paste the kubeadm join command to join the cluster:**
        ```bash
        sudo kubeadm join ...
        ```
    - **In the Control Plane Node, view cluster status:**
        ```bash
        kubectl get nodes
        ```