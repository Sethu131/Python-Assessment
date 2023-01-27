from datetime import date, timedelta


def compute_prev_date(dates_list: list):
    """
    function will take a list of dates in this format: YYYY-MM-DD
    and for each date returns previous date in the format DD xxx YYYY
    where the xxx is the month as locale's abbreviation
    """

    return [
        (date.fromisoformat(date_str) - timedelta(days=1)).strftime("%d %b %y")
        for date_str in dates_list
    ]


list_of_dates = ["2022-11-01", "2022-11-02"]
previous_date = compute_prev_date(list_of_dates)
print(previous_date)
