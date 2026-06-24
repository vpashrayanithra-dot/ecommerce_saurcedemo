# E-commerce Automation Test Suite

## Description
This project is an automated test suite developed to validate key functional workflows for the SauceDemo e-commerce platform. It serves as a professional-grade framework designed to bridge the gap between academic scripting and industrial-standard QA automation. 

## Development Philosophy
This project was developed through an **AI-augmented development approach**. I utilized AI as a mentor to guide the architectural design, optimize Python scripting, and troubleshoot CI/CD configurations. My goal was to move from fundamental automation concepts to building a fully functional, professional-grade pipeline while gaining a deep, practical understanding of modern software quality engineering.

## Tech Stack
* **Language:** Python
* **Testing Framework:** Pytest
* **Browser Automation:** Selenium WebDriver
* **CI/CD:** GitHub Actions
* **Version Control:** Git/GitHub

## Key Features
* **Automated Regression Testing:** Executes critical test cases automatically upon code changes.
* **CI/CD Integration:** Integrated with GitHub Actions for continuous, automated testing in a headless environment.
* **Environment Parity:** Managed dependencies using `requirements.txt` to ensure consistency across local and cloud environments.
* **Headless Execution:** Configured for optimized performance in automated cloud-based testing workflows.

## How to Run Locally
1. **Clone the repository:**
```bash
   git clone [https://github.com/vpashtayanithra-dot/ecommerce_saurcedemo.git](https://github.com/vpashtayanithra-dot/ecommerce_saurcedemo.git)
Install dependencies:

Bash
   pip install -r requirements.txt
Run the tests:

Bash
   pytest
CI/CD Pipeline
This project uses GitHub Actions to automate testing. Every time code is pushed to the main branch, the pipeline automatically:

Sets up the Python environment.

Installs all necessary dependencies.

Executes the test suite in a headless browser.

Reports the success or failure of the build.
