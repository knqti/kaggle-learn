import pandas
from pathlib import Path

def export_parquet(dataframe, filename:str):
    export_to = Path(__file__).parents[1] / 'parquet_files' / filename
    dataframe.to_parquet(export_to)
    print(f'Exported to: {export_to}')

def import_parquet(filename:str):
    import_from = Path(__file__).parents[1] / 'parquet_files' / filename
    dataframe = pandas.read_parquet(import_from)
    print('Dataframe imported.')
    return dataframe