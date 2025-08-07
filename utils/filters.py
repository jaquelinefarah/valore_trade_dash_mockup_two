from datetime import datetime, timedelta
import pandas as pd

def get_last_closed_week(offset=0):
    """
    Retorna a última semana útil (segunda a sexta), ajustada por offset.
    offset = 0 → semana passada
    offset = -1 → 2 semanas atrás
    """
    today = datetime.today()
    days_since_monday = today.weekday()
    last_monday = today - timedelta(days=days_since_monday + 7 * (1 + abs(offset)))
    last_friday = last_monday + timedelta(days=4)
    return last_monday.date(), last_friday.date()

def filter_df_by_period(df, start_date, end_date):
    """
    Filtra um DataFrame pelo intervalo de datas.
    """
    df['date'] = pd.to_datetime(df['date'])
    return df[(df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]

def calculate_variation(current, previous):
    """
    Calcula a variação percentual entre dois valores.
    """
    if previous == 0:
        return 0
    return ((current - previous) / previous) * 100