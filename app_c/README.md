# Appendix C: Deploying the SmartCMS on Azure’s Kubernetes Service

## Pre-requisites

To install the az-cli, see: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest.

To setup a Kubernetes cluster on Azure, follow the steps here: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-portal?tabs=azure-cli until but not including the "Deploy the application" step.

Once you're done creating the cluster, grab the public IP assigned to your cluster with:
```sh
az network public-ip list --query "[?starts_with(resourceGroup, 'MC_') && ipAddress!=null].{Name:name, ResourceGroup:resourceGroup, IP:ipAddress}" -o table
```

You'll get output that looks like this:
```sh
Name          ResourceGroup             IP
------------  ------------------------  -----------
715a31e6-...  MC_sswasm_sswasm_westus2  4.155.90.17
```

With this, you can set the public-ip'S DNS name like this:
```sh
az network public-ip update --resource-group <YOUR PUBLIC IP'S RG> --name <YOUR PUBLIC IP'S NAME> --dns-name <YOUR PUBLIC IP'S DNS NAME> --query "dnsSettings.fqdn"
```

Replace `<YOUR PUBLIC IP'S RG>` with the resource group name, `<YOUR PUBLIC IP'S NAME>` with the public IP's name (i.e., the leftmost column), and `<YOUR PUBLIC IP'S DNS NAME>` with a DNS name of your choice (e.g., `danbugssmartcms`). Grab the public IP's FQDN outputted from this command (e.g., `danbugssmartcms.westus2.cloudapp.azure.com`) as it will be used in the Ingress configuration later.

Aside from that, I've already built frontend image and pushed it to GHCR.
```sh
docker build -t ghcr.io/danbugs/smartcms-frontend:v1 ./frontend/
docker push ghcr.io/danbugs/smartcms-frontend:v1
```

In subsequent steps, we'll be using this image to deploy the frontend of the SmartCMS.

## Steps

### Prepare cluster

(1) Install the wasmcloud-platform:
```sh
helm upgrade --install wasmcloud-platform --values https://raw.githubusercontent.com/wasmCloud/wasmcloud/main/charts/wasmcloud-platform/values.yaml oci://ghcr.io/wasmcloud/charts/wasmcloud-platform:0.1.2 --dependency-update
```

(2) Configure ingress (replace `<YOUR PUBLIC IP HERE>` with the public IP you got in the pre-requisite step):
```sh
helm upgrade --install ingress-nginx ingress-nginx/ingress-nginx --namespace ingress-nginx --create-namespace --set controller.replicaCount=2 --set controller.nodeSelector."kubernetes\.io/os"=linux --set defaultBackend.nodeSelector."kubernetes\.io/os"=linux --set controller.service.externalTrafficPolicy=Local --set controller.service.loadBalancerIP="<YOUR PUBLIC IP HERE>"
```

After deploying the ingress controller, it may take a few minutes for the EXTERNAL-IP to show up. You can check it using:
```sh
kubectl get svc -n ingress-nginx
```

(3) Install cert-manager to enable TLS with HTTPS:
```sh
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/latest/download/cert-manager.yaml
kubectl wait --namespace cert-manager --for=condition=Available deployment/cert-manager --timeout=120s

```

(4) Create a cluster issuer for Let's Encrypt.

Here's an example of a `ClusterIssuer` configuration for Let's Encrypt. Replace `<YOUR EMAIL HERE>` with your email address to receive notifications about certificate expiration and issues.
```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    email: <YOUR EMAIL HERE>
    server: https://acme-v02.api.letsencrypt.org/directory
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
      - http01:
          ingress:
            class: nginx
```

With this file saved as `cluster-issuer.yaml`, apply it with:
```sh
kubectl apply -f cluster-issuer.yaml
```

(5) Create Wasmcloud host
```sh
kubectl apply -f https://raw.githubusercontent.com/danbugs/serverside-wasm-book-code/refs/heads/main/app_c/setup/wasmcloud-host.yaml
```

### Deploy the SmartCMS

(1) Deploy the backend components:
```sh
kubectl apply -f https://raw.githubusercontent.com/danbugs/serverside-wasm-book-code/refs/heads/main/app_c/backend/ollama.yaml
kubectl rollout status deployment/ollama --timeout=120s
kubectl apply -f https://raw.githubusercontent.com/danbugs/serverside-wasm-book-code/refs/heads/main/app_c/backend/wadm.yaml
kubectl apply -f https://raw.githubusercontent.com/danbugs/serverside-wasm-book-code/refs/heads/main/app_c/backend/wasmcloud-api.yaml
```

> Note: We have a `wasmcloud-api` service now because we won't be directly port-forwarding the API service anymore. Instead, we'll be using the Ingress to route traffic to it.

(2) Deploy the frontend:
```sh
kubectl apply -f https://raw.githubusercontent.com/danbugs/serverside-wasm-book-code/refs/heads/main/app_c/frontend/frontend.yaml
```

(3) Configure Ingress
Here's an example of an Ingress configuration. Save it as `ingress.yaml`:
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - <YOUR PUBLIC IP'S FQDN>
      secretName: sswasm-tls  
  rules:
    - host: <YOUR PUBLIC IP'S FQDN>
      http:
        paths:
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: wasmcloud-api
                port:
                  number: 8000
          - path: /
            pathType: Prefix
            backend:
              service:
                name: smartcms-frontend
                port:
                  number: 80
```

Apply the Ingress configuration with:
```sh
kubectl apply -f ingress.yaml
```

> Note: You could also buy a domain and point it to the public IP of your cluster!

Once this is all done, you should be able to access the SmartCMS frontend at `https://<YOUR PUBLIC IP'S FQDN>`. To view my own deployment, visit https://sswasm.com/

> Note: 
>> - Deploying an update to the frotend image? Run: `kubectl delete pod -l app=smartcms-frontend`