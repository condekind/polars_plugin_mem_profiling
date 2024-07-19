
# Profiling

To start profiling for an existing input file with N rows (e.g., 100000), run:

```bash
bash start_prof.sh 100000
```

(This requires a csv file with a specific name to be present in `input`, see that folder's README)

The `start_prof.sh` script essentially runs a file that is prepared to track memory usage (e.g., `00_call_it_allocates_apply_values.py`), then generates its flamegraph. That is done for all compatible files in this folder.
