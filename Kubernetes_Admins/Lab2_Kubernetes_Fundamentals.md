# Lab 2: Kubernetes Fundamentals with Pods, ReplicaSets, and Services

**Time:** 25 Minutes  
**Deploying MinIO as a Container on Kubernetes**

## Lab Summary
In this lab, participants will deploy MinIO, a high-performance object storage solution, as a containerized application on Kubernetes. This lab introduces key Kubernetes concepts, including Pods, ReplicaSets, and Services, while guiding participants through the process of deploying MinIO. Starting with a basic Pod to run the MinIO container, participants will then create a ReplicaSet to ensure high availability and scalability. Finally, they will expose MinIO to external traffic using a Kubernetes Service, making it accessible for use. This lab is designed to reinforce the foundational Kubernetes concepts while providing practical experience with deploying real-world applications.

### Objectives
- Deploy MinIO as a Pod
- Ensure Availability with a ReplicaSet
- Expose MinIO Using a Service
- Test and Verify the Deployment

---

## Step 1: Starting a Minikube Cluster

1. **Start Minikube with the specified resources.**
   - Open your terminal and start a Minikube cluster with 2 CPUs and 4GB of memory:
     ```bash
     minikube start --cpus=2 --memory=4096
     ```

2. **Verify the Minikube cluster is running.**
   - Ensure that the Minikube cluster is up and running:
     ```bash
     kubectl get nodes
     ```
   - You should see a node with the status `Ready`.

---

## Step 2: Open VS Code

1. **Open your Kubernetes YAML files in VS Code.**
   - Navigate to the directory containing your lab files:
     ```bash
     cd sixgroups/kubernetes_developer/
     code .
     ```

2. **Handle prompts (if any).**
   - If prompted, just press "Cancel."
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcjsb2B25L6jaBrJ2LR9tnVotbDe-vlcPa4jQLbmfyp1lrAmOCV8bf89PG_Y0cOHDhGJ-8napcoymh-s6MTeQSUz_bx1mnPf5qp44gGKm8WSIyHXbGqBng-ibzC55sRK498FFTNpIyugkZmN-2ogaMkygIU?key=_hGo9wnSDVGe9fjA-s6ZYg)
   - If you see a prompt asking if you trust the author, click "Yes, I trust the author."
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeSXr4o5gU7QLVgwveiFPLVC8QJdgVcAaaovEFojVsvw6VA7Pz7aR4MoBCpLdWI_fh3rqBzRnKZrdgq5FJfUGRWln8agK9t08DTC75RW_SYVDaDp_GaH6RzKcHPXhhZ8hHgZyqQwgknzSf_W71540osPRBU?key=_hGo9wnSDVGe9fjA-s6ZYg)


## Step 3: Deploy MinIO as a Pod

1. **Locate the `minio_pod.yaml` file under Lab2.**

   **YAML File Explanation:**

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: minio
     labels:
       app: minio
   spec:
     containers:
     - name: minio
       image: minio/minio
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
       - containerPort: 9001
``


**Step-by-Step Explanation:**

1.  **`apiVersion: v1`:**

    -   Specifies the API version used to create the resource.  `v1`  is the stable API version for core Kubernetes objects.
2.  **`kind: Pod`:**

    -   Defines the type of Kubernetes resource you are creating. A Pod represents a single instance of a running process in your cluster.
3.  **`metadata`:**

    -   Provides metadata about the object, including its name (`minio`) and labels (`app: minio`).
4.  **`spec`:**

    -   Defines the desired state and configuration of the Pod.
5.  **`containers`:**

    -   Lists the containers that will run inside the Pod. Here, there is one container named  `minio`.
    -   **`image: minio/minio`:**  Specifies the Docker image to use for this container.
    -   **`args`:**  Passes additional command-line arguments (`server`  and  `/data`) to the container's entry point.
    -   **`env`:**  Defines environment variables (`MINIO_ROOT_USER`  and  `MINIO_ROOT_PASSWORD`) for the container.
    -   **`ports`:**  Exposes ports  `9000`  and  `9001`  for the MinIO API and web console.
6.  **Open the terminal inside VS Code.**
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXccXKdnsc03z7DcGZvsKlzHl8R5Sq5YDrfrPy080ZBULPzxuMTfe3B3PLO5N3VHdepApszh9ti_m3KlGTVX8yS9pQzeTiGDwiH7lATFJtLVFfoN9YJ-uF4W_vohlDqN8GfE-ucYteaPn8vl9uELh0I4lpXo?key=_hGo9wnSDVGe9fjA-s6ZYg)
    -   Navigate to the  `labs/Lab2`  folder.
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXep1KqibYgSVSyCxV3MqrlVIBtahLIst1YD0-5KcXnggJmBsoK44ftHUwOV9C33hVJnn7Sx53X88354K67BTr6KgJcIxRUesAV1a4wALfJWjdfyLE-ZQEU6P0Gufoy3Oiu5PyWXzhFUQXKvQybsl0N4GHfn?key=_hGo9wnSDVGe9fjA-s6ZYg)
7.  **Apply the YAML file to create the Pod.**

    -   Deploy the Pod using the  `kubectl apply`  command:

        ```
        kubectl apply -f minio_pod.yaml
        ```
