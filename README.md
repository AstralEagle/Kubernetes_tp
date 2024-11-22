# Projet Final Docker k8s
Groupe de Merwan Laakad, Antoine Richard, Arthur Dias

## Launch app

1. Connect to Minikube's Docker daemon (powershell)
```
& minikube -p minikube docker-env --shell powershell | Invoke-Expression
```

2. Build the images:
```
docker-compose build
```

3. Apply Kubernetes manifests:
```
kubectl apply -f pv.yaml
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f backend-service.yaml
kubectl apply -f frontend-service.yaml
kubectl apply -f hpa.yaml
```

4. Create Service for frontend
```
minikube service frontend
```

5. Scaling
```
kubectl get hpa -w
```
