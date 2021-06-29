import time
import unittest
from selenium import webdriver
from Common_Code import Driver,Path,LaunchURL
from fractions import Fraction
import HtmlTestRunner

#Verify that 'Ireland' is not listed in tomorrow's matches.

class Testcase3(unittest.TestCase):

 def test_Testcase3(self):
  Driver=LaunchURL()
  time.sleep(5)
  L=Driver.find_elements_by_xpath("//div[@class='sport-event media-cells preplay-event-selections ']/a/div/div")
  count=0
  print ("Below are the List of country present on screen:<br/>")
  for i in L:
   count=count+1
   #Ireland Name is verified from the Tommorows list'
   try:
    print(i.text,'<br/>')
    self.assertIsNot('Ireland', i.text, 'In Tommorow List ireland is present')
    if (count>=6):
     break
   except E:
    print ("The Exception in the given program is: ", E)
  print ("<br/>Ireland is not in given above list: ")

if __name__ == "__main__":
 unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Reports",
                                                        report_title="888 Spectate-Testcase3:Result",
                                                        open_in_browser=True,
                                                        add_timestamp=True,
                                                        combine_reports=False,
                                                        verbosity=3))  # HTML Resport is created at end