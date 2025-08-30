🧪 Behave API Automation Framework

This is a BDD-style API automation framework built using Python, Behave, and Allure Reporting, integrated with GitHub Actions CI/CD. It is designed for REST API testing with a focus on clean structure, reusability, and real-world practices.

📌 Features

✅ BDD with Behave and Gherkin syntax

✅ Data-driven testing support

✅ Allure reporting for HTML reports

✅ Logging with timestamps

✅ .env support for secure configuration

✅ GitHub Actions for CI/CD

✅ Modular structure (utilities, steps, configs)

🔧 Technologies Used

Tool

Purpose

Python

Core scripting language

Behave

BDD framework

Requests

API calls

Allure

HTML test reporting

GitHub Actions

CI/CD automation

dotenv

Environment variable management

📁 Project Structure

behave-api-testing-framework/
├── features/
│   ├── steps/                  # Step definitions (Python)
│   ├── environment.py         # Hooks for setup/teardown
│   ├── *.feature              # Gherkin test files
├── reports/
│   └── allure-results/        # Raw test results for Allure
├── utils/
│   └── logger.py              # Central logging setup
├── .env                       # Base URL and secrets
├── requirements.txt           # Dependencies
└── .github/workflows/         # GitHub Actions workflow

🚀 Getting Started

1. Clone the repository

git clone git@github.com:your-username/behave-api-testing-framework.git
cd behave-api-testing-framework

2. Install dependencies

pip install -r requirements.txt

3. Add .env file

Create a .env file in root:

BASE_URL=https://restful-booker.herokuapp.com

4. Run tests with Allure output

behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results

5. Generate Allure HTML report

allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report

🤖 GitHub Actions – CI/CD

On every push to main, GitHub Actions:

Sets up Python

Installs dependencies

Runs Behave tests

Uploads Allure result artifacts

Sample workflow:

.github/workflows/behave-tests.yml

📊 Logging

Logging is handled via logger.py:

2025-08-31 14:30:22 - INFO - Base URL is set to https://jsonplaceholder.typicode.com

❓ FAQs

How do you manage environment configs? → Using .env + dotenv

How are reports generated? → Using allure-behave formatter + CLI tool

What’s unique about this framework? → Real-world structure + BDD + CI/CD integration

✅ To Do (Next Phases)





Made with 💻 by Sachin Mate

