---
name: Deploy your Docker image to Kubernetes
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: ''

---

**As a** developer  
**I need** to deploy the Docker image to Kubernetes  
**So that** the service is available in a scalable and resilient environment  

### Details and Assumptions
* Use Kubernetes deployment and service definitions.
* Image is pushed to a container registry.

### Acceptance Criteria     
```gherkin
Given a Docker image is available
When I apply the Kubernetes manifests
Then the service is running in the cluster
