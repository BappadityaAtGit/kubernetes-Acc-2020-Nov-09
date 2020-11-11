 14  echo "amitvashist7@outlook.com" | base64
   15  echo "amitvashist7@outlook.com" | base64 > /root/username.txt
   16  echo "Accenture@432!" | base64 > /root/password.txt
   17  cat /root/username.txt
   18  cat /root/password.txt
   19  kubectl get deploy
   20  kubectl delete deploy --all
   21  kubectl get deploy
   22  ls
   23  kubectl get secrets
   24  kubectl  get pods
   25  kubectl describe pod mywebapp
   26  ls
   27  kubectl get secrets
   28  kubectl create secret --help
   29  kubectl create secret generic --help
   30  kubectl create secret generic my-secret --from-file=/root/username.txt  --from-file=/root/password.txt
