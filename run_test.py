# run_test.py
import pytest
import sys
import os

# Ensure the root directory is on the path so imports work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# Define the directory where your tests and conftest are located
TEST_DIR = 'tests'

# Check if a specific file was requested (optional, for debugging)
if len(sys.argv) > 1:
    test_path = sys.argv[1]
else:
    # Default run command: Run all tests in the tests/ directory
    test_path = TEST_DIR

# Execute pytest with HTML reporting
print(f"Attempting to run tests in: {test_path}")

# We use subprocess or direct execution of pytest.main
# Using the direct path is most reliable.

try:
    # Run pytest programmatically
    exit_code = pytest.main([
        test_path, 
        '--html=report.html',
        '--self-contained-html',
        '-v' # verbose output to see what happens
    ])
    print(f"Pytest execution finished with exit code: {exit_code}")

except Exception as e:
    print(f"An error occurred during pytest execution: {e}")

# You can now run this script using: python run_test.py