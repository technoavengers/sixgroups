# Lab 3: Deploying MinIO as a Deployment with Persistent Volume in Kubernetes

**Time:** 25 Minutes

## Lab Summary
In this 25-minute lab, participants will deploy MinIO as a Deployment in Kubernetes, using Persistent Volumes (PVs) through an existing Storage Class to ensure data persistence. Although Deployments typically manage stateless applications, attaching a Persistent Volume enables MinIO to retain its state. The lab also covers upgrading the Deployment and performing rolling updates to ensure minimal downtime during updates.

### Objectives
- Create a Persistent Volume Claim using the existing Storage Class.
- Deploy MinIO as a Deployment.
- Expose MinIO using a Service.
- Upgrade the Deployment and perform rolling updates.
- Clean up resources.

---

## Step 1: Create a Persistent Volume Claim (PVC) Using the Existing Storage Class

1. **Locate the `Minio_pvc.yaml` file under Lab3.**

   This YAML file defines a PersistentVolumeClaim (PVC) named `minio-pvc` that requests 1Gi of storage with ReadWriteOnce access, meaning it can be mounted as read-write by a single node. It uses the `standard` storage class to provision the requested storage in the Kubernetes cluster.

    ```yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: minio-pvc
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 1Gi
      storageClassName: standard
    ```

2. **In your VS code terminal, go to the `labs/Lab3` folder.**

3. **Apply the Persistent Volume Claim configuration:**

    ```bash
    kubectl apply -f minio_pvc.yaml
    ```

4. **Verify the persistent volume created because of the above claim:**

    ```bash
    kubectl get pv
    ```

    *Note:* The STATUS of the PVC should be `Bound`, indicating that a Persistent Volume has been dynamically provisioned.

---

## Step 2: Deploy MinIO as a Deployment

1. **Locate the `Minio_deployment.yaml` file under Lab3.**

   This YAML file defines a Kubernetes Deployment named `minio-deployment` that ensures 2 replicas of the MinIO server are running, each using the `minio/minio:latest` image. It mounts a PersistentVolumeClaim named `minio-pvc` to the `/data` directory in each container for persistent storage.

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: minio-deployment
    spec:
      replicas: 2
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
            image: minio/minio:latest
            args:
            - server
            - /data
            env:
            - name: MINIO_ROOT_USER
              value: "admin"
            - name: MINIO_ROOT_PASSWORD
              value: "password"
            ports:
            - containerPort: 9000
              name: minio
            volumeMounts:
            - name: data
              mountPath: /data
          volumes:
          - name: data
            persistentVolumeClaim:
              claimName: minio-pvc
    ```

2. **Apply the Deployment configuration:**

    ```bash
    kubectl apply -f minio_deployment.yaml
    ```

3. **Verify the Deployment:**

    ```bash
    kubectl get deployment minio-deployment
    ```

4. **Check the Pods:**

    ```bash
    kubectl get pods -l app=minio
    ```

    *Note:* Ensure that the MinIO Pod is running before proceeding.

---

## Step 3: Expose MinIO Using a Service

1. **Locate the `minio_service.yaml` file under Lab3.**

   It is the same file that we have discussed in the ReplicaSet as well. Since we deleted this service as part of cleanup, we are going to create it again.

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: minio-service
    spec:
      selector:
        app: minio
      ports:
      - name: minio-svc
        protocol: TCP
        port: 9000
        targetPort: 9000
      - name: minio-console
        protocol: TCP
        port: 9001
        targetPort: 9001
      type: ClusterIP
    ```

2. **Apply the Service configuration:**

    ```bash
    kubectl apply -f minio_service.yaml
    ```

3. **Verify the Service:**

    ```bash
    kubectl get service minio-service
    ```

4. **Forward port 9001 to access the MinIO console on `http://localhost:9001`:**

    ```bash
    kubectl port-forward svc/minio-service 9001
    ```

5. **Open the browser and access `http://localhost:9001`:**
    - **Username:** `admin`
    - **Password:** `password`

---

## Step 4: Upgrade the Deployment and Perform Rolling Updates

1. **Modify the Deployment YAML for an upgrade:**

    Open `minio_deployment.yaml` and update the image field in the Deployment YAML to use a different version of MinIO:

    ```yaml
    image: minio/minio:RELEASE.2024-08-26T15-33-07Z
    ```

2. **Apply the updated Deployment configuration:**

    ```bash
    kubectl apply -f minio_deployment.yaml
    ```

3. **Monitor the rolling update:**

    Use the following command to monitor the rollout status:

    ```bash
    kubectl rollout status deployment/minio_deployment
    ```

4. **Verify the Pods are updated:**

    ```bash
    kubectl get pods -l app=minio
    ```

---

## Step 5: Clean Up Resources

1. **Delete all the Deployment, PVC, and Service using the YAML file:**

    Make sure you are in the Lab3 folder, then run the following command:

    ```bash
    kubectl delete -f .
    ```

2. **Verify all resources are deleted:**

    ```bash
    kubectl get all
    kubectl get pvc
    ```

---

## Conclusion

Participants have successfully deployed MinIO as a Deployment in Kubernetes with Persistent Volumes to ensure data persistence. They also performed a rolling update to upgrade the MinIO deployment, ensuring minimal downtime during the update. This lab provides hands-on experience in managing stateful applications using Kubernetes Deployments.

**END OF LAB**
