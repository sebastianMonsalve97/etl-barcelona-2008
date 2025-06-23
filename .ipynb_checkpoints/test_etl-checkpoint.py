import pandas as pd
from etl import extract_match_data, transform_data

def test_extract_returns_dataframe():
    df = extract_match_data()
    assert isinstance(df, pd.DataFrame), "❌ La extracción no devolvió un DataFrame"

def test_transform_filters_data():
    df = extract_match_data()
    df_transformed = transform_data(df)
    assert not df_transformed.empty, "❌ El dataframe transformado está vacío"
    assert "Barcelona" in df_transformed['home_team_name'].values or \
           "Barcelona" in df_transformed['away_team_name'].values, \
           "❌ No hay datos del Barcelona"
