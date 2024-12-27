---
name: Read an account from the service
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: ''

---

**As a** user  
**I need** to read an account from the service  
**So that** I can view customer details  

### Details and Assumptions
* Endpoint will retrieve account by ID.
* Account details include name and address.

### Acceptance Criteria     
```gherkin
Given an account ID
When I make a GET request to the endpoint
Then the account details are returned