8.  **Verify that the Pod is running.**

    -   Check the status of the Pod:
	    ```
	    kubectl get pods
	    ```
		![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd8alGJeqnDXMKLrXqb0x6gwWZdtPz1LhrinhlXSpDExUDrYpoLeL2GsjYJ07tCPbjkRjgk9-yk8uA3eCng2CRPXr90yUwEW9pXbfQ4PdXJCQfIilY_T-hNhuktB_wyuFWSIkZH3Meo0eaaoVF_OUR4_nEk?key=_hGo9wnSDVGe9fjA-s6ZYg)
    -   The `minio` Pod should show a status of `Running`.
8.  **Delete the Pod.**

    -   Delete the Pod using the following command:
	    ```
	    kubectl delete pod minio
	    ```

## Step 4: Creating a ReplicaSet for MinIO

1. **Locate the `minio_replicaset.yaml` file under Lab2.**

2. **YAML File Content:**

    ```yaml
    apiVersion: apps/v1
    kind: ReplicaSet
    metadata:
      name: minio-replicaset
      labels:
        app: minio
    spec:
      replicas: 3
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
            env:
            - name: MINIO_ROOT_USER
              value: "admin"
            - name: MINIO_ROOT_PASSWORD
              value: "password"
            ports:
            - containerPort: 9000
            - containerPort: 9001
    ```

3. **Explanation:**

    This file defines a Kubernetes ReplicaSet named `minio-replicaset` that ensures three replicas of a Pod running the MinIO server are always up and running.

4. **Apply the YAML file to create the ReplicaSet.**

    Deploy the ReplicaSet using the `kubectl apply` command:

    ```bash
    kubectl apply -f minio_replicaset.yaml
    ```

5. **Verify that the ReplicaSet is functioning.**

    Check the status of the ReplicaSet and the number of running Pods:

    ```bash
    kubectl get replicaset
    kubectl get pods
    ```

    You should see three Pods created by the ReplicaSet, all with the status `Running`.
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfDpSfObyzPjU7bxSczSj8MlFacQ4gLCBNZuOc4ER9C6sTM7mtOn0fx43RGiCUcbeS7RANI2H04R4NlXTqXVV0nWBaBERauCAmYZtjkfWS3rdVCwPEtLKysDXjDTDnKaiZJGKnIsrvhZEViZU4bLuPfDeA7?key=_hGo9wnSDVGe9fjA-s6ZYg)

## Step 5: Exposing MinIO with a Kubernetes Service

1. **Locate the `minio_service.yaml` file under Lab2.**

2. **YAML File Content:**

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
      type: NodePort
    ```

3. **Explanation:**

    This file defines a Kubernetes Service named `minio-service` that routes traffic to Pods with the `app: minio` label. It exposes ports `9000` and `9001` for the MinIO API and console, respectively.

4. **Apply the YAML file to create the Service.**

    Expose MinIO using the `kubectl apply` command:

    ```bash
    kubectl apply -f minio_service.yaml
    ```

5. **Check for services.**

    Verify the service using:

    ```bash
    kubectl get services
    ```
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdWHsr5yLRLG5hV-TU7QwGw6Aml0rjynJYZoHHauFr11MTnwbBlshMfhDnHFcoPH3IUneGtxlkXqsKvOWj-IduxLMRmxmRhzAzdsn5og6Nn9BbRFXlGD6Q1M8PUNUQ688Cb-cI-OBZ_doLGCryEuzwnM6Om?key=_hGo9wnSDVGe9fjA-s6ZYg)
6. **Port-forwarding to access MinIO Console.**

    Forward port `9001` on your local machine to port `9001` of the `minio-service` Kubernetes Service:

    ```bash
    kubectl port-forward svc/minio-service 9001
    ```

    Open your browser and access the MinIO console at [http://localhost:9001](http://localhost:9001).  
    Use the following credentials:  
    **Username:** `admin`  
    **Password:** `password`

---

## Step 6: Testing and Scaling the Deployment

1. Open a new Terminal
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdilLTr2QcKjB0r25d3CKTrvyyuXbX2bGVsGgMYjDimhYl2yXiqzAwFpWYZWfR9tbk0wz6nRtys4i_O0rWfW-C72JwXvMXGzfAhlls_7WV7jX4_-k2t0o0YNGQGavDUISthXeA07fasGnnmOQKDi5YHULk?key=_hGo9wnSDVGe9fjA-s6ZYg)
2. **Scale the ReplicaSet.**
    Increase the number of replicas to 5:

    ```bash
    kubectl scale replicaset minio-replicaset --replicas=5
    ```

3. **Verify that two additional Pods are created:**

    Check the Pods:

    ```bash
    kubectl get pods
    ```

---

## Step 7: Clean Up Resources

1. **Delete the resources:**
    Remove the ReplicaSet and Service:

    ```bash
    kubectl delete rs minio-replicaset
    kubectl delete service minio-service
    ```

2. **Verify all resources are deleted:**

    Check that all resources have been deleted:

    ```bash
    kubectl get all
    ```

---

## Conclusion

In this lab, you have deployed MinIO on Kubernetes using Pods, ReplicaSets, and Services. You started by deploying a single Pod, ensured high availability and scalability with a ReplicaSet, and exposed MinIO to external traffic using a Service. These foundational Kubernetes concepts are essential for deploying and managing real-world applications in a cloud-native environment.

**END OF LAB**
