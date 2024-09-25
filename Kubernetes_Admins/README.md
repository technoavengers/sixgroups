# Kubernetes Labs: MinIO Operator and CRDs

## Overview

Welcome to the Kubernetes labs focused on MinIO and Custom Resource Definitions (CRDs). These labs are designed to provide hands-on experience with deploying, managing, and scaling MinIO instances in a Kubernetes environment. Through these exercises, you will gain practical knowledge of how to use CRDs, manage configuration with ConfigMaps and Secrets, and leverage the MinIO Operator for advanced management tasks.

## Labs Included

1. **Lab 1: Getting Started with Kubernetes**
   - Learn the basics of Kubernetes by running MinIO as a container on Docker.

2. **Lab 2: Kubernetes Fundamentals with Pods, ReplicaSets, and Services**
   - Deploy MinIO as a Pod, ensure availability with a ReplicaSet, and expose it using a Service.

3. **Lab 3: Deploying MinIO as a Deployment with Persistent Volume in Kubernetes**
   - Deploy MinIO as a Deployment, using Persistent Volumes to ensure data persistence.

4. **Lab 4: Upgrading MinIO as a StatefulSet in Kubernetes**
   - Deploy and upgrade MinIO using StatefulSets to manage stateful applications in Kubernetes.

5. **Lab 5: Managing Configuration with ConfigMaps and Secrets in Kubernetes**
   - Enhance MinIO deployments by managing configuration with ConfigMaps and sensitive information with Secrets.

6. **Lab 6: Understanding Custom Resource Definitions (CRDs) in Kubernetes and MinIO Operator**
   - Explore CRDs in Kubernetes and understand how they work with custom controllers, using a simple example.

7. **Lab 7: Exploring MinIO Operator CRDs and Custom Controllers**
   - Dive deeper into the MinIO Operator, exploring its CRDs and how it automates the management of MinIO deployments.

## Prerequisites

- Basic knowledge of Kubernetes concepts.
- A working Kubernetes cluster (e.g., Minikube, kind, or a cloud-based Kubernetes service).
- `kubectl` command-line tool configured to interact with your Kubernetes cluster.
- Access to the internet to pull necessary images and configurations.

## How to Use This Repository

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Navigate to each lab's directory:**

    Each lab has its own directory (e.g., `labs/Lab1`, `labs/Lab2`, etc.) containing the relevant YAML files and instructions.

    ```bash
    cd labs/Lab1
    ```

3. **Follow the instructions:**

    Each lab includes a detailed Markdown file (e.g., `Lab1.md`) that provides step-by-step instructions. Open this file and follow the steps to complete the lab.

4. **Clean up resources:**

    After completing each lab, it's important to clean up the resources you created to avoid unnecessary charges or resource usage:

    ```bash
    kubectl delete -f <lab-specific-yaml-files>
    ```

## Troubleshooting

If you encounter any issues while running the labs, ensure that:

- Your Kubernetes cluster is running and accessible via `kubectl`.
- All dependencies are installed and correctly configured.
- The MinIO Operator and CRDs are properly applied before attempting to create MinIO-specific resources.

---

Happy learning!
