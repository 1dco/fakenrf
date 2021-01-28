# Kubernetes

based on a single server deployment microk8s
```
microk8s.enable dns registry storage istio
sudo apt install python3 python3-pip
pip3 install flask
sudo apt install docker
kubectl label namespace default istio-injection=enabled 
```

```
$ microk8s.status
microk8s is running
addons:
cilium: disabled
dashboard: disabled
dns: enabled
fluentd: disabled
gpu: disabled
helm: disabled
ingress: disabled
istio: enabled
jaeger: disabled
juju: disabled
knative: disabled
kubeflow: disabled
linkerd: disabled
metallb: disabled
metrics-server: disabled
prometheus: disabled
rbac: disabled
registry: enabled
storage: enabled 
```

## Grafana Forward

```
kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l app=grafana -o jsonpath='{.items[0].metadata.name}') 3000:3000 --address 0.0.0.0 &
```

## Jaeger Trace

```
kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l app=jaeger -o jsonpath='{.items[0].metadata.name}') 16686:16686 --address 0.0.0.0 &
```

## Forward Kiali

```
kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l app=kiali -o jsonpath='{.items[0].metadata.name}') 20001:20001 --address 0.0.0.0 &
```

## Forward Prometheus

```
kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l app=prometheus -o jsonpath='{.items[0].metadata.name}') 9090:9090 --address 0.0.0.0 &
```