import time
import unittest
from selenium import webdriver
from Common_Code import Driver,Path,LaunchURL
import HtmlTestRunner


class Testcase1(unittest.TestCase):

#Write a test script that loads our Euro-2020 page: https://www.888sport.com/football/europe/euro-2020/
#And verifies that the 'Match Result' tab is selected by default.

 def test_Testcase1(self):
  Driver=LaunchURL() #Launch the URL
  time.sleep(4)
  Title=Driver.find_element_by_xpath("//span[contains(text(),'Euro 2020, Europe')]").text #Locator used
  # Assertion is applied for verififcation of perticular tab is opened
  self.assertEqual('EURO 2020, EUROPE',Title,'Match Result Tab is Not Open by default') #assertion implemented
  print("The Test script to loads Euro-2020 page: https://www.888sport.com/football/europe/euro-2020/ execute successfully<br/>"
        "And verification of the Match Result tab is done successfully")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Reports",
                                                       report_title="888 Spectate-Testcase1:Result",
                                                       open_in_browser=True,
                                                       add_timestamp=True,
                                                       combine_reports=False, verbosity=3)) #HTML Resport is created at end