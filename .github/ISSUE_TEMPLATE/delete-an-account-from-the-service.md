---
name: Delete an account from the service
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: ''

---

**As a** user  
**I need** to delete an account from the service  
**So that** I can remove outdated or unnecessary customer records  

### Details and Assumptions
* Account must exist to be deleted.
* Deletion is irreversible.

### Acceptance Criteria     
```gherkin
Given an existing account ID
When I make a DELETE request to the endpoint
Then the account is removed from the database
