---
name: List all accounts in the service
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: ''

---

**As a** user  
**I need** to list all accounts in the service  
**So that** I can see a complete overview of customer records  

### Details and Assumptions
* Endpoint returns a paginated list of accounts.
* Accounts include names and addresses.

### Acceptance Criteria     
```gherkin
Given multiple accounts in the database
When I make a GET request to the list endpoint
Then all accounts are returned in a paginated response
