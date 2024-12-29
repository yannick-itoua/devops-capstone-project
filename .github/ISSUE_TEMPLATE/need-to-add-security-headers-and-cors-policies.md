---
name: Need to add security headers and CORS policies
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: ''

---

Title: Need to add security headers and CORS policies
    **As a** service provider
    **I need** my service to use security headers and CORS policies
    **So that** my web site is not vulnerable to CORS attacks
    #### Assumptions
    * Flask-Talisman will be used for security headers
    * Flask-Cors will be used to establish cross-origin resource sharing (CORS) policies
    #### Acceptance Criteria
    ```gherkin
    Given the site is secured
    When a REST API request is made
    Then secure headers and a CORS policy should be returned
    ```
