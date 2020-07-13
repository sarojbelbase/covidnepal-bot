import arrow


def padding(any_num):
    if int(any_num) < 10:
        return '0' + str(any_num)
    else:
        return f"{int(any_num):,}"


def humanize_date(any_date):
    return arrow.get(any_date).to('US/Pacific').humanize()


def humanize_local_date(any_local_date):
    return arrow.get(any_local_date).shift(minutes=-345).to('US/Pacific').humanize()
