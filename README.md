# Fake Gold Bar Identification Challenge

This project automates the process of identifying a fake gold bar among nine using a balance scale on a web-based challenge. The solution is implemented using Python and Selenium WebDriver.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.8+**: Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/).
- **Google Chrome**: Make sure Google Chrome is installed. The script uses Chrome as the browser for automation.
- **ChromeDriver**: Download the version of ChromeDriver that matches your installed version of Chrome. You can get it from [ChromeDriver Downloads](https://googlechromelabs.github.io/chrome-for-testing/). Ensure that the `chromedriver` executable is in your system's PATH or specify its path in the script.

# Usage

To run the script and find the fake gold bar:

1. **Open the Terminal/Command Prompt.**
2. **Navigate to the Project Directory:**

    ```bash
    cd <your-repo-directory>
    ```

3. **Run the Script:**

    ```bash
    python main.py
    ```

The script will automate the process of identifying the fake gold bar by performing weighings and interacting with the website. The identified fake bar number and the result will be printed in the console.

# How It Works

### Setup:

- The script opens the challenge webpage in incognito mode using Chrome.

### Reset Bowls:

- Before each weighing, the script resets the bowls to ensure a clean slate.

### Weighing:

- The script simulates placing three bars on each side of the scale for the first weighing and records the result.
- Based on the result, the lighter group is identified.
- The second weighing involves comparing individual bars from the lighter group to pinpoint the fake one.

### Click Fake Bar:

- The script clicks on the identified fake bar and captures the alert message.

### Output:

- The script prints the identified fake bar number and the sequence of weighings in the console.

### Error Handling

- The script handles unexpected alerts that may appear during the process, ensuring smooth execution.

### Troubleshooting

- **Browser Not Opening:** Ensure that ChromeDriver is correctly installed and its path is added to your system's PATH.
- **Script Errors:** Verify that all dependencies are installed and the website is accessible.
