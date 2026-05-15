# Usage Examples

## Organize Files

Preview changes first:

```bash
automation-toolkit organize-files examples/sample_files --dry-run
```

Move files into extension folders:

```bash
automation-toolkit organize-files examples/sample_files
```

Expected result:

```text
examples/sample_files/
├── pdf/
│   └── invoice.pdf
├── txt/
│   └── notes.txt
└── no_extension/
    └── README
```

## Clean Text

Input:

```bash
automation-toolkit clean-text "  Customer    needs    support  "
```

Output:

```text
Customer needs support
```

Input:

```bash
automation-toolkit clean-text "  Customer    NEEDS    Support  " --lowercase
```

Output:

```text
customer needs support
```

## Convert CSV to Excel

Input:

```bash
automation-toolkit csv-to-excel examples/sample_files/report.csv
```

Expected output:

```text
Excel file created: .../examples/sample_files/report.xlsx
```

Custom output path:

```bash
automation-toolkit csv-to-excel examples/sample_files/report.csv --output organized_output/report.xlsx
```
