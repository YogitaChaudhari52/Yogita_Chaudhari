from selenium import webdriver
import subprocess
from os.path import dirname, join

MAIN_DIRECTORY = dirname(dirname(__file__))


def get_directory(*path):
    return join(MAIN_DIRECTORY, *path)

#Making Dynamic Path using folder and file name we can get any path
def Path():
    path_to_map = get_directory('Drivers', 'chromedriver.exe')
    return path_to_map

def LaunchURL():
    driver= Driver()
    # URL of the website
    url = "https://www.888sport.com/football/europe/euro-2020/"
    # opening link in the browser
    driver.get(url)
    return driver



def Driver():
    # selecting Chrome as the browser
    # in order to select Chrome
    # webdriver.Chrome() will be used
    path=Path()
    driver = webdriver.Chrome(path)
    driver.maximize_window()
    return driver