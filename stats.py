import pandas as pd

def convert_df(df_pm25):
    df = df_pm25.copy()

    formated = (
        df
        .set_index(("datetime", ""))
        .stack(["Miejscowość", "Kod stacji"])
        .reset_index()
    )

    formated.columns = ["datetime", "Miejscowość", "Kod stacji", "PM25"]
    formated["PM25"] = (
        formated["PM25"].astype(str).str.strip()
        .str.replace(",", ".", regex=False)
    )
    formated["PM25"] = pd.to_numeric(formated["PM25"], errors="coerce")

    return formated


def calc_monthly_means(formated):
    df = formated.copy()
    

    return (
        df.groupby([
            df["datetime"].dt.year.rename("Rok"),
            df["datetime"].dt.month.rename("Miesiąc"),
            "Miejscowość",
            "Kod stacji"
        ])["PM25"].mean().reset_index(name="Mean PM25")
    )


def calc_monthly_city_means(monthly_means):
    df = monthly_means.copy()
    df["Mean PM25"] = pd.to_numeric(df["Mean PM25"], errors="coerce")

    return (
        df.groupby(["Rok", "Miesiąc", "Miejscowość"])["Mean PM25"]
        .mean()
        .reset_index()
    )


def calc_daily_means(formated):
    df = formated.copy()
    df["PM25"] = pd.to_numeric(df["PM25"], errors="coerce")

    out = (
        df.groupby([
            df["datetime"].dt.year.rename("Rok"),
            df["datetime"].dt.date.rename("Data"),
            "Miejscowość",
            "Kod stacji"
        ])["PM25"]
        .mean()
        .reset_index(name="Daily mean PM25")
    )
    return out


def count_overnorm_days(daily, threshold):
    df = daily.copy()
    over = df[df["Daily mean PM25"] > threshold]

    out = (
        over.groupby(["Rok", "Kod stacji"])["Data"]
        .nunique()
        .reset_index(name=f"Liczba dni PM25 > {threshold}")
    )
    return out


def top_bottom_stations(over_counts, year, n=3):
    df = over_counts[over_counts["Rok"] == year].copy()
    col = df.columns[-1] # licznik dni
    top = df.nlargest(n, col)
    bottom = df.nsmallest(n, col)
    out = pd.concat([top, bottom], ignore_index=True)
    return out