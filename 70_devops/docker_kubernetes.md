# DevOps for AI: Docker and Kubernetes

DevOps makes AI systems operational and scalable.

## 1. Docker
Docker packages applications and dependencies into containers.

### Example Dockerfile
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

### Commands
```bash
docker build -t my-ai-app .
docker run -p 8000:8000 my-ai-app
```

## 2. Docker Compose
Used to orchestrate multi-container apps:
- app service
- database service
- cache service
- monitoring service

## 3. Kubernetes
Kubernetes is used to manage containerized workloads at scale.

Core concepts:
- pod
- deployment
- service
- configmap
- secret
- ingress
- node
- cluster

## 4. CI/CD
Common pipeline steps:
- checkout code
- install dependencies
- run tests
- build container
- deploy to staging/production

## 5. Infrastructure as code
- Terraform
- Helm
- Ansible

## 6. Monitoring
- Prometheus
- Grafana
- logging pipelines
- alerts and dashboards

## 7. Why DevOps matters for AI
AI projects often fail not because models are wrong, but because:
- deployment is manual
- environments are inconsistent
- scaling is poor
- monitoring is missing
- retraining is not automated

## 8. Goal
Learn how to deploy and run AI systems reliably in real production environments.
