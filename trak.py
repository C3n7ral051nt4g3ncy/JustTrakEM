from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chromedriver_py import binary_path
import time
from colorama import Fore, Style, init

# Initialize colorama
from colorama import init
init(autoreset=True)


# Path to the Brave browser on MacOS
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

# Using Brave with Selenium
options = Options()
options.binary_location = brave_path
service = Service(executable_path=binary_path)
driver = webdriver.Chrome(service=service, options=options)


# Initialize colorama
init()

# Just TRAK'EM Banner
banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣶⡿⠡⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡎⢳⠤⠃⠀⠀⢠⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡰⢉⣩⠑⠑⢉⠶⢀⠀⠀⢈⣽⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⣁⠩⠚⣿⣶⣁⠀⢀⣞⠢⣠⠊⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢇⢱⠀⠀⣴⡌⠡⢊⠝⠈⠒⠇⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⡾⠄⢠⣿⠃⠄⢾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠊⢸⣧⣴⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⡟⠟⠃⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⠀⡨⠋⠉⠓⠧⢤⡀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠖⢅⠔⠉⠀⠀⠀⠀⠀⠜⠛⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡔⢁⠔⠁⠀⠀⠀⠀⠀⠀⡼⢀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡤⠾⡔⠁⠀⠀⠀⠀⠀⠀⠀⣰⢡⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢻⢸⠃⠀⠀⠀⠀⠀⠀⠀⠘⠤⡙⠆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠤⠤⠤⠤⠬⠮⠆⠄⢀⡀⠤⠤⠤⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀
⣿⣯⣯⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
 J U S T   T R A K ' EM """



def check_for_profile_not_found():
    """Check for the absence of a profile."""
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        return "Sorry, Page Not Found" in driver.page_source
    except:
        return False  

def check_profile_combinations(full_name):
    """Check for profile existence in different name combinations."""
    formats = [''.join(full_name.lower().split()), ''.join(full_name.lower().split()[::-1])]

    for username in formats:
        url = f"https://www.sports-tracker.com/view_profile/{username}"
        driver.get(url)
        time.sleep(2)  

        if not check_for_profile_not_found():
            print(Fore.GREEN + f"Profile Found for {full_name}: {url}")
            return  # Exit function after finding profile

# Print header
print(Fore.CYAN + Style.BRIGHT + "Sports Tracker Profile Checker\n")
print(Fore.CYAN + Style.BRIGHT + banner)


file_path = 'full_names.txt' 
with open(file_path, 'r') as file:
    for line in file:
        full_name = line.strip()
        check_profile_combinations(full_name)

driver.quit()
