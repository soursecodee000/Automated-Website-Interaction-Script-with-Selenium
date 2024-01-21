# Selenium Video Automation Script

## Overview

This Python script leverages the Selenium library to automate interactions with a website. The primary goal is to open a webpage, wait for a video to start playing, click a designated button on the page, and play the video for a randomized duration. The entire process is repeated 1000 times using a list of URLs read from a text file.

## Features

- **Automated Interaction:** The script automates the process of interacting with a website, targeting a video element and a specific button.

- **Randomized Video Duration:** The script plays the video for a random duration between 30 seconds and 1.5 minutes, providing variability in the automated process.

- **Error Handling:** Comprehensive error handling is implemented to catch and print exceptions, ensuring smoother execution and debugging.

## Prerequisites

- Python 3.x
- Selenium library (`pip install selenium`)
- ChromeDriver (automatically managed by `ChromeDriverManager`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/soursecodee000/selenium-video-automation.git


Navigate to the project directory:


cd selenium-video-automation


Install required dependencies:

pip install -r requirements.txt

Create a text file named Links_list.txt and add the URLs you want to automate, one per line.

Run the script:

python script.py

Observe the automated interactions with the specified websites.

Configuration
You can customize additional options in the options variable within the automate_website function in script.py.

Disclaimer
This script is provided as-is and assumes that the webpage structure and elements are consistent across the target websites. Use responsibly and ensure compliance with the terms of service of the websites being automated.

License
This project is licensed under the MIT License.


Remember to replace "soursecodee000" in the repository URL with your actual GitHub username. Also, make sure to include a license file (e.g., `LICENSE`) in your project directory if you want to specify licensing terms.




