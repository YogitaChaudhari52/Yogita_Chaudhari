import time
import unittest
from selenium import webdriver
from Common_Code import Driver,Path,LaunchURL
from fractions import Fraction
import HtmlTestRunner

#Verify that all 3 odds (Home win '1', Draw 'X', Away win '2') for
#the first match listed are all in the fractional format N/N, where Ns are numbers*

class Testcase2(unittest.TestCase):

 def test_Testcase2(self):
  Driver=LaunchURL() #Launch URL
  time.sleep(5)
  L=Driver.find_elements_by_xpath("//span[@class='bb-sport-event__selection']") #Locator find
  for i in L:
   #Fraction Number divided by '/'
   try:
    print(i.text)
    F=str(i.text).split("/") #Text is divided using '/'
    print ("Number is in fraction format<br/>")
   except:
    print ("Number is not in fraction format<br/>")


if __name__ == "__main__":
 unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Reports",
                                                        report_title="888 Spectate-Testcase2:Result",
                                                        open_in_browser=True,
                                                        add_timestamp=True,
                                                        combine_reports=False,
                                                        verbosity=3))  # HTML Resport is created at end