# ETCD Basic Opps. 
```
# kubectl get pods -n kube-system
```
```
# kubectl exec -it etcd-master -n kube-system -- /bin/sh	
```
```
ETCDCTL_API=3 etcdctl --cacert="/etc/kubernetes/pki/etcd/ca.crt"  --cert="/etc/kubernetes/pki/etcd/server.crt" --key="/etc/kubernetes/pki/etcd/server.key" endpoint status 
```
```
ETCDCTL_API=3 etcdctl --cacert="/etc/kubernetes/pki/etcd/ca.crt"  --cert="/etc/kubernetes/pki/etcd/server.crt" --key="/etc/kubernetes/pki/etcd/server.key" get / --prefix --keys-only
```	
	
