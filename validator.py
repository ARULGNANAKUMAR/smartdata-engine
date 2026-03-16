def validate_dataframe(df):
    warnings = []
    if df.isnull().sum().sum() > 0:
        warnings.append("Null values detected")
    if df.duplicated().sum() > 0:
        warnings.append(f"Found {df.duplicated().sum()} duplicate rows")
    return warnings
