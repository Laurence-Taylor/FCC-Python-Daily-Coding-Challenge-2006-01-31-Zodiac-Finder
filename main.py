from datetime import datetime
def get_sign(date_str):
    # declare and init a Zodiac Dictionary
    zodiac_dict = {
        "Aries" : ('03-21','04-19'),
        "Taurus" : ('04-20', '05-20'),
        "Gemini" : ('05-21','06-20'),
        "Cancer" : ('06-21', '07-22'),
        "Leo" : ('07-23','08-22'),
        "Virgo" : ('08-23', '09-22'),
        "Libra" : ('09-23','10-22'),
        "Scorpio" : ('10-23', '11-21'),
        "Sagittarius" : ('11-22','12-21'),
        "Capricorn" : ('12-22', '01-19'),
        "Aquarius" : ('01-20','02-18'),
        "Pisces" : ('02-19', '03-20')
    }
    # define the format of date
    date_format = "%Y-%m-%d"
    # convert the date to a date object
    date_obj = datetime.strptime(date_str, date_format)
    # iterate over the zodiac to determine the sign
    for key,value in zodiac_dict.items():
        # Check if the sign is in an especific range
        if datetime.strptime((date_str[:5]+value[0]), date_format) <= date_obj <= datetime.strptime((date_str[:5]+value[1]), date_format):return key
        # Check Capricorn special sign because of the change of year
        if key == 'Capricorn':
            if datetime.strptime((date_str[:5]+value[0]), date_format) <= date_obj <= datetime.strptime((str(int(date_str[:4])+1)+'-'+value[1]), date_format):return key


if __name__ == '__main__':
    print(get_sign("2026-01-31"))
    print('------')
    print(get_sign("2001-06-10"))
    print('------')
    print(get_sign("1985-09-07"))
    print('------')
    print(get_sign("2023-03-19"))
    print('------')
    print(get_sign("2045-11-05"))
    print('------')
    print(get_sign("1985-12-06"))
    print('------')
    print(get_sign("2025-12-30"))
    print('------')
    print(get_sign("2018-10-08"))
    print('------')
    print(get_sign("1958-05-04"))