import sys
import polars as pl
from mem_profiling import it_allocates_apply_values
import memray


def call_it_allocates_apply_values(df: pl.DataFrame) -> pl.DataFrame:
    print("\n------------------------------------------------------------")
    print("it_allocates_apply_values\n")
    df = df.with_columns(fields=it_allocates_apply_values("URLs"))
    print("done")
    return df


if __name__ == "__main__":
    num_rows = 100
    if len(sys.argv) > 1:
        num_rows = int(sys.argv[1])

    df = pl.read_csv(f"input/urls_{num_rows:_}.csv")

    with memray.Tracker(
        f"00_call_it_allocates_apply_values_{num_rows:_}.bin",
        native_traces=True,
    ):
        df = call_it_allocates_apply_values(df)

    print(df)
