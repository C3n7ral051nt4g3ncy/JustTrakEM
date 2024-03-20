# Just Trak'EM ✓
Sports Tracker Large Scale Profile Checker 

<img src="https://github.com/C3n7ral051nt4g3ncy/JustTrak-EM/assets/104733166/a68c0814-89b0-4ff9-b814-0e32a900fe8b" width='633'>

## Description

I created this script for myself after finding weaknesses on [Sports Tracker](https://www.sports-tracker.com). 
I had a large list of approx. 1000 names to check and had to automate the process, it would have taken months to do it manually.
I explained the whole process on this thread on [X](https://twitter.com/OSINT_Tactical/status/1770471606038483270)


The **Sports Tracker Profile Checker** is an automated tool designed to check for the existence of user profiles on the Sports Tracker app based on a list of names. 
It's particularly useful for handling large datasets, making it an excellent resource for researchers, data analysts, and privacy advocates interested in assessing user visibility and privacy on the platform.

## Features

- **Automated Profile Checking**: Quickly verifies the presence of Sports Tracker profiles for a list of names.
- **Large Dataset Handling**: Optimized for performance with extensive lists, facilitating bulk operations with ease.
- **Privacy-Focused**: Aids in privacy impact assessments and highlights the importance of conscious privacy settings in social fitness platforms.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.10
- Brave Browser (or modify the script for your preferred Chromium-based browser)
- *Please not that the path to the Brave Browser in the scrpt is the usual path on MacOS (Change it according to your own OS and path)
- chromedriver-py is version 122.0.6261.128 as you can see in the requirements.txt file, this can be changed to suite your Brave browser version.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/C3n7ral051nt4g3ncy/JustTrakEM.git
   cd JustTrakEM

2. **Set up a VENV (Virtual Environment)** (Optional but recommended to avoid conflicting libs)
3. **Install Required Python Libraries**
   ```bash
   pip install -r requirements.txt

## Usage 

1. **Prepare Your Names List**

   Create a text file named full_names.txt and populate it with full names from companies, organizations, or any list of names you have, each on a new line.

   You can test this tool with names that I generated randomly in the ```full_names.txt``` file, if you are happy everything works correctly, you can then put your own names in the file.


3. **Run the Script**

   ```python3 trak.py```


**The script will process each name from the list, checking for existing profiles on Sports Tracker and outputting the results when a profile is found matching the name.**

## Customization
To use a browser other than Brave, adjust the ```brave_path``` variable in the script to point to the executable of your preferred Chromium-based browser.
Customize the delay or add additional Selenium configurations as needed.

## Contributing
Contributions to Just Trak'EM are welcome! Please submit a pull request or create an issue for any features, bug fixes, or enhancements.

## License
This project is licensed under the MIT License

## Acknowledgments
This tool was created for educational and research purposes. Please use it responsibly and ethically.

