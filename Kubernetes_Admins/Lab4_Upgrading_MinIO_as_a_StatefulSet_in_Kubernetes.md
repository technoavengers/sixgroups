# Lab 4: Upgrading MinIO as a StatefulSet in Kubernetes

**Time:** 25 Minutes

## Lab Summary
In this lab, participants will deploy MinIO as a StatefulSet in Kubernetes, ensuring data persistence with Persistent Volumes. StatefulSets are ideal for stateful applications like MinIO, as they provide stable network identities, ordered deployment, and stable storage. This lab will guide participants through upgrading MinIO, explaining potential differences from deploying MinIO as a Deployment.

### Objectives
- Deploy MinIO as a StatefulSet.
- Observe stable network identities.
- Understand ordered deployment and termination.
- Clean up resources.

---

## Step 1: Deploy MinIO as a StatefulSet

**Difference from Deployment:** StatefulSets ensure that each Pod has a unique, persistent identity and storage, even across rescheduling. Unlike Deployments, StatefulSets are used for applications requiring stable network identities and persistent storage.

1. **Locate the `minio_statefulset.yaml` file in the Lab4 folder.**

    This YAML file defines the MinIO StatefulSet:

    ```yaml
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: minio-statefulset
    spec:
      serviceName: "minio"
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
            - --console-address
            - ":9001"
            env:
            - name: MINIO_ACCESS_KEY
              value: "admin"
            - name: MINIO_SECRET_KEY
              value: "password"
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

2. **Apply the StatefulSet configuration:**

    ```bash
    kubectl apply -f minio-statefulset.yaml
    ```

3. **Verify the StatefulSet:**

    ```bash
    kubectl get statefulset minio-statefulset
    ```

4. **Check the Pods:**

    ```bash
    kubectl get pods -l app=minio
    ```

    *Note:* Each Pod in the StatefulSet will have a stable identifier, such as `minio-statefulset-0`, `minio-statefulset-1`, etc.

---

## Step 2: Observe Stable Network Identities

**Difference from Deployment:** In StatefulSets, each Pod gets a consistent DNS name based on its ordinal index, ensuring stable network identities.

1. **Check the Pod DNS name:**

    ```bash
    kubectl get pod minio-statefulset-0 -o jsonpath='{.spec.hostname}'
    ```

2. **Check the Pod's full DNS address:**

    ```bash
    kubectl get pod minio-statefulset-0 -o jsonpath='{.status.podIP}'
    ```

    The DNS name follows the pattern: `<pod_name>.<service_name>.<namespace>.svc.cluster.local`.

    *Note:* The stable network identity allows other applications to reliably connect to specific MinIO instances.

---

## Step 3: Understand Ordered Deployment and Termination

**Difference from Deployment:** StatefulSets deploy and terminate Pods in an ordered fashion, ensuring that the next Pod only starts after the previous one is Running and Ready.

1. **Scale the StatefulSet to 3 replicas and observe the ordered deployment:**

    ```bash
    kubectl scale statefulset minio-statefulset --replicas=3
    kubectl get pods -l app=minio --watch
    ```

    Watch how the Pods are created one by one. To exit this watch mode, press `Ctrl+c` or `Ctrl+x`.

    *Note:* Pods will be created in order (`minio-statefulset-0`, `minio-statefulset-1`, `minio-statefulset-2`).

---

## Step 4: Clean Up Resources

1. **Delete the StatefulSet and PVC:**

    ```bash
    kubectl delete statefulset minio-statefulset
    kubectl delete pvc -l app=minio
    ```

---

**END OF LAB**
