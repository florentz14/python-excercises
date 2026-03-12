# Program Guide (Short)

Condensed reference with top programs per folder.
Each section includes up to 8 representative scripts from `guide.md`.

Columns: Program, Algorithm Used, How it Works, Complexity.

## 05_Data_Structures

| Program | Algorithm Used | How it Works | Complexity |
| --- | --- | --- | --- |
| `05_Data_Structures/01_fractional_knapsack.py` | Greedy algorithm strategy | Builds locally optimal choices to approximate or reach global optimum | Typically O(n log n) with sorting/priority structures |
| `05_Data_Structures/02_activity_selection.py` | Sorting algorithm implementation | Orders values using comparison-based or distribution-based sorting strategy | Varies by algorithm: O(n^2), O(n log n), or O(n+k) |
| `05_Data_Structures/03_kruskal.py` | Greedy algorithm strategy | Builds locally optimal choices to approximate or reach global optimum | Typically O(n log n) with sorting/priority structures |
| `05_Data_Structures/04_huffman.py` | Greedy algorithm strategy | Builds locally optimal choices to approximate or reach global optimum | Typically O(n log n) with sorting/priority structures |
| `05_Data_Structures/05_coin_change.py` | Greedy algorithm strategy | Builds locally optimal choices to approximate or reach global optimum | Typically O(n log n) with sorting/priority structures |
| `05_Data_Structures/06_interval_scheduling.py` | Core data-structure algorithm | Weighted Interval Scheduling. Select non-overlapping intervals to maximize sum of weights. Uses dynamic programming. O(n log n) with sorting | Depends on algorithm and input size |
| `05_Data_Structures/08_rabin_karp.py` | String matching algorithm | Preprocesses pattern/text to accelerate substring search | O(n+m) KMP/Z, average O(n+m) Rabin-Karp |
| `05_Data_Structures/09_z_algorithm.py` | Search algorithm pattern | Locates target values using sequential or divide-and-conquer search | O(n) linear, O(log n) binary (sorted input) |

## 06_Statistics

| Program | Algorithm Used | How it Works | Complexity |
| --- | --- | --- | --- |
| `06_Statistics/01_mean.py` | Central tendency statistics | Computes representative center values of a dataset | O(n) time, O(1) to O(n) space depending on method |
| `06_Statistics/02_median.py` | Central tendency statistics | Computes representative center values of a dataset | O(n) time, O(1) to O(n) space depending on method |
| `06_Statistics/03_mode.py` | Central tendency statistics | Computes representative center values of a dataset | O(n) time, O(1) to O(n) space depending on method |
| `06_Statistics/04_variance.py` | Dispersion/variability analysis | Measures spread of values around central tendency | O(n) time; O(1) extra space for streaming formulas |
| `06_Statistics/05_standard_deviation.py` | Central tendency statistics | Computes representative center values of a dataset | O(n) time, O(1) to O(n) space depending on method |
| `06_Statistics/06_quartiles_percentiles.py` | Probability distribution analysis | Evaluates PMF/PDF/CDF properties or samples from distributions | O(n) for sample-based metrics; formula evaluation often O(1) |
| `06_Statistics/07_iqr.py` | Dispersion/variability analysis | Measures spread of values around central tendency | O(n) time; O(1) extra space for streaming formulas |
| `06_Statistics/08_probability_basics.py` | Probability distribution analysis | Evaluates PMF/PDF/CDF properties or samples from distributions | O(n) for sample-based metrics; formula evaluation often O(1) |

## 07_Lists_and_Tuples

