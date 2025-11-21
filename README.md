🧪 Behave API Automation Framework

This is a BDD-style API automation framework built using Python, Behave, and Allure Reporting, integrated with GitHub Actions CI/CD. It is designed for REST API testing with a focus on clean structure, reusability, and real-world practices.

📌 Features

✅ BDD with Behave and Gherkin syntax

✅ Data-driven testing support

✅ Advanced validations (headers, schema, response structure)

✅ Retry mechanism & timeout handling

✅ Allure reporting for HTML reports

✅ Logging with timestamps

✅ .env support for secure configuration

✅ GitHub Actions for CI/CD

✅ Modular structure (utilities, steps, configs)

🔧 Technologies Used

| Tool           | Purpose                       |
|----------------|-------------------------------|
| Python         | Core scripting language       |
| Behave         | BDD framework                 |
| Requests       | API calls                     |
| Allure         | HTML test reporting           |
| GitHub Actions | CI/CD automation              |
| dotenv         | Environment variable management |

📁 Project Structure

```bash
behave-api-testing-framework/
├── features/
│   ├── steps/                  # Step definitions (Python)
│   ├── environment.py         # Hooks for setup/teardown
│   ├── *.feature              # Gherkin test files
├── reports/
│   └── allure-results/        # Raw test results for Allure
├── utils/
│   ├── logger.py              # Central logging setup
│   ├── api_helper.py          # Request handlers with retry, timeout
│   └── token_manager.py       # Token-based authentication support
├── .env                       # Base URL and secrets
├── requirements.txt           # Dependencies
└── .github/workflows/         # GitHub Actions workflow
```

🚀 Getting Started

1. Clone the repository

```bash
git clone git@github.com:your-username/behave-api-testing-framework.git
cd behave-api-testing-framework
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Add .env file

Create a `.env` file in root:


BASE_URL=https://restful-booker.herokuapp.com


4. Run tests with Allure output

```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

5. Generate Allure HTML report

```bash
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

🤖 GitHub Actions – CI/CD

On every push to main, GitHub Actions:

- Sets up Python
- Installs dependencies
- Runs Behave tests
- Uploads Allure result artifacts

Sample workflow:

`.github/workflows/behave-tests.yml`

```yaml
name: Run Behave Tests

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

📊 Logging
Logging is handled via `logger.py`:
```log
2025-08-31 14:30:22 - INFO - Base URL is set to https://jsonplaceholder.typicode.com
```




Made with 💻 by Sachin Mate

🌐 GitHub Pages

This repository now publishes the contents of the `docs/` folder to GitHub Pages via `.github/workflows/pages.yml`. To enable it:
1. Open **Settings → Pages** and choose **GitHub Actions** as the source.
2. Push to `main` (or run the workflow manually) to deploy.
3. Edit `docs/index.md` (or add additional markdown files) to update the site content.

