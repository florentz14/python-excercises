# 08_Matrices

Vector, matrix, and NumPy operations. Linear algebra, scientific computing, and interview practice.

---

## Matrix Rank (01-08, 03a-03e, 04a-04d)

| File | Content |
|------|---------|
| `01_rank_original.py` | Original rank computation |
| `02_rank_optimized.py` | Optimized with extra info |
| `03a_rank_compute.py` | Rank with `matrix_rank` |
| `03b_max_possible_rank.py` | Max rank `min(m, n)` |
| `03c_full_rank_vs_deficient.py` | Full rank vs rank deficient |
| `03d_determinant_singular.py` | Determinant, singular (square) |
| `03e_fundamental_subspaces.py` | Column, row, null space dimensions |
| `04a_rank_matrix_rank.py` | `np.linalg.matrix_rank` |
| `04b_rank_svd.py` | Rank via SVD and tolerance |
| `04c_rank_qr.py` | Rank via QR diagonal of R |
| `04d_rank_methods_agreement.py` | Compare three methods |
| `05_rank_example_types.py` | Example types |
| `06_rank_properties.py` | Properties |
| `07_rank_interactive.py` | Interactive version |
| `08_rank_summary.py` | Summary |

---

## Basic Matrices (09-40)

| File | Content |
|------|---------|
| `09_create_display.py` | Create and display |
| `10_add.py` | Add matrices |
| `11_scalar_product.py` | Scalar product |
| `12_transpose.py` | Transpose |
| `13_multiply.py` | Multiplication |
| `14_vector_product.py` | Matrix × vector |
| `15_create_access_modify.py` | Create, access, modify |
| `16_zeros_identity.py` | Zeros and identity |
| `17a_matrix_transpose.py` | Transpose (list comprehensions) |
| `17b_matrix_add.py` | Matrix addition |
| `17c_scalar_matrix_multiply.py` | Scalar times matrix |
| `18_row_column_sum_maxmin.py` | Row, column, sum, max/min |
| `19_grid_types_square.py` | Grid, types, square |
| `20_rotate_diagonal_traverse.py` | Rotate, diagonal, traverse |
| `21_comprehension_practical.py` | Comprehension, practical |
| `22_add_subtract_scalar.py` | Add, subtract, scalar |
| `23_hadamard_product.py` | Hadamard product |
| `24a_matrix_transpose.py` | Transpose (rectangular) |
| `24b_matrix_scalar_divide.py` | Divide matrix by scalar |
| `24c_matrix_negation.py` | Negate matrix (-A) |
| `25a_identity_times_matrix.py` | Identity * matrix |
| `25b_trace.py` | Trace (diagonal sum) |
| `25c_determinant_2x2.py` | Determinant 2x2 |
| `26_row_column_sums.py` | Row/column sums |
| `27a_elementwise_division.py` | Element-wise division |
| `27b_matrix_squared.py` | Matrix square (I * I) |
| `28_practical_examples.py` | Practical examples |
| `29_inverse.py` | Matrix inverse |
| `30_determinant_methods.py` | Determinant by different methods *(planned)* |
| `31_symmetric_skew.py` | Symmetric and skew-symmetric *(planned)* |
| `32_upper_lower_triangular.py` | Upper/lower triangular *(planned)* |
| `33_diagonal_matrix.py` | Diagonal matrix operations *(planned)* |
| `34_sparse_matrix_intro.py` | Sparse matrices intro *(planned)* |
| `35_row_operations.py` | Elementary row operations |
| `36_gaussian_elimination.py` | Gaussian elimination |
| `37_gauss_jordan.py` | Reduced row echelon form *(planned)* |
| `38_solve_linear_system.py` | Solve Ax = b *(planned)* |
| `39_augmented_matrix.py` | Augmented matrices *(planned)* |
| `40_consistency_systems.py` | Consistent/inconsistent systems *(planned)* |

---

## NumPy (41-60)

| File | Content |
|------|---------|
| `41_install_import.py` | Install and import |
| `42_create_array.py` | Create arrays |
| `43_vectors.py` | Vectors with NumPy |
| `44_matrices.py` | Matrices with NumPy |
| `45_multiplication.py` | Multiplication |
| `46_summary.py` | Summary |
| `47_linalg.py` | Linear algebra (linalg) |
| `48_broadcasting.py` | Broadcasting |
| `49_array_attributes.py` | shape, ndim, size, dtype *(planned)* |
| `50_dtype_conversion.py` | astype and dtype conversion *(planned)* |
| `51_copy_vs_view.py` | Copy vs view *(planned)* |
| `52_axis_operations.py` | axis in sum, mean, max, min |
| `53_nan_inf_handling.py` | NaN and Inf handling *(planned)* |
| `54_save_load_arrays.py` | save, load, savez *(planned)* |
| `55_eigenvalues_eigenvectors.py` | Eigenvalues and eigenvectors |
| `56_svd_intro.py` | SVD *(planned)* |
| `57_lu_decomposition.py` | LU decomposition *(planned)* |
| `58_qr_decomposition.py` | QR decomposition *(planned)* |
| `59_condition_number.py` | Condition number *(planned)* |
| `60_norms.py` | Vector and matrix norms *(planned)* |

---

## Vectors (61-72)

