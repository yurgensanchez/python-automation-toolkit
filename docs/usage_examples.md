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

## Rename Files

Preview the changes:

```bash
automation-toolkit rename-files examples/sample_files --prefix document --dry-run
```

Apply the rename:

```bash
automation-toolkit rename-files examples/sample_files --prefix document
```

Expected result:

```text
document_001
document_002.csv
document_003.txt
```

## Generate File Report

Show a report in the terminal:

```bash
automation-toolkit file-report examples/sample_files
```

Write the report to a Markdown file:

```bash
automation-toolkit file-report examples/sample_files --output organized_output/report.md
```

Expected content:

```markdown
# Directory Report

Total files: 3

## Files by Extension

| Extension | Files |
| --- | ---: |
| csv | 1 |
| no_extension | 1 |
| txt | 1 |
```
