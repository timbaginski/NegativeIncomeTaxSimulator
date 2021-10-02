import pandas as pd

NUM_WORKERS = 161450000
NUM_ADULTS_US = 258300000
NUM_RETIRED_ADULTS = 46330000


# returns the percent of workers at a given income level
def percent_at_income(df: pd.DataFrame, income: float) -> float:
    incomes = df["2021"]
    percentiles = df["PERCENTILE"]
    h = incomes.searchsorted(income, "right")
    l = h - 1
    return (percentiles[l] + (percentiles[h] - percentiles[l]) *
            (income - incomes[l]) / (incomes[h] - incomes[l])) / 100


# Given an income and a threshold, calculate amount somebody with that income saves from new taxes
def taxes_saved(threshold: float, income: int, tax_rates: pd.DataFrame) -> float:
    temp = min(threshold, income)
    taxes = 0.0
    for index, value in tax_rates["BRACKET"].items():
        if temp <= 0:
            break
        taxes += min(temp, value) * (tax_rates["RATE"][index] / 100)
        temp -= value

    return taxes


# returns the total cost of a NIT program given a threshold and percent
# In addition to all workers, includes non-working non-retired adults
def payment_cost(threshold: float, percent: float, df: pd.DataFrame, tax_rates: pd.DataFrame) -> float:
    res, prev_percent = 0.0, 0.0
    for i in range(0, int(threshold), 100):
        curr = percent_at_income(df, i)
        tax_savings = taxes_saved(threshold, i, tax_rates) * (curr - prev_percent) * NUM_WORKERS
        res += (curr - prev_percent) * NUM_WORKERS * ((threshold - i) * percent) + tax_savings
        prev_percent = curr

    return (res + ((NUM_ADULTS_US - NUM_WORKERS - NUM_RETIRED_ADULTS) *
                   (threshold * percent)))


def main():
    income_percentiles = pd.read_csv('data.csv')
    tax_rates = pd.read_csv("tax_rates.csv")
    threshold = float(input("What threshold do you want the NIT to apply to?"))
    percent = float((input("What percent of the threshold minus income should the NIT give?")))
    cost = round(payment_cost(threshold, percent / 100, income_percentiles, tax_rates), 2)

    print("A NIT guaranteeing " + str(percent) + "% of a threshold of $" +
          str(threshold) + " would cost: $" + f'{cost:,}')


main()
