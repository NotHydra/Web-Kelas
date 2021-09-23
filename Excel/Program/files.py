global wb_mingguan_file
wb_mingguan_file = [
    "Excel/Mingguan/Excel/List Tugas Minggu Ke-1 (26 Juli 2021 -  1 Agustus 2021).xlsx",
    "Excel/Mingguan/Excel/List Tugas Minggu Ke-2 (2 Agustus 2021 - 8 Agustus 2021).xlsx",
    "Excel/Mingguan/Excel/List Tugas Minggu Ke-3 (9 Agustus 2021 - 15 Agustus 2021).xlsx",
    "Excel/Mingguan/Excel/List Tugas Minggu Ke-4 (16 Agustus 2021 - 22 Agustus 2021).xlsx",
    "Excel/Mingguan/Excel/List Tugas Minggu Ke-5 (23 Agustus 2021 - 29 Agustus 2021).xlsx",
    "Excel/Mingguan/Excel/List Tugas Minggu Ke-6 (30 Agustus 2021 - 5 September 2021).xlsx",
    "Excel/Mingguan/Excel/List Tugas Minggu Ke-7 (6 September 2021 - 12 September 2021).xlsx",
    "Excel/Mingguan/Excel/List Tugas Minggu Ke-8 (13 September 2021 - 19 September 2021).xlsx",
    "Excel/Mingguan/Excel/List Tugas Minggu Ke-9 (20 September 2021 - 26 September 2021).xlsx"
]

global wb_bulanan_file
wb_bulanan_file = [
    "Excel/Bulanan/Excel/List Tugas Bulanan Ke-1 (26 Juli 2021 - 29 Agustus 2021).xlsx",
    "Excel/Bulanan/Excel/List Tugas Bulanan Ke-2 (30 Juli 2021 - 27 September 2021).xlsx"
]

global wb_mingguan_image_name
wb_mingguan_image_name = [
    "Image List Tugas Minggu Ke-1",
    "Image List Tugas Minggu Ke-2",
    "Image List Tugas Minggu Ke-3",
    "Image List Tugas Minggu Ke-4",
    "Image List Tugas Minggu Ke-5",
    "Image List Tugas Minggu Ke-6",
    "Image List Tugas Minggu Ke-7",
    "Image List Tugas Minggu Ke-8",
    "Image List Tugas Minggu Ke-9"
]

global wb_bulanan_image_name
wb_bulanan_image_name = [
    "Image List Tugas Bulan Ke-1",
    "Image List Tugas Bulan Ke-2"
]

global weekly_task_start_column_range, weekly_task_end_column_range
weekly_task_start_column_range = [3, 8, 16, 23, 26, 34, 39, 42, 47]
weekly_task_end_column_range   = [8, 16, 23, 26, 34, 39, 42, 47, 52]

global monthly_task_start_column_range,monthly_task_end_column_range
monthly_task_start_column_range = [3, 34]
monthly_task_end_column_range   = [34, 52]

global wb_bulanan_start_container, wb_bulanan_end_container # How much week it contains
wb_bulanan_start_container = [1, 6]
wb_bulanan_end_container   = [6, 10]

global wb_bulanan_subtract
wb_bulanan_subtract = [0, 31]

global combined_task_range
combined_task_range = "A1:AY42"