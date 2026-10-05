# Tasks

Small practice exercises from learning DevOps tooling (committed 2024): Docker,
Docker Compose, Jenkins on Kubernetes, Helm, nginx and Python scripting. Each
folder is independent. These are learning exercises, not maintained projects;
the status column says what was checked in October 2026.

| Folder | What it is | Status |
| --- | --- | --- |
| [`Flask_docker-compose`](Flask_docker-compose) | Flask + Redis hit counter run with Docker Compose (Docker's Compose getting-started sample) | Runs: `docker compose up` |
| [`python/date_listener`](python/date_listener) | Raw TCP server on port 8080 that returns today's date, in a Docker image | Runs |
| [`nginx`](nginx) | nginx image with a reverse-proxy config for `/hello` | Image builds; proxy target not included |
| [`jenkins/jenkins-k8s`](jenkins/jenkins-k8s) | Jenkins on minikube: Deployment, NodePort Services, PV/PVC, RBAC, plus the same as a Helm chart | Manifests validate (kubeconform), chart lints |
| [`jenkins/Jenkinsfile`](jenkins/Jenkinsfile) | Parameterised pipeline that runs `terraform apply`/`destroy` for an EC2 config ([Terraform repo](https://github.com/shaharco99/Terraform/tree/main/terraform-EC2)) with AWS keys from Jenkins credentials | Not run; uses a local path on the original machine |
| [`jenkins/docker-jenkins`](jenkins/docker-jenkins) | Jenkins in Docker Compose, a custom Jenkins image with plugins, and a plugin-update script | Not verified |
| [`grafana_piplane`](grafana_piplane) | Prometheus and Grafana config files and a Jenkinsfile | Incomplete: the Dockerfiles and compose file it references are not in the repo |
| [`selenium`](selenium) | Selenium + Chrome image | Broken: the chromedriver download URL it uses no longer exists |
| [`google_search`](google_search) | Prints the top Google results for a query | Not verified |
| [`python`](python) | Short scripts: HTTP request, directory count, interest calculator | Not verified |

## Examples

```bash
cd Flask_docker-compose
docker compose up -d --build
curl localhost:8000        # Hello World! I have been seen 1 times.
curl localhost:8000        # Hello World! I have been seen 2 times.
docker compose down
```

```bash
cd python/date_listener
docker build -t date .
docker run -d --rm -p 8080:8080 --name date date
curl --http0.9 localhost:8080
# Today is Monday
# The current date is 2026-10-05
docker stop date
```
