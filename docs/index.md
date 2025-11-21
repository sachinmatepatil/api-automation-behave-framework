# Behave API Automation Framework

Welcome to the GitHub Pages site for the Behave API Automation Framework. This site provides quick links and documentation snippets to help you run the test suite, review reports, and understand the project layout.

## What is this project?
A BDD-style API automation framework built with **Python**, **Behave**, and **Allure**. It targets REST API testing with reusable helpers, schema validation, and CI integration.

## Quick start
1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
2. **Set configuration**
   Create a `.env` file (or export environment variables) with your API host settings.
   ```bash
   BASE_URL=https://restful-booker.herokuapp.com
   ```
3. **Run the suite**
   ```bash
   behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
   ```

## Viewing reports locally
After a test run you can generate and open the Allure HTML report:
```bash
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

## Repository structure
- `features/` – Gherkin feature files, environment hooks, and step definitions.
- `utils/` – Shared helpers for HTTP calls, logging, assertions, and token handling.
- `schemas/` – JSON schemas used for response validation.
- `reports/` – Allure result output from test executions.
- `.github/workflows/` – CI/CD workflows for tests and Pages deployment.

## Continuous Integration
GitHub Actions automatically runs the Behave suite on pushes to `main` and uploads Allure artifacts. The Pages workflow (added in this repository) publishes the contents of `docs/` to the `github-pages` environment for easy reference.

## Need help?
Open an issue in the repository with reproduction details and logs. Contributions and improvements are welcome!
