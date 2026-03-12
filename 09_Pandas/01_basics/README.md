# 01_basics - Pandas Fundamentals

Core Pandas practice folder with progressive exercises focused on DataFrame/Series basics.

## Overview

- Total scripts: `74` (`01` to `74`)
- Goal: build fluency with the most common Pandas operations before moving to advanced modules
- Typical topics: creation, indexing, selection, null handling, sorting, type conversion, merge/concat, simple feature engineering

## Learning Blocks

### 1) DataFrame and Series creation

- Create DataFrames from dictionaries, lists, NumPy arrays
- Build Series from lists, dicts, and arrays
- Configure index labels and basic structure

Examples:
- `01_create_dataframe.py`
- `02_create_from_dict.py`
- `21_series_from_list.py`
- `23_series_from_numpy.py`
- `24_series_from_dictionary.py`

### 2) Inspection and basic manipulation

- Explore data with `head`, `tail`, `info`, `describe`
- Select/reorder columns and rows
- Add/remove rows and columns

Examples:
- `04_read_csv.py`
- `05_basic_summary.py`
- `06_explore.py`
- `07_columns.py`
- `11_drop.py`

### 3) Nulls, dtypes, and cleaning basics

- Detect/fill/remove nulls
- Convert data safely with `astype` and `to_numeric`
- Rename columns and adjust display

Examples:
- `09_nulls.py`
- `17_astype_and_conversion.py`
- `19_to_numeric.py`
- `38_rename_columns.py`
- `49_widen_output_display.py`

### 4) Index, sorting, and structure operations

- Work with index reset/set and index-to-column transforms
- Sort by one or multiple columns
- Change column order and insert columns

Examples:
- `14_index_operations.py`
- `25_sort_multiple_columns.py`
- `40_change_column_order.py`
- `51_convert_index_to_column.py`
- `62_sort_by_multiple_columns.py`

### 5) Merge, concat, mapping, and advanced basics

- Combine DataFrames with `merge`, `concat`, and `join`
- Map and replace values
- Basic binning, outlier handling, and grouped transforms

Examples:
- `10_merge_concat.py`
- `43_merge_join_basics.py`
- `44_concat_pivot_basics.py`
- `46_mapping_replace_basics.py`
- `48_strings_and_advanced_groupby.py`
- `50_merging_and_joining_in_depth.py`

## How to run

From repository root:

```bash
python 09_Pandas/01_basics/01_create_dataframe.py
```

Or from inside `09_Pandas`:

```bash
python 01_basics/01_create_dataframe.py
```

## Data location

Most scripts read data from:

- `09_Pandas/data`

with paths built using `pathlib.Path` for portability.
