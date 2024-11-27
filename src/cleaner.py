class DataCleaner:
    @staticmethod
    def clean_column_names(df):
        return df.columns.str.strip().str.lower().str.replace(' ', '_')

    @staticmethod
    def clean_value_column(df):
        df['valor'] = df['valor'].str.replace(r'[^\d,.-]', '', regex=True).str.replace(',', '.').astype(float)
        return df
