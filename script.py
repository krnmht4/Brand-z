import pandas as pd

# Load the CSV data
csv_df = pd.read_csv('indian_brands_merged_full.csv')

# Load the Excel data 
excel_df = pd.read_excel('indian_brands_phase2_with_celebrities.xlsx', sheet_name='Sheet1')

# Rename columns in Excel dataset for consistency
excel_df = excel_df.rename(columns={'Brand Name': 'Brand', 'Industry/Category': 'Industry'})

print("CSV columns:", csv_df.columns.tolist())
print("Excel columns:", excel_df.columns.tolist())

# Check the data overlap
print(f"CSV shape: {csv_df.shape}")
print(f"Excel shape: {excel_df.shape}")

# Merge datasets properly - use outer join to capture all brands
merged_df = pd.merge(csv_df, excel_df, on=['Brand', 'Industry'], how='outer', suffixes=('', '_excel'))

# For columns that exist in both, fill missing values from excel data
for col in ['Parent Company', 'Major Campaigns (Past 5 Years)', 'Celebrity Endorsements']:
    if col + '_excel' in merged_df.columns:
        merged_df[col] = merged_df[col].fillna(merged_df[col + '_excel'])
        merged_df.drop(columns=[col + '_excel'], inplace=True)

print(f"Merged shape: {merged_df.shape}")
print("Merged columns:", merged_df.columns.tolist())

# Save as brand_selection_list.csv
merged_df.to_csv('brand_selection_list.csv', index=False)

print("Data successfully merged and saved as brand_selection_list.csv")

# Show sample of the merged data
print("\nFirst 5 rows of merged data:")
print(merged_df[['Brand', 'Industry', 'Parent Company', 'Celebrity Endorsements']].head())