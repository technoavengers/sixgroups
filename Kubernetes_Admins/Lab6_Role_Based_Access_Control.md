## **Lab 6: Role-Based Access Control (RBAC) for MinIO in Kubernetes**

***Estimated Time: 25 mins***

#### **Objective:**

This lab will guide Kubernetes administrators through the process of applying RBAC to manage access control for MinIO deployments in a Kubernetes cluster. By the end of the lab, participants will:

1. Create and manage roles, role bindings, and cluster role bindings for MinIO.  
2. Assign users different levels of access (e.g., admin, read-only).  
3. Restrict access to MinIO pods and services.  
4. Audit and verify RBAC policies.

***All the yaml files for this lab are provided under*** 

**Kubernetes\_Admins/labs/Lab6**

### **Part 1: Create Namespace and Deploy MinIO**

### **Step 1: Create Namespace** 

### Create a new namespace and deploy MinIO as a StatefulSet in the `minio-rbac` namespace

| apiVersion: v1kind: Namespacemetadata:  name: minio-rbac |
| :---- |

| kubectl apply \-f minio\_namespace.yaml  |
| :---- |

**Step 2: Deploy MinIO StatefulSet**

 You will find YAML for the StatefulSet (***Kubernetes\_Admins/labs/Lab6/minio\_statefulset.yaml)***

| apiVersion: apps/v1kind: StatefulSetmetadata:  name: minio-statefulset  namespace: minio-rbacspec:  serviceName: "minio"  replicas: 2  selector:    matchLabels:      app: minio  template:    metadata:      labels:        app: minio    spec:      containers:      \- name: minio        image: minio/minio:latest        args:        \- server        \- /data        \- \--console-address        \- ":9001"        env:        \- name: MINIO\_ROOT\_USER          value: "admin"        \- name: MINIO\_ROOT\_PASSWORD          value: "password"        ports:        \- containerPort: 9000          name: minio        volumeMounts:        \- name: data          mountPath: /data  volumeClaimTemplates:  \- metadata:      name: data    spec:      accessModes: \["ReadWriteOnce"\]      resources:        requests:          storage: 1Gi      storageClassName: standard |
| :---- |

| kubectl apply \-f minio\_statefulset.yaml |
| :---- |

**Step 3: Create a Service for MinIO**:

 You will find YAML for the Service (***Kubernetes\_Admins/labs/Lab6/minio\_service.yaml***):

| apiVersion: v1kind: Servicemetadata:  name: minio-service  namespace: minio-rbacspec:  selector:    app: minio  ports:  \- name: minio-svc    protocol: TCP    port: 9000    targetPort: 9000  \- name: minio-console    protocol: TCP    port: 9001    targetPort: 9001  type: ClusterIP |
| :---- |

Apply the service yaml

| kubectl apply \-f minio\_service.yaml |
| :---- |

### 

### 

### **Part 2 : Creating RBAC Policies for MinIO**

#### **Task:**

Create Kubernetes RBAC roles and role bindings to control access to the MinIO deployment.

#### **Steps:**

1. Create a `Role` to grant basic permissions for managing MinIO resources.  
2. Create a `RoleBinding` to assign the role to a user.  
3. Use the `kubectl auth can-i` command to verify the permissions.

**Step 1: Create a Role**:

     	 Below Role YAML file can be found at   

***(Kubernetes\_Admins/labs/Lab6/Roles/read\_write/minio-role.yaml)***

| apiVersion: rbac.authorization.k8s.io/v1kind: Rolemetadata:  name: minio-manager  namespace: minio-rbacrules:\- apiGroups: \["", "apps", "batch"\]  resources: \["pods", "services", "statefulsets"\]  verbs: \["get", "list", "create", "delete"\] |
| :---- |

         **– Apply the Role**

	Before running below command, make sure you are in folder where minio-role.yaml exists

	***(Kubernetes\_Admins/labs/Lab6/Roles/read\_write/minio-role.yaml)***

            kubectl apply \-f minio-role.yaml

### **What This Role Does:**

* The `minio-manager` Role allows users with this Role to:  
  * **Get** information about Pods, Services, and StatefulSets within the `minio-rbac` namespace.  
  * **List** all Pods, Services, and StatefulSets in the `minio-rbac` namespace.  
  * **Create** new Pods, Services, and StatefulSets within the namespace.  
  * **Delete** existing Pods, Services, and StatefulSets within the namespace.

