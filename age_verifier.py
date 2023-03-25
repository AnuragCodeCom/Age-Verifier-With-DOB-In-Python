from datetime import datetime
import time


class age_verify():
    def verify_age(self,year_check , dob):
        year_check = year_check

        date_today = str(datetime.date(datetime.now()))

        year_today = int(date_today.split("-")[0])
        month_today = int(date_today.split("-")[1])
        date_today = int(date_today.split("-")[2])

        # Months With 30 Days
        month_day_30 = ["4", "6", "9", "11"]
        # Months With 31 Days
        month_day_31 = ['1', '3', '5', '7', '8', '10', '12']

        if len(dob) < 11 and len(dob) > 8:  # checking wheather the input date is correct
            year_dob = int(dob.split("-")[0])  # 2008
            month_dob = int(dob.split("-")[1])  # 2
            date_dob = int(dob.split("-")[2])  # 2
            if month_dob < 13 and month_dob > 0:
                if str(month_dob) == "2":
                    dob_leap_c = year_dob / 4
                    decimal_dob_leap = str(dob_leap_c).split(".")[1]
                    if int(decimal_dob_leap) != 0 and date_dob < 29 and date_dob > 0:
                        pass
                    elif int(decimal_dob_leap) == 0 and date_dob < 30 and date_dob > 0:
                        pass
                    else:
                        time.sleep(1)
                        return ("Error Code 802A;Invalid DOB Date")
                elif str(month_dob) in month_day_30 and date_dob < 31 and date_dob > 0:
                    pass
                elif str(month_dob) in month_day_31 and date_dob < 32 and date_dob > 0:
                    pass
                else:
                    time.sleep(1)
                    return ("Error Code 802B;Invalid DOB Date")

                if year_dob < year_today - year_check:
                    return True
                else:
                    time.sleep(1)
                    return ("Sorry User is Less Than Specified Age")
            else:
                time.sleep(1)
                return ("Error Code 801 ;Invalid DOB Month")
        else:
            time.sleep(1)
            return ("Error Code 800 ; Wrong DOB")