| Program | Algorithm Used | How it Works | Complexity |
| --- | --- | --- | --- |
| `07_Lists_and_Tuples/list_basics/01_create_list.py` | General list/tuple operation pattern | Demonstrates Create list | Depends on operation and input size |
| `07_Lists_and_Tuples/list_basics/02_access_indices.py` | General list/tuple operation pattern | Demonstrates Access indices | Depends on operation and input size |
| `07_Lists_and_Tuples/list_basics/03_length.py` | General list/tuple operation pattern | Demonstrates Length | Depends on operation and input size |
| `07_Lists_and_Tuples/list_basics/04_slicing.py` | General list/tuple operation pattern | Demonstrates Slicing | Depends on operation and input size |
| `07_Lists_and_Tuples/list_basics/05_modify_elements.py` | General list/tuple operation pattern | Demonstrates Modify elements | Depends on operation and input size |
| `07_Lists_and_Tuples/list_basics/06_append.py` | General list/tuple operation pattern | Demonstrates Append | Depends on operation and input size |
| `07_Lists_and_Tuples/list_basics/07_insert.py` | General list/tuple operation pattern | Demonstrates Insert | Depends on operation and input size |
| `07_Lists_and_Tuples/list_basics/08_remove.py` | List/Tuple filtering workflow | Demonstrates Remove | O(n) typical pass |

## 08_Matrices

| Program | Algorithm Used | How it Works | Complexity |
| --- | --- | --- | --- |
| `08_Matrices/01_rank_original.py` | Matrix rank analysis | Uses row-reduction/SVD-based rank computation and interpretation | O(min(m,n)*m*n) typical dense |
| `08_Matrices/02_rank_optimized.py` | Matrix rank analysis | Uses row-reduction/SVD-based rank computation and interpretation | O(min(m,n)*m*n) typical dense |
| `08_Matrices/03_rank_full_analysis.py` | Matrix invariants computation | Computes trace/determinant and identity properties | Trace O(n), determinant typically O(n^3) |
| `08_Matrices/04_rank_compare_methods.py` | Matrix rank analysis | Uses row-reduction/SVD-based rank computation and interpretation | O(min(m,n)*m*n) typical dense |
| `08_Matrices/05_rank_example_types.py` | Matrix rank analysis | Uses row-reduction/SVD-based rank computation and interpretation | O(min(m,n)*m*n) typical dense |
| `08_Matrices/06_rank_properties.py` | Matrix rank analysis | Uses row-reduction/SVD-based rank computation and interpretation | O(min(m,n)*m*n) typical dense |
| `08_Matrices/07_rank_interactive.py` | Matrix rank analysis | Uses row-reduction/SVD-based rank computation and interpretation | O(min(m,n)*m*n) typical dense |
| `08_Matrices/08_rank_summary.py` | Matrix rank analysis | Uses row-reduction/SVD-based rank computation and interpretation | O(min(m,n)*m*n) typical dense |

## 09_Pandas

| Program | Algorithm Used | How it Works | Complexity |
| --- | --- | --- | --- |
| `09_Pandas/01_basics/01_create_dataframe.py` | Tabular I/O processing | Reads/writes tabular files and infers/assigns schema | O(n) by number of records |
| `09_Pandas/01_basics/04_read_csv.py` | Tabular I/O processing | Reads/writes tabular files and infers/assigns schema | O(n) by number of records |
| `09_Pandas/01_basics/06_explore.py` | Descriptive statistics analysis | Computes summary statistics and distribution-oriented metrics | O(n) for simple stats; O(n*d) for multi-column summaries |
| `09_Pandas/01_basics/07_columns.py` | DataFrame/Series construction | Creates tabular structures and performs column/index operations | O(n) |
| `09_Pandas/01_basics/09_nulls.py` | Data cleaning pipeline | Detects and handles nulls/duplicates/outliers and standardizes values | O(n) typical per cleaning pass |
| `09_Pandas/01_basics/10_merge_concat.py` | DataFrame join/merge workflow | Combines datasets by key alignment and join strategy | Typically O(n+m) to O((n+m) log(n+m)) |
| `09_Pandas/01_basics/11_drop.py` | Data cleaning pipeline | Detects and handles nulls/duplicates/outliers and standardizes values | O(n) typical per cleaning pass |
| `09_Pandas/01_basics/12_statistics.py` | Descriptive statistics analysis | Computes summary statistics and distribution-oriented metrics | O(n) for simple stats; O(n*d) for multi-column summaries |

## 10_Matplotlib

