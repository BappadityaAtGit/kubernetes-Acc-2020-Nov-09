111  kubectl create -f 09-WordPress/
  112  kubectl get pods
  113  kubectl describe pod wordpress-deployment-7d4896594c-pjb7r
  114  kubectl get pods
  115  kubectl get svc
  116  kubectl get pods
  117  kubectl exec -it wordpress-deployment-7d4896594c-pjb7r -c mysql -- mysql -u root -p
  118  kubectl exec -it wordpress-deployment-7d4896594c-pjb7r -c mysql -- /bin/bash
  119  kubectl get pods
