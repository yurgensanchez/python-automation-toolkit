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