###  **rules:**

This section defines the permissions that the `minio-manager` Role grants. Each rule specifies what resources can be accessed, in which API groups, and what actions (verbs) are allowed.

#### **rules: apiGroups**

| \- apiGroups: \["", "apps", "batch"\] |
| :---- |

* **apiGroups** define the resource groups that this Role can interact with. API groups organize resources in Kubernetes by functionality.  
  * **`""` (empty string)**: Refers to the **core API group**, which includes core resources such as Pods, Services, and ConfigMaps.  
  * **`apps`**: Refers to the **apps API group**, which includes resources like Deployments, StatefulSets, and ReplicaSets.  
  * **`batch`**: Refers to the **batch API group**, which includes resources like Jobs and CronJobs.

#### **rules: resources**

| resources: \["pods", "services", "statefulsets"\] |
| :---- |

* **resources** define the types of Kubernetes resources that this Role can manage:  
  * **`pods`**: Refers to the Pods resource in Kubernetes, which are the smallest deployable units that run containers.  
  * **`services`**: Refers to Services, which expose applications running in Pods to be accessible within the cluster or externally.  
  * **`statefulsets`**: Refers to StatefulSets, which manage stateful applications and provide stable identities to the Pods they manage.

#### 

#### **rules: verbs**

| verbs: \["get", "list", "create", "delete"\] |
| :---- |

* **verbs** define the actions that the Role allows on the resources. These are the operations that can be performed on the specified resources.  
  * **`get`**: Allows reading a specific resource (e.g., `kubectl get pod`).  
  * **`list`**: Allows listing resources (e.g., `kubectl get pods` to list all pods in the namespace).  
  * **`create`**: Allows creating new resources (e.g., `kubectl create pod` to create a new pod).  
  * **`delete`**: Allows deleting resources (e.g., `kubectl delete pod` to remove a pod).

Step 2: **Create a RoleBinding**:

RoleBinding YAML file can be found at  

***(Kubernetes\_Admins/labs/Lab6/Roles/read\_write/minio-rolebinding.yaml)***

| apiVersion: rbac.authorization.k8s.io/v1kind: RoleBindingmetadata:  name: minio-manager-binding  namespace: minio-rbacsubjects:\- kind: User  name: minio-user  apiGroup: rbac.authorization.k8s.ioroleRef:  kind: Role  name: minio-manager  apiGroup: rbac.authorization.k8s.io |
| :---- |

**– Apply the Role**

Before running below command, make sure you are in folder where minio-rolebinding.yaml exists

***(Kubernetes\_Admins/labs/Lab6/Roles/read\_write/minio-rolebinding.yaml)***

| *kubectl apply \-f minio-rolebinding.yaml* |
| :---- |

   

### 

### **What This RoleBinding Does:**

* ### This RoleBinding binds the `minio-manager` Role to the user `minio-user` in the `minio-rbac` namespace.

* ### The `minio-manager` Role (defined in a separate YAML) would have permissions to perform actions on resources like `pods`, `services`, and `statefulsets` within the `minio-rbac` namespace.

* ### By creating this RoleBinding, you're giving the `minio-user` the ability to perform the actions specified in the `minio-manager` Role (e.g., get, list, create, and delete `pods`, `services`, and `statefulsets`).

### 

### **`subjects:`**

| subjects:\- kind: User  name: minio-user  apiGroup: rbac.authorization.k8s.io |
| :---- |

* **subjects** define the entities (users, groups, or service accounts) that will be granted the permissions from the associated Role.  
* Each subject is defined with the following attributes:  
  * **kind**: Specifies the type of subject. In this case, `User` indicates that the subject is a user.  
  * **name**: The name of the user who will be granted the permissions from the Role. In this case, the user is `minio-user`.  
  * **apiGroup**: The API group that the subject belongs to. For Kubernetes RBAC, the API group for users and groups is `rbac.authorization.k8s.io`.

#### **Supported `kind` values for subjects:**

* **User**: Refers to an individual user.  
* **Group**: Refers to a group of users.  
* **ServiceAccount**: Refers to a service account, which is commonly used for automating tasks or binding roles to applications rather than actual users.

### 

### 

### **`roleRef:`**

| roleRef:  kind: Role  name: minio-manager  apiGroup: rbac.authorization.k8s.io |
| :---- |

