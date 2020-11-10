   19  mkdir 03-Replication-Cantroller
   20  ls
   21  cd 03-Replication-Cantroller/
   22  ls
   23  vim helloworld-replication-cantoller.yaml
   24  ls
   25  kubectl create -f helloworld-replication-cantoller.yaml 
   26  kubectl get pods 
   27  kubectl get pods -o wide 
   28  cat helloworld-replication-cantoller.yaml 
   29  ls
   30  vim nginx-rc.yaml
   31  kubectl create -f nginx-rc.yaml 
   32  kubectl get pods 
   33  kubectl describe pod my-nginx-s7bwp
   34  kubectl get pods 
   35  kubectl get rc 
   36  kubectl scale=5 rc helloworld-controller
   37  kubectl scale --replicas=5 rc helloworld-controller
   38  kubectl get rc 
   39  kubectl get pods 
   40  kubectl scale --replicas=15 rc helloworld-controller
   41  kubectl get rc 
   42  kubectl get pods 
   43  kubectl get rc 
   44  kubectl get pods 
   45  kubectl scale --replicas=1 rc helloworld-controller
   46  kubectl get pods 
   47  kubectl get rc 
   48  kubectl delete rc my-nginx
   49  kubectl get rc 
   50  kubectl get pods 
   51  kubectl get rc 
   52  kubectl delete pod helloworld-controller-r2fkz
   53  kubectl get rc 
   54  kubectl get pods 
   55  kubectl delete pod hello-k8s helloworld-controller-zcrwc
   56  kubectl get pods 
   57  ls
   58  cat helloworld-replication-cantoller.yaml 
   59  kubectl get rc 
   60  kubectl apply -f helloworld-replication-cantoller.yaml 
   61  kubectl get rc 
   62  ls
   63  kubectl  get pods 
   64  kubectl delete pod helloworld-controller-mvjns helloworld-controller-whx7n
   65  kubectl  get pods 
   66  kubectl  get rc,pods
   67  kubectl delete pod pod/helloworld-controller-pp9rz pod/helloworld-controller-zt7v9
   68  kubectl delete pod helloworld-controller-pp9rz helloworld-controller-zt7v9
   69  kubectl  get rc,pods
   70  kubectl delete -f helloworld-replication-cantoller.yaml 
   71  kubectl  get rc,pods
   72  cd ..
   73  l
   74  history 
   75  ls
   76  vim 03-Replication-Cantroller/README.md
   77  history > 03-Replication-Cantroller/README.md
