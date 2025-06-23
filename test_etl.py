import pandas as pd
from etl import extract_match_data, transform_data

def test_extract_returns_dataframe():
    df = extract_match_data()
    assert isinstance(df, pd.DataFrame), "❌ La extracción no devolvió un DataFrame"
    print("✅ test_extract_returns_dataframe pasó")

def test_transform_filters_data():
    df = extract_match_data()
    print("Registros extraídos:", len(df))
    df_transformed = transform_data(df)
    print("Registros transformados:", len(df_transformed))
    assert not df_transformed.empty, "❌ El dataframe transformado está vacío"
    assert df_transformed['home_team_name'].str.contains("Barcelona").any() or \
           df_transformed['away_team_name'].str.contains("Barcelona").any(), \
           "❌ No hay datos del Barcelona"
    print("✅ test_transform_filters_data pasó")

# Ejecutar los tests
test_extract_returns_dataframe()
test_transform_filters_data()



