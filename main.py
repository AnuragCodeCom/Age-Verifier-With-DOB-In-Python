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


#   This Module Only Calculates On The Basis Of Year So Check Year Is Reccommended To be 1 Year Less Than Desired For Accurate Output
#   But it Still Verifies Wheather The Input Of Month And Date Is Correct Or Not
#   It Also Checks Specially For Leap Year And Verifies 29FEB As Correct only in leap years


#**********************************************
# Replace Here with The Age year You Want To Verify The DOB With
# IMPORTANT: This Module Mainly Uses DOB year To Verify User's Age So Its Reccommended To Put Year Of Checking To be 1 Less Than Desired
# But Still it Check the Month And Date Wheather its Correct
year_check = 18
#**********************************************

#**********************************************
# Taking User Dob As Input Format: YYYY-MM-DD
dob = input("Enter Your DOB [YYYY-MM-DD]: ")


#-----------------Creating A User To Use The Module On-----------------------
user = age_verify()
#------------Running The Module On The Created User And Taking its Output In A Variable--------------
output = user.verify_age(year_check, dob)

#---------------Checking The Output------------

if output == True:
    print("User Is Above The Age Of",year_check)