| Program | Algorithm Used | How it Works | Complexity |
| --- | --- | --- | --- |
| `10_Matplotlib/01_pyplot_basic_plot.py` | Multi-plot composition workflow | Combines several charts in one figure with coordinated axes/layout | O(n) data prep + rendering per subplot |
| `10_Matplotlib/02_pyplot_multiple_lines.py` | Multi-plot composition workflow | Combines several charts in one figure with coordinated axes/layout | O(n) data prep + rendering per subplot |
| `10_Matplotlib/03_pyplot_save_figure.py` | Matplotlib plotting workflow | Saving a figure to file demo | O(n) by number of plotted elements |
| `10_Matplotlib/04_pyplot_oop_style.py` | Chart styling and annotation | Configures labels, legends, markers, colors, and axis formatting | O(n) with low constant overhead |
| `10_Matplotlib/05_plotting_two_points.py` | Line plotting workflow | Maps ordered x-y series into continuous lines for trend analysis | O(n) by plotted points |
| `10_Matplotlib/06_plotting_markers_only.py` | Line plotting workflow | Maps ordered x-y series into continuous lines for trend analysis | O(n) by plotted points |
| `10_Matplotlib/07_plotting_multiple_styles.py` | Multi-plot composition workflow | Combines several charts in one figure with coordinated axes/layout | O(n) data prep + rendering per subplot |
| `10_Matplotlib/08_plotting_keyword_args.py` | Line plotting workflow | Maps ordered x-y series into continuous lines for trend analysis | O(n) by plotted points |

## 11_OOP

| Program | Algorithm Used | How it Works | Complexity |
| --- | --- | --- | --- |
| `11_OOP/01_basic_class.py` | Core object-oriented programming pattern | Creating a basic class in Python | Mostly O(1) per method call; can be O(n) with collections |
| `11_OOP/02_init_constructor.py` | Core object-oriented programming pattern | Understanding the __init__ constructor method | Mostly O(1) per method call; can be O(n) with collections |
| `11_OOP/03_attributes_methods.py` | Core object-oriented programming pattern | Class attributes vs instance attributes | Mostly O(1) per method call; can be O(n) with collections |
| `11_OOP/04_str_repr.py` | Python data model customization | Implements dunder methods to integrate with Python protocols | O(1) to O(n) depending on represented data |
| `11_OOP/05_private_attributes.py` | Encapsulation and controlled access | Protects internal state via methods/properties and validation | O(1) typical accessor/mutator |
| `11_OOP/06_getters_setters.py` | Encapsulation and controlled access | Protects internal state via methods/properties and validation | O(1) typical accessor/mutator |
| `11_OOP/07_property_decorator.py` | Encapsulation and controlled access | Protects internal state via methods/properties and validation | O(1) typical accessor/mutator |
| `11_OOP/08_inheritance_basic.py` | Inheritance-based OOP design | Defines parent-child classes to reuse and extend behavior | Method dispatch O(1); overall depends on method internals |

## 14_Trees

| Program | Algorithm Used | How it Works | Complexity |
| --- | --- | --- | --- |
| `14_Trees/01_node.py` | Core tree algorithm pattern | Binary tree node class with value, left, and right children | Typically O(n) traversal or O(h) search/update |
| `14_Trees/02_traversal.py` | Tree traversal algorithm | Visits nodes in a specific DFS/BFS order to process tree structure | O(n) time, O(h) recursion/stack (or O(w) queue) |
| `14_Trees/03_height.py` | Tree property computation | Computes structural metrics such as height/depth/balance | O(n) time, O(h) space |
| `14_Trees/04_basic_binary.py` | Binary Search Tree operation | Uses BST ordering property for locate/insert/delete | O(h) time, O(h) space recursion |
| `14_Trees/05_traversals.py` | Tree traversal algorithm | Visits nodes in a specific DFS/BFS order to process tree structure | O(n) time, O(h) recursion/stack (or O(w) queue) |
| `14_Trees/06_bst.py` | Binary Search Tree operation | Uses BST ordering property for locate/insert/delete | O(h) time, O(h) space recursion |
| `14_Trees/07_avl.py` | Binary Search Tree operation | Uses BST ordering property for locate/insert/delete | O(h) time, O(h) space recursion |
| `14_Trees/08_nary.py` | Level-order traversal (BFS) | Processes nodes level by level using a queue | O(n) time, O(w) space |

