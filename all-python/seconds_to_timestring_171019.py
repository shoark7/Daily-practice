"""Change seconds to a time string.

    For an another issue, I had to make a function which changes integers of seconds to a time
    delta string.

    Start Date: 2017/10/19
    End  Date : 2017/10/19
"""

TIME_UNIT = {'korean': ['시간', '분', '초'], 'english': [' hour', ' minute', ' second']}


def seconds_2_time(time, precision=4, locale='english'):
    """Change seconds to time delta string.

    time should be a real number value gte 0.
    Seconds can be a fraction value so precision for rounding can be added.
    locale can be set for a time unit you want.
    Units of plural number have suffix 's' at the end of themselves.

    :input:
        time: A real number value gte 0.
        preicision: An integer for precision of time string. Default: 4
        locale: locale for time string format.
                'korean' and 'english' is supported. Default: 'english'.

    :return:
        A string of time delta. Hour, minute and second are shown.
    """
    if time < 0:
        raise ValueError("Time should be a real number over 0")

    if locale not in TIME_UNIT.keys():
        raise ValueError("locale should be either 'korean' or 'english'")

    hour_seconds, minute_seconds = 3600, 60
    hour, rest = divmod(time, hour_seconds)
    minute, second = divmod(rest, minute_seconds)
    second = round(second, precision)
    hour, minute = int(hour), int(minute)

    hour_unit, minute_unit, second_unit = TIME_UNIT[locale]

    result_string = ''

    if hour:
        result_string += str(hour) + hour_unit + ('s  ' if hour > 1 and locale == 'english' else '  ')
    if minute:
        result_string += str(minute) + minute_unit + ('s  ' if minute > 1 and locale == 'english' else '  ')
    if second:
        result_string += str(second) + second_unit + ('s  ' if second > 1 and locale == 'english' else '  ')

    return result_string


if __name__ == '__main__':
    print('3600', seconds_2_time(3600))
    print('60', seconds_2_time(60))
    print('3660', seconds_2_time(3660))
    print('5', seconds_2_time(5))
    print('1231244', seconds_2_time(1231244.123123, locale='korean'))
    print('1231244', seconds_2_time(1231244.123123, precision=-3))
    print('1231244', seconds_2_time(1231244.123123, locale='chinese'))