* **roleRef** specifies the Role that this RoleBinding will reference and apply to the subjects. The `roleRef` tells Kubernetes which Role’s permissions should be assigned to the specified subjects.  
  * **kind**: Specifies whether this is a `Role` (namespace-scoped) or a `ClusterRole` (cluster-wide). In this case, it refers to a `Role`, meaning the permissions will be applied only within the specified namespace (`minio-rbac`).  
  * **name**: The name of the Role that this RoleBinding references. In this case, the Role is named `minio-manager`, which contains the set of permissions defined in the Role.  
  * **apiGroup**: The API group for RBAC, which is always `rbac.authorization.k8s.io` for Role and RoleBinding.

**Part 3: Verify Restrictions**

Use the `kubectl auth can-i` command to check the permissions for the `minio-user`:The output of the `kubectl auth can-i` command will return either `yes` or `no`, indicating whether the specified user (`minio-user`) has the necessary permissions to perform the given action.

kubectl auth can-i get pods \--as minio-user \-n minio-rbac  
kubectl auth can-i create services \--as minio-user \-n minio-rbac  
kubectl auth can-i delete statefulsets \--as minio-user \-n minio-rbac  
kubectl auth can-i get pods \--as minio-user

**Part 4: ClusterRole and ClusterRoleBinding for MinIO Access Across Namespaces**

**Step 1: Create a ClusterRole:**

YAML file for cluster role can be found at  Kubernetes\_Admins/labs/Lab6/ClusterRoles/minio\_clusterrole.yaml

| apiVersion: rbac.authorization.k8s.io/v1kind: ClusterRolemetadata:  name: minio-cluster-managerrules:\- apiGroups: \["", "apps"\]  resources: \["statefulsets", "services", "pods"\]  verbs: \["get", "list", "create", "delete"\] |
| :---- |

**– Apply the cluster role**

| kubectl apply \-f minio\_clusterrole.yaml |
| :---- |

This ClusterRole defines a set of permissions that apply cluster-wide, meaning across all namespaces in the Kubernetes cluster.

### **What This ClusterRole Does:**

This ClusterRole, `minio-cluster-manager`, allows any user or service account with this role to perform the following actions **cluster-wide** (i.e., across all namespaces):

* **Get** and **List** existing Pods, Services, and StatefulSets.  
* **Create** new Pods, Services, and StatefulSets.  
* **Delete** existing Pods, Services, and StatefulSets.

**Step2: Create a ClusterRoleBinding:**

Bind the ClusterRole to a user across all namespaces.YAML for the cluster role binding can be found at

*Kubernetes\_Admins/labs/Lab6/ClusterRoles/minio\_clusterrolebinding.yaml*

| *apiVersion: rbac.authorization.k8s.io/v1kind: ClusterRoleBindingmetadata:  name: minio-cluster-manager-bindingsubjects:\- kind: User  name: minio-cluster-admin  apiGroup: rbac.authorization.k8s.ioroleRef:  kind: ClusterRole  name: minio-cluster-manager  apiGroup: rbac.authorization.k8s.io* |
| :---- |

**– Apply the cluster role binding**

| kubectl apply \-f minio\_clusterrolebinding.yaml |
| :---- |

This YAML defines a ClusterRoleBinding, which associates the ClusterRole `minio-cluster-manager` with a user named `minio-cluster-admin`. This grants the user `minio-cluster-admin` the permissions defined in the `minio-cluster-manager` ClusterRole across all namespaces in the Kubernetes cluster.

### Key Points:

* Subjects: `minio-cluster-admin` (a user) will get the permissions.  
* RoleRef: Points to the `minio-cluster-manager` ClusterRole, which defines permissions such as `get`, `list`, `create`, and `delete` for `pods`, `services`, and `statefulsets` across all namespaces.

**Step3: Verify permissions**

| kubectl auth can-i get statefulsets \--as minio-cluster-admin \--all\-namespaceskubectl auth can-i create services \--as minio-cluster-admin \--all\-namespaces |
| :---- |

**Clean Up**

| kubectl delete \--all statefulset \-n minio-rbackubectl delete svc minio-service  \-n minio-rbackubectl delete role minio-manager  \-n minio-rbackubectl delete rolebinding minio-manager-binding  \-n minio-rbackubectl delete clusterrole minio-cluster\-managerkubectl delete clusterrolebinding minio-cluster\-manager-binding |
| :---- |

**END OF LAB**