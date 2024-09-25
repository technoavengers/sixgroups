#!/bin/bash

# Define the namespace and pod label
NAMESPACE="minio-tenant"
POD_LABEL="app=minio"

# Function to check if the MinIO pods are ready
check_pods_ready() {
  while true; do
    # Check if all MinIO pods are running and ready
    READY_PODS=$(kubectl get pods -n "$NAMESPACE" -l "$POD_LABEL" -o jsonpath='{.items[*].status.containerStatuses[*].ready}' | grep false)

    if [ -z "$READY_PODS" ]; then
      echo "All MinIO pods are running and ready."
      break
    else
      echo "Waiting for MinIO pods to be ready..."
      sleep 5
    fi
  done
}

# Call the function to check for MinIO pods
check_pods_ready

# Start port-forwarding once the pods are ready
echo "Starting port-forward..."
kubectl port-forward svc/myminio-console 9090 -n minio-tenant
