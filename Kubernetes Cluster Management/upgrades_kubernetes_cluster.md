# Upgrade Kubernetes Cluster

## Upgrade Control Plane Node

1. **Get the Running Node and Version**
    ```sh
    kubectl get nodes
    ```

2. **Drain Master Node**
    ```sh
    kubectl drain <node-to-drain> --ignore-daemonsets
    ```

3. **Upgrade kubeadm**
    ```sh
    sudo apt-get update
    sudo apt-get install -y --allow-change-held-packages kubeadm=1.21.1-00
    ```

4. **Verify that the download works and has the expected version**
    ```sh
    kubeadm version
    ```

5. **Verify the upgrade plan**
    ```sh
    sudo kubeadm upgrade plan v1.21.1-00
    ```

6. **Apply the Upgrade**
    ```sh
    sudo kubeadm upgrade apply v1.21.1
    ```

7. **Upgrade kubelet and kubectl packages**
    ```sh
    sudo apt-get update
    sudo apt-get install -y --allow-change-held-packages kubelet=1.21.1-00 kubectl=1.21.1-00
    ```

8. **Restart the kubelet**
    ```sh
    sudo systemctl daemon-reload
    sudo systemctl restart kubelet
    ```

9. **Get the Running Node and Version**
    ```sh
    kubectl get nodes
    ```

10. **Uncordon the Node**
    ```sh
    kubectl uncordon <node-to-uncordon>
    ```

## Upgrade Worker Node

1. **Drain Worker Node**
    ```sh
    kubectl drain <node-to-drain> --ignore-daemonsets --force
    ```

2. **Upgrade kubeadm**
    ```sh
    sudo apt-get update
    sudo apt-get install -y --allow-change-held-packages kubeadm=1.21.1-00
    ```

3. **Verify that the download works and has the expected version**
    ```sh
    kubeadm version
    ```

4. **Upgrade the local kubelet configuration**
    ```sh
    sudo kubeadm upgrade node
    ```

5. **Upgrade kubelet and kubectl packages**
    ```sh
    sudo apt-get update
    sudo apt-get install -y --allow-change-held-packages kubelet=1.21.1-00 kubectl=1.21.1-00
    ```

6. **Restart the kubelet**
    ```sh
    sudo systemctl daemon-reload
    sudo systemctl restart kubelet
    ```

7. **Get the Running Node and Version**
    ```sh
    kubectl get nodes
    ```

8. **Uncordon the Node**
    ```sh
    kubectl uncordon <node-to-uncordon>
    ```