## Launch app

1. Connect to Minikube's Docker daemon:
```powershell
& minikube -p minikube docker-env --shell powershell | Invoke-Expression
```

2. Build the images:
```powershell
docker-compose build
```

3. Apply Kubernetes manifests:
```powershell
kubectl apply -f pv.yaml
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f backend-service.yaml
kubectl apply -f frontend-service.yaml
kubectl apply -f hpa.yaml
```

4. Create Service for frontend
```powershell
minikube service frontend
```