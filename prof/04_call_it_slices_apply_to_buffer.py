import sys
import polars as pl
from mem_profiling import it_slices_apply_to_buffer
import memray


def call_it_slices_apply_to_buffer(df: pl.DataFrame) -> pl.DataFrame:
    print("\n------------------------------------------------------------")
    print("it_slices_apply_to_buffer\n")
    df = df.with_columns(fields=it_slices_apply_to_buffer("URLs"))
    print("done")
    return df


if __name__ == "__main__":
    num_rows = 100
    if len(sys.argv) > 1:
        num_rows = int(sys.argv[1])

    df = pl.read_csv(f"input/urls_{num_rows:_}.csv")

    with memray.Tracker(
        f"04_call_it_slices_apply_to_buffer_{num_rows:_}.bin",
        native_traces=True,
    ):
        df = call_it_slices_apply_to_buffer(df)

    print(df)
