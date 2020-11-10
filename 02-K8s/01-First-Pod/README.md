# Creating First Pod with Nginx 

```
kubectl get pods 
```
```
kubectl run hello-k8s --image=nginx --port=80
```
```
kubectl get pods
```

# Creating a Second Pod with custom webapp image. 

```
kubectl run mywebapp --image=amitvashist7/my-python-webapp:v1 --port=8080
```
