# Lab 5: Managing Configuration with ConfigMaps and Secrets in Kubernetes

**Time:** 20 Minutes

## Lab Summary
In this lab, participants will enhance the MinIO StatefulSet by incorporating Kubernetes ConfigMaps and Secrets to manage configuration and sensitive information. They will learn how to externalize MinIO configuration using ConfigMaps and securely manage access keys using Secrets. This approach ensures that configuration and sensitive data are separated from the application code, making it easier to manage and secure stateful applications in Kubernetes.

### Objectives
- Create a ConfigMap for MinIO configuration.
- Apply the ConfigMap using kubectl.
- Verify the creation of the ConfigMap.
- Create a Secret for MinIO access keys.
- Apply the Secret using kubectl.
- Verify the creation of the Secret.
- Modify the MinIO StatefulSet to use ConfigMap and Secret.

> **Note:** YAML files for this lab are under `labs/Lab5`. Open a terminal in VS Code and navigate to that folder first.

---

## Step 1: Create a ConfigMap for MinIO Configuration

**Purpose:** ConfigMaps allow you to decouple configuration artifacts from image content to keep containerized applications portable.

1. **Locate the `minio_configmap.yaml` file in the Lab5 folder.**

    This YAML file defines a ConfigMap named `minio-config` that stores configuration data for MinIO, including the volume path (`/data`) and the server URL (`http://minio:9000`). This configuration can be used to inject these settings into the MinIO pod.

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: minio-config
    data:
      MINIO_VOLUMES: "/data"
      MINIO_SERVER_URL: "http://minio:9000"
    ```

2. **Apply the ConfigMap using kubectl:**

    ```bash
    kubectl apply -f minio_configmap.yaml
    ```

3. **Verify the creation of the ConfigMap:**

    ```bash
    kubectl get configmap minio-config -o yaml
    ```

    *Note:* This ConfigMap will store MinIO configuration variables such as the storage volume location and the server URL.

---

## Step 2: Create a Secret for MinIO Access Keys

**Purpose:** Secrets in Kubernetes allow you to store and manage sensitive information such as passwords, OAuth tokens, and SSH keys securely.

1. **Locate the `minio_secret.yaml` file in the Lab5 folder.**

    This YAML file defines a Kubernetes Secret named `minio-secret` containing base64-encoded credentials for `rootuser` and `rootpassword`, which are `minioadmin` and `miniosecret` respectively. It is of type `Opaque`, used for storing arbitrary sensitive data.

    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: minio-secret
    type: Opaque
    data:
      rootuser: bWluaW9hZG1pbg==  # Base64 encoded value for 'minioadmin'
      rootpassword: bWluaW9zZWNyZXQ=  # Base64 encoded value for 'miniosecret'
    ```

    *Note:* The access and secret keys are base64 encoded.

2. **Apply the Secret using kubectl:**

    ```bash
    kubectl apply -f minio_secret.yaml
    ```

3. **Verify the creation of the Secret:**

    ```bash
    kubectl get secret minio-secret -o yaml
    ```

    *Note:* Verify that the Secret is created and contains the expected data.

---

## Step 3: Modify the MinIO StatefulSet to Use ConfigMap and Secret

**Purpose:** Modify the existing MinIO StatefulSet to use the newly created ConfigMap and Secret for its configuration and sensitive data.

1. **Locate the `minio_statefulset_with_config.yaml` file in the Lab5 folder.**

    ```yaml
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: minio-statefulset
    spec:
      serviceName: "minio"
      replicas: 1
      selector:
        matchLabels:
          app: minio
      template:
        metadata:
          labels:
            app: minio
        spec:
          containers:
          - name: minio
            image: minio/minio
            args:
            - server
            - /data
            - --console-address
            - ":9001"
            env:
            - name: MINIO_VOLUMES
              valueFrom:
                configMapKeyRef:
                  name: minio-config
                  key: MINIO_VOLUMES
            - name: MINIO_SERVER_URL
              valueFrom:
                configMapKeyRef:
                  name: minio-config
                  key: MINIO_SERVER_URL
            - name: MINIO_ROOT_USER
              valueFrom:
                secretKeyRef:
                  name: minio-secret
                  key: rootuser
            - name: MINIO_ROOT_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: minio-secret
                  key: rootpassword
            ports:
            - containerPort: 9000
              name: minio
            volumeMounts:
            - name: data
              mountPath: /data
      volumeClaimTemplates:
      - metadata:
          name: data
        spec:
          accessModes: ["ReadWriteOnce"]
          resources:
            requests:
              storage: 1Gi
          storageClassName: standard
    ```

    *Note:* In this modification, the environment variables are sourced from the ConfigMap and Secret using `env`.

2. **Apply the updated StatefulSet:**

    ```bash
    kubectl apply -f minio_statefulset_with_config.yaml
    ```

3. **Verify the StatefulSet configuration:**

    ```bash
    kubectl get statefulset
    ```

    *Note:* Ensure that the StatefulSet is using the ConfigMap and Secret for its configuration and credentials.

---

## Step 4: Verify the Configuration

1. **Check the Pods:**

    ```bash
    kubectl get pods -l app=minio
    ```

2. **Check the logs to confirm that MinIO is configured correctly:**

    ```bash
    kubectl logs minio-statefulset-0
    ```

3. **Verify Secrets and config variables are set as environment variables inside the pod:**

    Connect to your pod:

    ```bash
    kubectl exec -it minio-statefulset-0 /bin/bash
    ```

    You will see environment variables inside your pod, such as `MINIO_ROOT_USER` and `MINIO_ROOT_PASSWORD`, which are set from the Secret file. `MINIO_VOLUMES` and `MINIO_SERVER_URL` are set from the ConfigMap.
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfv0wbWCinxcswrtaLoB6s76aciJIGs_eQjebq07581e5o7XKhCM18vbFj_yGbzQ7LJZYbTrTQgx-WbIRPlCBn8Wt-1DRTdk3xqXijv4pzNcO9UI77f8jCeh1fRzDX5XapaFnhRyr_KUOkUUO70wnZ8I-k?key=_hGo9wnSDVGe9fjA-s6ZYg)
---

## Step 5: Clean Up Resources

1. **Delete the StatefulSet, ConfigMap, and Secret:**

    ```bash
    kubectl delete statefulset minio-statefulset
    kubectl delete configmap minio-config
    kubectl delete secret minio-secret
    ```

---

**END OF LAB**
