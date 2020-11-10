  256  mkdir 05-Deployments
  257  ls
  258  kubectl  get pods 
  259  kubectl  delete pod mywebapp
  260  kubectl  get pods 
  261  ls
  262  cd 05-Deployments/
  263  ls
  264  vim helloworld.yaml
  265  ls
  266  kubectl create -f helloworld.yaml 
  267  kubectl  get deployment 
  268  kubectl  get rs 
  269  kubectl  get pods 
  270  kubectl scale --replicas=5 deployment helloworld-deployment
  271  kubectl  get pods 
  272  kubectl  get pods --show-lables
  273  kubectl  get pods --show-label
  274  kubectl  get pods --show-labels
  275  kubectl  get rs 
  276  kubectl describe rs helloworld-deployment-78cf6987f9
  277  kubectl scale --replicas=7 deployment helloworld-deployment
  278  kubectl describe rs helloworld-deployment-78cf6987f9
  279  kubectl describe deployment helloworld-deployment
  280  kubectl scale --replicas=2 deployment helloworld-deployment
  281  kubectl describe deployment helloworld-deployment
  282  kubectl get pods 
  283  kubectl scale --replicas=15 deployment helloworld-deployment
  284  kubectl get pods 
  285  kubectl describe deployment helloworld-deployment
  286  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:2
  287  kubectl  get pods --show-labels
  288  kubectl get rs 
  289  kubectl describe rs helloworld-deployment-78cf6987f9
  290  kubectl get rs 
  291  kubectl describe rs helloworld-deployment-558759896c
  292  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:3
  293  kubectl get rs 
  294  kubectl describe rs helloworld-deployment-ff6c77c8
  295  ls
  296  kubectl rollout status deployment helloworld-deployment
  297  kubectl rollout undo deployment helloworld-deployment
  298  kubectl get rs
  299  kubectl rollout undo deployment helloworld-deployment
  300  kubectl get rs
  301  kubectl rollout history deployment helloworld-deployment
  302  kubectl rollout history deployment helloworld-deployment --revsion=5
  303  kubectl rollout history deployment helloworld-deployment --revision=5
  304  kubectl rollout history deployment helloworld-deployment --revision=4
  305  kubectl rollout history deployment helloworld-deployment --revision=1
  306  kubectl rollout undo deployment helloworld-deployment --to-revision=1
  307  kubectl get rs
  308  kubectl rollout history deployment helloworld-deployment 
  309  kubectl rollout history deployment helloworld-deployment --revision=6
  310  kubectl rollout history deployment helloworld-deployment --revision=5
  311  kubectl rollout history deployment helloworld-deployment --revision=4
  312  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:4 --record
  313  kubectl rollout history deployment helloworld-deployment 
  314  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:3 --record
  315  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:2 --record
  316  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web --record
  317  kubectl rollout history deployment helloworld-deployment 
  318  kubectl get rs 
  319  ls
  320  kubectl delete -f helloworld.yaml 
  321  vim helloworld-v2.yaml
  322  ls
  323  cat helloworld.yaml 
  324  vim helloworld-v2.yaml
  325  kubectl create -f helloworld-v2.yaml 
  326* 
  327  kubectl  describe deploy helloworld-2-deployment
  328  ls
  329  kubectl set image deployment helloworld-2-deployment k8s-demo=amitvashist7/k8s-tiny-web:2 --record
  330  kubectl delete -f helloworld-v2.yaml 
  331  vim helloworld-v3.yaml 
  332  kubectl create -f helloworld-v3.yaml 
  333  kubectl  describe deploy helloworld-3-deployment
  334  kubectl set image deployment helloworld-3-deployment k8s-demo=amitvashist7/k8s-tiny-web:2 --record
  335  ls
  336  cd ..
  337  ls
  338  cd 05-Deployments/
  339  ls
  340  history > README.md