| File | Content |
|------|---------|
| `61_create_display.py` | Create and display |
| `62_add.py` | Add vectors |
| `63_scalar_product.py` | Scalar product |
| `64_dot_product.py` | Dot product |
| `65_magnitude.py` | Magnitude |
| `66_subtract.py` | Subtract vectors |
| `67_unit_vector.py` | Normalize vector |
| `68_angle_between_vectors.py` | Angle between vectors *(planned)* |
| `69_projection.py` | Vector projection *(planned)* |
| `70_cross_product.py` | Cross product |
| `71_distance_between_vectors.py` | Euclidean distance *(planned)* |
| `72_cosine_similarity.py` | Cosine similarity *(planned)* |

---

## Arrays (73-89)

| File | Content |
|------|---------|
| `73_slicing_indexing.py` | Slicing, indices |
| `74_reshape_flatten.py` | Reshape, flatten, ravel |
| `75_stack_concatenate.py` | vstack, hstack, concatenate |
| `76_statistics.py` | sum, mean, min, max, std |
| `77_sorting.py` | sort, argsort |
| `78_bool_ix.py` | Boolean masks, fancy indexing, AND/OR |
| `79_arange_linspace.py` | arange, linspace, meshgrid |
| `80_random.py` | rand, randn, randint, choice |
| `81_unique_counts.py` | unique, return_counts, bincount |
| `82_where.py` | np.where: indices and conditional replacement |
| `83_padding.py` | pad arrays *(planned)* |
| `84_repeat_tile.py` | repeat and tile *(planned)* |
| `85_split_arrays.py` | split, hsplit, vsplit *(planned)* |
| `86_clip_round.py` | clip, round, floor, ceil *(planned)* |
| `87_searching.py` | argmax, argmin, nonzero *(planned)* |
| `88_cumulative_ops.py` | cumsum, cumprod *(planned)* |
| `89_percentiles_quantiles.py` | percentile, quantile *(planned)* |
| `98a_array_linear_search.py` | Linear search |
| `98b_array_membership_index.py` | `in`, index(), count() |
| `98c_array_binary_search.py` | Binary search (sorted list) |
| `98d_array_filter_extrema.py` | filter, comprehension, min/max |
| `110_df_bool.py` | Pandas: boolean row filter (data_colors) |

---

## Matrix Problems / Practice (90-99)

| File | Content |
|------|---------|
| `90_spiral_traversal.py` | Spiral traversal |
| `91_set_matrix_zeroes.py` | Set matrix zeroes |
| `92_search_2d_matrix.py` | Search in sorted 2D matrix |
| `93_rotate_image_90.py` | Rotate image 90° *(planned)* |
| `94_diagonal_sum.py` | Diagonal sum *(planned)* |
| `95_toeplitz_matrix.py` | Toeplitz matrix check *(planned)* |
| `96_matrix_reshape.py` | Matrix reshape problem *(planned)* |
| `97_flood_fill_matrix.py` | Flood fill *(planned)* |
| `98_game_of_life.py` | Conway's Game of Life *(planned)* |
| `99_island_perimeter.py` | Island perimeter *(planned)* |

---

## Special Matrix Implementations (100-108)

| File | Content |
|------|---------|
| `100a_tridiagonal_create.py` | Tridiagonal: full matrix and 3 vectors |
| `100b_tridiagonal_verify.py` | Test if matrix is tridiagonal |
| `100c_tridiagonal_read.py` | Read diagonals, memory stats |
| `100d_tridiagonal_operations.py` | Sum, scalar, fast matvec |
| `100e_tridiagonal_thomas.py` | Thomas algorithm (Ax = b) |
| `100f_tridiagonal_storage.py` | Full grid vs compact storage |
| `101a_lower_triangular_create.py` | Lower triangular construction |
| `101b_lower_triangular_verify.py` | Verify lower triangular |
| `101c_lower_triangular_read.py` | Read regions and stats |
| `101d_lower_triangular_operations.py` | Sum, product, transpose |
| `101e_lower_forward_substitution.py` | Forward substitution Lx = b |
| `101f_lower_determinant_diagonal.py` | det(L) = product diagonal |
| `102a_upper_triangular_create.py` | Upper triangular construction |
| `102b_upper_triangular_verify.py` | Verify upper triangular |
| `102c_upper_triangular_read.py` | Read upper region, trace |
| `102d_upper_triangular_operations.py` | Sum, scalar, transpose |
| `102e_upper_back_substitution.py` | Back substitution Ux = b |
| `103_hadamard_matrix_multiplication.py` | Element-wise multiplication (Hadamard product) |
| `104_elementwise_matrix_addition.py` | Element-wise matrix addition |
| `105_elementwise_matrix_subtraction.py` | Element-wise matrix subtraction |
| `106_standard_matrix_multiplication.py` | Standard matrix multiplication (dot product) |
| `107_matrix_transpose.py` | Matrix transpose (swap rows and columns) |
| `108_scalar_matrix_multiplication.py` | Scalar matrix multiplication |

---

## Utilities

| File | Content |
|------|---------|
| `rank_util.py` | Matrix rank utility |
| `matrix_helpers.py` | Print helpers + samples for 100a-102e |

---

*Planned items can be added incrementally. The 10 most valuable additions (29, 35, 36, 52, 55, 67, 70, 90, 91, 92) are already implemented.*
