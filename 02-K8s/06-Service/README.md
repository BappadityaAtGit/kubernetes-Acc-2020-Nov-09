# Create a Pod & Expose the same

```
 kubectl run mywebapp --image=amitvashist7/my-python-webapp:v1 --port=8080
```
```
 kubectl expose pod mywebapp --type=NodePort
```


  374  kubectl get svc 
  375  kubectl describe svc mywebapp
  376  kubectl get pods --show-labels
  377  kubectl get pods -o wide 
  378  kubectl describe pod mywebapp
  379  ls
  380  cp -rf ../05-Deployments/helloworld.yaml 
  381  cp -rf ../05-Deployments/helloworld.yaml  .
  382  ls
  383  kubectl create -f helloworld.yaml 
  384  kubectl get pods 
  385  ls
  386  vim helloworld-svc.yaml
  387  kubectl get svc 
  388  ls
  389  cat helloworld-svc.yaml 
  390  kubectl create -f helloworld-svc.yaml 
  391  kubectl get svc 
  392  kubectl get pods --show-labels
  393  kubectl get pods -o wide
  394  kubectl describe svc helloworld-service
  395  kubectl scale --replicas=1 deploy helloworld-deployment
  396  kubectl get pods -o wide
  397  kubectl describe svc helloworld-service
  398  kubectl scale --replicas=5 deploy helloworld-deployment
  399  kubectl describe svc helloworld-service
  400  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:2 --record
  401  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:3 --record
  402  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:4 --record
  403  kubectl describe pod mywebapp
  404  history 
  405  ls
  406  cat helloworld-svc.yaml 
  407  cat helloworld.yaml 
  408  ls
  409  kubectl get svc 
  410  kubectl describe svc helloworld-service
  411  kubectl  get pods -o wide 
  412  kubectl rollout undo deployment helloworld-deployment --to-revision=1
  413  kubectl  get pods -o wide 
  414  kubectl describe svc helloworld-service
  415  ls
  416  cd ..
  417  ls
  418  cd ..
  419  ls
  420  git add . ; git commit -m "K8s-06-Service"; git push 
  421  ls
  422  cd 02-K8s/
  423  ls
  424  cd 06-Service/
  425  ls
  426  history 
  427  history >> README.md 
