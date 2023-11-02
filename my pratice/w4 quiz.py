import os
import toolkit_config as cfg
import yf_example2


def qan_prc_to_csv(year):
    """
    Download Qantas stock prices for a given year into a CSV file.

    Parameters:
        year (int): The year for which stock prices need to be downloaded.

    Returns:
        None. The function saves the data to a CSV file in the 'data' folder.
    """
    # Variables date
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"

    # Download the data
    df = yf_example2.yf_prc_to_csv(ticker='QAN.AX', start_date=start_date, end_date=end_date)
    filename = f"qan_prc_{year}.csv"

    # Create a path
    path = os.path.join(cfg.DATA_PATH, filename)

    df.to_csv(path)


if __name__ == "__main__":
    # Test case
    qan_prc_to_csv(year=2020)