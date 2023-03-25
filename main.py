from datetime import datetime
# -----------IMPORTING THE CODE---------------------
from age_verifier import age_verify

#--------------------------CODE BY-------------------------------------
#   AnuragCodeCom
#   Website: https://anuragcode.com/
#   GitHub: https://github.anuragcode.com/
#   Instagram: https://insta.anuragcode.com/
#   Discord: https://discord.anuragcode.com/
#----------------------------------------------------------------------


#   This Module Only Calculates On The Basis Of Year
#   But it Still Verifies Wheather The Input Of Month And Date Is Correct Or Not
#   It Also Checks Specially For Leap Year And Verifies 29FEB As Correct only in leap years


#**********************************************
# Replace Here with The Age year You Want To Verify The DOB With
year_check = 17
#**********************************************

#**********************************************
# Taking User Dob As Input Format: YYYY-MM-DD
dob = input("Enter Your DOB [YYYY-MM-DD]: ")


#-----------------Creating A User To Use The Module On-----------------------
user = age_verify()
#------------Running The Module On The Created User--------------
user.verify_age(year_check + 1, dob )