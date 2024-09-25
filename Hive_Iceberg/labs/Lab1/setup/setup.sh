cd /home/training/sixgroups_latest/sixgroups/setup/k8s/minio

minikube start
kubectl apply -k "github.com/minio/operator?ref=v6.0.2"
sleep 5
kubectl apply -f tenant.yaml
sleep 10
kubectl apply -f create_bucket.yaml

cd /home/training/sixgroups_latest/sixgroups/setup/k8s/metastore
kubectl apply -f .

cd /home/training/sixgroups_latest/sixgroups/setup/k8s/trino
kubectl create namespace trino
helm install -f values.yaml trino-cluster trino/trino --namespace trino





