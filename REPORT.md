**1. Setup and Steps Followed**

Step 1: Repository Setup
Created a GitHub repository for the project.
Initialized the repository with a .gitignore file for Python projects.
Added all source code and committed the changes.

**Step 2: CI/CD Pipeline Configuration**

Created a .github/workflows/ci.yml file to define the GitHub Actions workflow.

**Configured three jobs:**

**test:** Runs unit tests using pytest.
![1](https://github.com/user-attachments/assets/76d593a1-4cb5-4ce7-bc21-4fc0c445aae3)

**build:** Builds Docker images using docker compose.
![2](https://github.com/user-attachments/assets/f1d5200a-9736-4b2b-a049-0996aa5323b3)

**deploy:** Deploys the services using docker compose up -d.
![3](https://github.com/user-attachments/assets/af8962ae-bf02-4925-bc93-b0e3120676cf)

**SUMMARY:**
![sum](https://github.com/user-attachments/assets/3789ed7d-2bc8-4ff7-9aaf-6613ce0b9dd9)

**RUNTIME:**
![run](https://github.com/user-attachments/assets/0b589bd4-a882-4dc6-aaa7-46a009a28a8c)
