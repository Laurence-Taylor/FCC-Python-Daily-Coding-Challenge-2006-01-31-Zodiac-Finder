def get_sign(date_str):
    zodiac_dict = {
        "Aries" : ('03-21','04-19'),
        "Taurus" : ('04-20', '05-20')
    }

    return date_str

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