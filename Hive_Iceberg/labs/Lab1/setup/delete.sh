cd /home/training/sixgroups_latest/sixgroups/setup/k8s/minio

cd sixgroups/minio_developer/labs/Lab1_MinioSetup
kubectl delete -f .
kubectl delete -k "github.com/minio/operator?ref=v6.0.2"

cd /home/training/sixgroups_latest/sixgroups/setup/k8s/metastore
kubectl delete -f .

cd /home/training/sixgroups_latest/sixgroups/setup/k8s/trino
helm uninstall trino-cluster --namespace trino
kubectl delete namespace trino


