## **Lab 9: Managing Pod Placement Using Affinity and Anti-Affinity** 

Estimate: 20 mins

### **Lab Overview:**

This lab will help you understand how to configure **node affinity** and **pod affinity/anti-affinity** to control the placement of MinIO pods on specific nodes or avoid scheduling them together based on labels.

---

### **Step 1: Set Up the Kubernetes Cluster** 

Start Minikube cluster with 3 nodes

| minikube delete minikube start \--nodes 3 |
| :---- |

**Step 2: Check the Nodes:**

Once the cluster is up, you can check the status of your nodes using:

| kubectl get nodes |
| :---- |

**Step 3: Label one of your nodes:**

| kubectl label nodes minikube node\-type\=storage-node |
| :---- |

**Step 4: Create a MinIO statefulSet with Affinity** 

Below YAML file can be found at location Kubernetes\_Admins\\labs\\Lab9\\minio\_statefulset\_with\_node\_affinity.yaml

| apiVersion: apps/v1kind: StatefulSetmetadata:  name: miniospec:  serviceName: "minio-service"  replicas: 2  selector:    matchLabels:      app: minio  template:    metadata:      labels:        app: minio    spec:      containers:      \- name: minio        image: minio/minio        args:          \- server          \- /data        ports:          \- containerPort: 9000        volumeMounts:          \- name: minio-storage            mountPath: /data      affinity:        nodeAffinity:          requiredDuringSchedulingIgnoredDuringExecution:            nodeSelectorTerms:            \- matchExpressions:              \- key: node-type                operator: In                values:                \- storage-node  \# Use the node label you applied earlier  volumeClaimTemplates:  \- metadata:      name: minio-storage    spec:      accessModes: \[ "ReadWriteOnce" \]      resources:        requests:          storage: 1Gi |
| :---- |

### **Behavior:**

* **Purpose**: This affinity rule ensures that the pod can only be scheduled on nodes that have the label `node-type=storage-node`.  
* **Hard Constraint**: If no nodes have this label, the pod will remain in a `Pending` state and will not be scheduled until such a node becomes available or the affinity rule is removed.  
* **Ignored Post-Scheduling**: Once the pod is scheduled, if the node label `node-type=storage-node` is removed or changed, the pod will not be affected, and it will continue to run.

**Step 5: Check pods**

Check pods should be deployed only on label with attached labels

| kubectl get pod \-o wide |
| :---- |

![][image1]

**Step 6: Let’s Label one more node:**

| kubectl label nodes minikube-m02 node\-type\=storage-node |
| :---- |

**Step 7: Let’s add pod anti affinity:**

| apiVersion: apps/v1kind: StatefulSetmetadata:  name: miniospec:  serviceName: "minio-service"  replicas: 2  selector:    matchLabels:      app: minio  template:    metadata:      labels:        app: minio    spec:      containers:      \- name: minio        image: minio/minio        args:          \- server          \- /data        ports:          \- containerPort: 9000        volumeMounts:          \- name: minio-storage            mountPath: /data      affinity:        nodeAffinity:          requiredDuringSchedulingIgnoredDuringExecution:            nodeSelectorTerms:            \- matchExpressions:              \- key: node-type                operator: In                values:                \- storage-node  \# Use the node label you applied earlier        podAntiAffinity:          requiredDuringSchedulingIgnoredDuringExecution:          \- labelSelector:              matchExpressions:              \- key: app                operator: In                values:                \- minio            topologyKey: "kubernetes.io/hostname"  volumeClaimTemplates:  \- metadata:      name: minio-storage    spec:      accessModes: \[ "ReadWriteOnce" \]      storageClassName: local-storage      resources:        requests:          storage: 1Gi |
| :---- |

**Node Affinity:**

* **Ensures that the pod is only scheduled on nodes labeled with `node-type=storage-node`.**  
* **This is a hard constraint during scheduling, meaning if no nodes have the label, the pod will remain unscheduled.**

**Pod Anti-Affinity:**

* **Ensures that MinIO pods (`app=minio`) are not scheduled on the same node as other MinIO pods.**  
* **The rule is enforced using the `topologyKey: kubernetes.io/hostname`, meaning pods will be spread across different nodes.**

**RequiredDuringSchedulingIgnoredDuringExecution:**

* **The scheduling rules must be met when the pod is scheduled, but they are ignored if the node or pod labels change after the pod is already running.**

**END OF LAB**

[image1]: <data:image/png;base64,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>