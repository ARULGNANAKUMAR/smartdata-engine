import pandas as pd
import numpy as np
import logging
import time
import psutil
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - althenaxavier - %(levelname)s - %(message)s"
)

class AlthenaXavierEngine:
    def __init__(self, chunk_size=None):
        self.chunk_size = chunk_size or self._adaptive_chunk()

    def _adaptive_chunk(self):
        ram = psutil.virtual_memory().available / (1024 ** 2)
        if ram > 8000:
            return 500000
        elif ram > 2000:
            return 100000
        return 10000

    def _validate_column(self, df, column):
        if column not in df.columns:
            raise ValueError(f"Column '{column}' not found. Available: {list(df.columns)}")

    def process(self, file, operation="sum", column=None):
        start_time = time.time()
        total_rows = 0
        result = None

        logging.info(f"Starting engine: {operation} on '{file}' (chunk={self.chunk_size})")

        for chunk in tqdm(pd.read_csv(file, chunksize=self.chunk_size), desc="Processing"):
            self._validate_column(chunk, column)
            series = chunk[column]

            if operation == "sum":
                value = series.sum()
                result = (result or 0) + value

            elif operation == "mean":
                value = series.mean()
                result = value if result is None else (result + value) / 2

            elif operation == "min":
                value = series.min()
                result = value if result is None else min(result, value)

            elif operation == "max":
                value = series.max()
                result = value if result is None else max(result, value)

            elif operation == "count":
                result = {
                    "total": len(series),
                    "non_null": series.count(),
                    "null": series.isnull().sum(),
                    "non_null_percentage": series.count() / len(series)
                }

            total_rows += len(chunk)

        elapsed = time.time() - start_time
        logging.info(f"Completed: {total_rows} rows in {elapsed:.2f}s")

        return result


if __name__ == "__main__":
    print("AlthenaXavier Engine v1.0.0")
