  212  kubectl proxy --port=9090 & 
  213  curl localhost:9090
  214  cat 02-K8s/03-Replication-Cantroller/helloworld-replication-cantoller.yaml 
  215  curl localhost:9090
  216  curl localhost:9090/api/v1
  217  kubectl get pods 
  218  curl localhost:9090/api/v1/pods
  219  kube
  220  kubectl get pods 
  221  curl localhost:9090/api/v1/pods | grep -A50 mywebapp
  222  curl localhost:9090/api/v1/pods > hello.txt | grep -A50 mywebapp hello.txt
  223  cat hello.txt 
  224  kubectl config get-clutsers
  225  kubectl config get-clusters
  226  kubectl config get-clusters kubernetes
  227  kubectl config view kubernetes
  228  kubectl config view 
  229  kubectl get pods 
  230  ls
  231  ps -ef | grep -i proxy 
  232  kill -9 28348
  233  kubectl proxy --port=9090 & 
  234  ps -ef | grep -i proxy 
  235  kill -9 11752
  236  ps -ef | grep -i proxy

# Exposing API Server to the Outsider world via Proxy.

``` 
kubectl proxy --address="172.31.0.100" --port=9090  --accept-hosts="." --accept-paths="." & 
```
