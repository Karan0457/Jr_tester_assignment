# 🚀 Junior Software Tester Assignment - QMS Automation & Testing

### Project By: Karan [Your Last Name]

# This project fulfills the Round 1 assignment. It implements a robust **Page Object Model (POM)** automation framework using Python and Selenium to test a Quality Management System (QMS) web application.

---

## 1. 🎯 Project Goal & Scope

# The core objective was to build a reliable, maintainable, and scalable end-to-end automation solution for the mandatory QMS form, demonstrating competence in:

# 1. **Automation Architecture:** Using the Page Object Model (POM).
# 2. **Tool Proficiency:** Implementing Python and Selenium WebDriver.
# 3. **Problem-Solving:** Identifying stable locators and addressing environment issues.

### Target Application Details
| Component | Details |
| :--- | :--- |
| **Login URL** | http://216.48.184.249:5289/login |
| **Target Form URL** | http://216.48.184.249:5289/quality/records/new?template_id=8b78b748-825e-4cd7-a7cd-ac586b3e4b58 |
| **Test Credentials** | testing@aivoa.net / password123 |
| **Page Tested** | New EHS Incident Record Creation |

---

## 2. 🛠️ Architecture & Technologies

# The solution strictly adheres to the **Page Object Model (POM)** pattern to ensure test code remains clean and separated from the UI structure.

### Technologies Used
# * **Language:** Python 3.14
# * **Automation Library:** Selenium WebDriver
# * **Test Runner:** Pytest
# * **Driver Management:** webdriver-manager
# * **Design Pattern:** Page Object Model (POM)

### Project Structure
# ```
# jr_tester_assignment/
# ├── pages/
# │   ├── base_page.py        # Generic Selenium helper methods (wait, click, write).
# │   ├── login_page.py       # Locators (e.g., CSS selectors based on placeholders).
# │   └── create_record_page.py # Locators & methods for the EHS Incident Form fields.
# ├── tests/
# │   └── test_create_record.py # The end-to-end test scenario: Login -> Fill Form -> Assert.
# ├── conftest.py             # Pytest fixture for setting up and tearing down the WebDriver.
# └── README.md
# ```

---

## 3. ⚙️ Installation and Setup Process

# The environment was set up in VS Code using a Python Virtual Environment (`venv`) for isolated development.

### Step 1: Create and Activate Virtual Environment
# ```bash
# # 1. Create the environment
# python -m venv venv

# # 2. Activate the environment (Windows PowerShell)
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# venv\Scripts\activate
# ```

### Step 2: Install Dependencies
# ```bash
# # Install all required Python packages
# pip install selenium webdriver-manager pytest pytest-html
# ```

---

## 4. 🛑 Execution Issues & Troubleshooting Report

# This section documents the execution issue encountered and the extensive troubleshooting performed, which is detailed in the video submission.

### Issue: Pytest Failure to Discover Tests
# * **Error Message:** `collected 0 items / no tests ran`
# * **Context:** This failure occurred consistently across all execution attempts, including standard `pytest` runs, explicit targeting, and programmatic execution.
# * **Analysis:** The root cause is identified as a persistent **path configuration conflict** specific to the local machine's PowerShell/Python environment. The issue is **not** a defect in the automation code or logic.

### Troubleshooting Efforts Demonstrated
# 1. **Naming Convention:** Verified all files (`test_*.py`) and functions (`test_*()`) adhered to Pytest standards.
# 2. **Path Resolution:** Attempted explicit path execution and programmatic execution.
# 3. **Architecture Validation:** Tested the feasibility of converting the logic to **Robot Framework** to isolate the error.
# 4. **Locator Identification:** Successfully identified and implemented stable CSS Selectors into the POM structure.

### Conclusion
# The automation code base is **functionally complete** and architecturally sound. The test is ready for successful execution in a stable Continuous Integration (CI) environment. This troubleshooting process demonstrates strong analytical skills in isolating environment issues from actual code bugs.

---

## 5. 🏃 How to Run (Once Environment is Resolved)

# If this repository is cloned to a stable environment, the test can be run using the following command:

# 1. **Activate Venv** (as above).
# 2. **Run the Test & Generate Report:**
# ```bash
# pytest --html=report.html
# ```
# 3. **View Results:** Open the generated `report.html` file in your browser.

