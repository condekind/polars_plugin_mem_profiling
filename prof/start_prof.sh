#!/bin/bash

gen_flamegraph() {
    memray flamegraph "$(python -c "import sys; num = int(sys.argv[2]); print(f'{sys.argv[1]}_{num:_}.bin')" "$1" "$2")"
}

for prof in "00_call_it_allocates_apply_values.py" "01_call_it_allocates_apply_to_buffer.py" "02_call_it_allocates_builder.py" "03_call_it_slices_apply_values.py" "04_call_it_slices_apply_to_buffer.py" "05_call_it_slices_builder.py"; do
   python "$prof" "$1"
   gen_flamegraph "${prof%%.py}" "$1"
done