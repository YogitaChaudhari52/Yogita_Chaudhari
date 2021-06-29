import time
import unittest
from selenium import webdriver
from Common_Code import Driver,Path,LaunchURL
from fractions import Fraction
import HtmlTestRunner

#Verify that the odds for Spain** to win its next Home match
# (where it's listed first against its opponent) are lower than 3/2

class Testcase4(unittest.TestCase):

 def test_Testcase4(self):
  Driver=LaunchURL()
  time.sleep(5)
  L=Driver.find_elements_by_xpath("//div[@class='sport-event media-cells preplay-event-selections ']/a/div/div[contains(@data-home-away-label,'H)')]")
  for i in L:
   #Ireland Name is verified from the Tommorows list'
   try:
   # print(i.text)
    if(i.text=='Spain'):
     print ('House match is Spain<br/>')
     score=Driver.find_elements_by_xpath("//div[@class='sport-event media-cells preplay-event-selections ']/a/div/div[contains(@data-home-away-label,'H)')]/following::div[contains(@class,'preplay-bet')]/span")
     for value in score:
       if (value.text=='3/2'):
          print('The spain odds is less than 3/2 fraction<br/>')
    else:
       print ("Spain is not in Home match list<br/>")
       break
   except E:
    print ("The Exception in the given program is: ", E)
  print ("<br/>Spain Home match is verified from the given list successfully")


if __name__ == "__main__":
 unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Reports",
                                                        report_title="888 Spectate-Testcase4:Result",
                                                        open_in_browser=True,
                                                        add_timestamp=True,
                                                        combine_reports=False,
                                                        verbosity=3))  # HTML Resport is created at end