## 15_Graphs

| Program | Algorithm Used | How it Works | Complexity |
| --- | --- | --- | --- |
| `15_Graphs/01_adjacency_list.py` | Graph representation workflow | Builds graph structures as adjacency list/matrix for algorithms | O(V + E) storage for list, O(V^2) for matrix |
| `15_Graphs/02_class.py` | Graph representation workflow | Builds graph structures as adjacency list/matrix for algorithms | O(V + E) storage for list, O(V^2) for matrix |
| `15_Graphs/03_bfs.py` | Breadth-First Search (BFS) | Explores graph by frontier layers from source nodes | O(V + E) time, O(V) space |
| `15_Graphs/04_dfs.py` | Depth-First Search (DFS) | Explores graph deeply using recursion or explicit stack | O(V + E) time, O(V) space |
| `15_Graphs/05_adjacency_list.py` | Breadth-First Search (BFS) | Explores graph by frontier layers from source nodes | O(V + E) time, O(V) space |
| `15_Graphs/06_adjacency_matrix.py` | Graph representation workflow | Builds graph structures as adjacency list/matrix for algorithms | O(V + E) storage for list, O(V^2) for matrix |
| `15_Graphs/07_path_search.py` | Breadth-First Search (BFS) | Explores graph by frontier layers from source nodes | O(V + E) time, O(V) space |
| `15_Graphs/08_dijkstra.py` | Dijkstra shortest path | Uses priority queue to expand minimum-distance vertex next | O((V+E) log V) with heap |

## 16_Files

| Program | Algorithm Used | How it Works | Complexity |
| --- | --- | --- | --- |
| `16_Files/01_write.py` | File I/O processing workflow | Reads/writes structured or plain text data with proper file modes and encoding | O(n) by file size processed |
| `16_Files/02_read.py` | File I/O processing workflow | Reads/writes structured or plain text data with proper file modes and encoding | O(n) by file size processed |
| `16_Files/03_append.py` | File I/O processing workflow | Reads/writes structured or plain text data with proper file modes and encoding | O(n) by file size processed |
| `16_Files/04_read_lines.py` | File I/O processing workflow | Reads/writes structured or plain text data with proper file modes and encoding | O(n) by file size processed |
| `16_Files/05_exists.py` | Filesystem traversal and management | Inspects and manipulates filesystem paths, metadata, and directory trees | O(k) by number of files/paths visited |
| `16_Files/06_list_directory.py` | Filesystem traversal and management | Inspects and manipulates filesystem paths, metadata, and directory trees | O(k) by number of files/paths visited |
| `16_Files/07_delete.py` | Filesystem traversal and management | Inspects and manipulates filesystem paths, metadata, and directory trees | O(k) by number of files/paths visited |
| `16_Files/08_copy_move.py` | Filesystem traversal and management | Inspects and manipulates filesystem paths, metadata, and directory trees | O(k) by number of files/paths visited |

## 17_Equations

