# Kubernetes DevOps Platform (Reference Documentation)

## Overview

This project demonstrates a production-style Kubernetes deployment of a containerized FastAPI application. It includes deployment, service exposure, ingress routing, resource management, health checks, and autoscaling.

---

## Architecture

User → Ingress → Service → Pods → Containers

* **Ingress**: Routes external HTTP traffic to the service
* **Service**: Provides stable networking and load balancing
* **Deployment**: Manages pod lifecycle and replicas
* **Pods**: Run the application containers

---

## Components

### 1. Deployment

* Manages pods using ReplicaSet
* Ensures desired number of replicas
* Supports rolling updates and self-healing

Key Concepts:

* `replicas`: Number of pods
* `selector`: Identifies pods to manage
* `template`: Pod blueprint (containers, labels)

---

### 2. Service

* Provides stable IP and DNS
* Load balances traffic across pods

Types:

* ClusterIP (default)
* NodePort (used in this project)
* LoadBalancer

---

### 3. Ingress

* Acts as HTTP reverse proxy
* Routes traffic based on host/path

Requires:

* Ingress Controller (NGINX in Minikube)

---

## Resource Management

### Requests

* Minimum required resources
* Used by scheduler

### Limits

* Maximum allowed resources
* Enforced at runtime

Example:

* CPU: 150m request, 500m limit
* Memory: 128Mi request, 256Mi limit

---

## Health Checks (Probes)

### Liveness Probe

* Checks if container is alive
* Restarts container on failure

### Readiness Probe

* Checks if container is ready to serve traffic
* Removes pod from service if failed

---

## Autoscaling (HPA)

* Scales pods based on CPU usage
* Uses percentage of requested CPU

Example:

* Target: 50% CPU
* Min pods: 2
* Max pods: 6

---

## Failure Handling

### Pod Failure

* Automatically recreated by ReplicaSet

### Node Failure

* Pods rescheduled on other nodes (if available)

### Application Failure

* Leads to CrashLoopBackOff
* Requires fix in code/config

---

## Key Commands

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
kubectl describe pod <pod>
kubectl logs <pod>
kubectl top pods
kubectl delete pod <pod>
```

---

## Key Learnings

* Kubernetes is declarative (desired vs actual state)
* Services provide stable networking abstraction
* Ingress handles external traffic routing
* Probes improve reliability and traffic control
* HPA enables dynamic scaling based on load

---

## Future Enhancements

* CI/CD pipeline integration
* Docker image registry setup
* Terraform-based infrastructure provisioning
* Monitoring (Prometheus, Grafana)

---

## Folder Structure (Recommended)

```
k8s-devops-platform/
  ├── app/
  ├── k8s/
  ├── docker/
  ├── docs/
  └── README.md
```

---

## Notes

This project is designed to simulate real-world DevOps practices including scalability, fault tolerance, and automation readiness.
