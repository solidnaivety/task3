# DevChallenge Automated Tests

## Overview

This project contains automated tests for the [DevChallenge](https://www.devchallenge.it) website. The tests are written in Python using Selenium and are designed to run headfully without the need to manually specify the Chrome WebDriver location.

## Test Cases

1. **Contact Email is Visible**
   - Navigate to `Dev Challenge → About` page.
   - Scroll to the bottom and verify the contact email `hello@devchallenge.it` is displayed.

2. **Count Judges**
   - Navigate to `Dev Challenge → Judges` page.
   - Verify that there are exactly 6 judges listed.

3. **No Mobile Partners**
   - Use a mobile viewport (Samsung Galaxy S21 - 360x800).
   - Navigate to `Dev Challenge → Partners` page.
   - Verify that `Apple Inc` is not listed among the partners.

## Prerequisites

- **Operating System:** Any (Windows, macOS, Linux)
- **Python:** Version 3.7 or higher
- **Google Chrome Browser:** Installed on your machine

## Setup Instructions

1. **Install Python**

   - Download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).
   - Ensure that Python is added to your system's PATH.

2. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