| Program | Algorithm Used | How it Works | Complexity |
| --- | --- | --- | --- |
| `17_Equations/01_original.py` | Linear system numerical solver | Solves Ax=b by elimination or iterative linear algebra techniques | Direct methods typically O(n^3); iterative methods O(k*n^2) |
| `17_Equations/02_improved.py` | Linear system numerical solver | Solves Ax=b by elimination or iterative linear algebra techniques | Direct methods typically O(n^3); iterative methods O(k*n^2) |
| `17_Equations/03_multiple_systems.py` | Linear system numerical solver | Solves Ax=b by elimination or iterative linear algebra techniques | Direct methods typically O(n^3); iterative methods O(k*n^2) |
| `17_Equations/04_fractions.py` | Linear system numerical solver | Solves Ax=b by elimination or iterative linear algebra techniques | Direct methods typically O(n^3); iterative methods O(k*n^2) |
| `17_Equations/05_complete_analysis.py` | Linear system numerical solver | Solves Ax=b by elimination or iterative linear algebra techniques | Direct methods typically O(n^3); iterative methods O(k*n^2) |
| `17_Equations/06_systems_examples.py` | Ordinary differential equation solver | Advances state through time using numerical integration steps | O(s) by number of integration steps |
| `17_Equations/07_compare_methods.py` | Linear system numerical solver | Solves Ax=b by elimination or iterative linear algebra techniques | Direct methods typically O(n^3); iterative methods O(k*n^2) |
| `17_Equations/08_summary.py` | Linear system numerical solver | Solves Ax=b by elimination or iterative linear algebra techniques | Direct methods typically O(n^3); iterative methods O(k*n^2) |

## 19_Hash_Tables

| Program | Algorithm Used | How it Works | Complexity |
| --- | --- | --- | --- |
| `19_Hash_Tables/01_hash_table_chaining.py` | Hash table with separate chaining | Stores colliding keys in per-bucket linked/list chains | Average O(1) insert/find/delete; worst O(n) |
| `19_Hash_Tables/02_hash_table_open_addressing.py` | Open addressing hash table | Resolves collisions by probing alternative slots in-table | Average O(1), worst O(n); depends on load factor |
| `19_Hash_Tables/03_hash_functions.py` | Hash function design | Maps keys to indices aiming for uniform distribution | O(len(key)) to compute hash, lookup average O(1) |
| `19_Hash_Tables/04_hash_table_applications.py` | Hash-map application pattern | Uses key-value mapping for counting, caching, or fast membership | Average O(1) update/query per operation |
| `19_Hash_Tables/05_quadratic_probing.py` | Open addressing hash table | Resolves collisions by probing alternative slots in-table | Average O(1), worst O(n); depends on load factor |
| `19_Hash_Tables/06_double_hashing.py` | Open addressing hash table | Resolves collisions by probing alternative slots in-table | Average O(1), worst O(n); depends on load factor |
| `19_Hash_Tables/07_dynamic_resizing.py` | Hash table resizing strategy | Expands and re-inserts entries when load exceeds threshold | Rehash O(n), amortized O(1) inserts |
| `19_Hash_Tables/08_load_factor_analysis.py` | Hash table resizing strategy | Expands and re-inserts entries when load exceeds threshold | Rehash O(n), amortized O(1) inserts |

## 21_Machine_Learning

| Program | Algorithm Used | How it Works | Complexity |
| --- | --- | --- | --- |
| `21_Machine_Learning/01_getting_started.py` | Machine learning workflow | ML intro: concepts, types, required libraries | Depends on algorithm, features, and dataset size |
| `21_Machine_Learning/02_mean_median_mode.py` | Machine learning workflow | Fundamental statistics: mean, median, mode | Depends on algorithm, features, and dataset size |
| `21_Machine_Learning/03_standard_deviation.py` | Machine learning workflow | Standard deviation and variance for data spread | Depends on algorithm, features, and dataset size |
| `21_Machine_Learning/04_percentile.py` | Machine learning workflow | Percentiles and quartiles for distribution analysis | Depends on algorithm, features, and dataset size |
| `21_Machine_Learning/05_data_distribution.py` | Machine learning workflow | Data distribution types and histograms | Depends on algorithm, features, and dataset size |
| `21_Machine_Learning/06_normal_data_distribution.py` | Machine learning workflow | Normal (Gaussian) distribution in ML | Depends on algorithm, features, and dataset size |
| `21_Machine_Learning/07_scatter_plot.py` | Machine learning workflow | Scatter plots for visualizing variable relationships | Depends on algorithm, features, and dataset size |
| `21_Machine_Learning/08_linear_regression.py` | Supervised learning model training | Fits labeled examples to learn prediction mapping | Varies by model (e.g., linear ~O(n*p^2), trees ~O(n*p*log n)) |

---

Generated from `guide.md` with top 8 rows per folder.
