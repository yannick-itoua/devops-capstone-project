---
name: Update an account in the service
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: ''

---

**As a** user  
**I need** to update an account in the service  
**So that** I can modify customer details  

### Details and Assumptions
* Endpoint supports updating fields like name and address.
* Account must exist to be updated.

### Acceptance Criteria     
```gherkin
Given an existing account
When I make a PUT request with updated details
Then the account is updated and the changes are saved
