
import pandas as pd

def check_csv_for_tokenization_issues(csv_file="Suicide_Detection.csv", text_col="text"):
    """
    Checks several potential pitfalls that cause 'ValueError: too many dimensions "str"' 
    or other tokenization issues with text data.
    1) Ensures text_col is always a string
    2) Checks for extremely long text entries
    3) Prints columns to confirm text_col exists
    4) Shows an example row
    """

    # 1) Load the CSV into a pandas DataFrame
    df = pd.read_csv(csv_file)
    print(f"Loaded {len(df)} rows from '{csv_file}'")

    # 2) Identify suspicious rows where text_col is not a str
    if text_col not in df.columns:
        print(f"ERROR: Column '{text_col}' not found in CSV. Columns are: {df.columns}")
        return
    
    # Check the column type
    mask = ~df[text_col].apply(lambda x: isinstance(x, str))
    problem_rows = df[mask]
    print(f"Number of suspicious rows (non-string '{text_col}'):", len(problem_rows))

    if len(problem_rows) > 0:
        print("\nSample suspicious rows:\n", problem_rows.head(5))
        print("Consider merging lists or removing them before tokenization.\n")
    else:
        print("No suspicious rows found. All entries in 'text' are strings.\n")

    # 3) Check text length
    df["text_length"] = df[text_col].apply(lambda x: len(x) if isinstance(x, str) else -1)
    print("Text length stats:\n", df["text_length"].describe(), "\n")

    # 4) Print columns
    print("Columns in CSV:", df.columns.tolist(), "\n")

    # 5) Show an example row (if any)
    if len(df) > 0:
        print("Example row:\n")
        print(df.iloc[0])
    else:
        print("No rows in the dataset to preview.")

if __name__ == "__main__":
    check_csv_for_tokenization_issues()
