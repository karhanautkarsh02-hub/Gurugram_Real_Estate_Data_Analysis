import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#data cleaning
df = pd.read_csv('data.csv')
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df= df.drop_duplicates()

# numeric columns cleaning 
df['price'] = df['price'].astype(str).str.replace(',', '').astype(float)
df['area'] = df['area'].astype(str).str.replace(',', '').astype(int)
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(',', '').astype(int)


#categorical columns cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
df['flat_type'] = df['flat_type'].str.strip().str.lower()
df= df.drop_duplicates()

#Q1 which the costliest flat in the dataset?
costliest_flat = df.loc[df['price'].idxmax()]
print(f"The costliest flat in the dataset is: {costliest_flat['flat_type']} located in {costliest_flat['locality']} with a price of {costliest_flat['price']}.")

#Q2. Which locality has the highest average price?
highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
print (f"The locality with the highest average price is: {highest_avg_price_locality}.")

#Q3 Which locality has the highest rate per square foot?
highest_rate_per_sqft_locality = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print (f"The locality with the highest rate per square foot is: {highest_rate_per_sqft_locality}.")

#Q4 Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()
if ready_to_move_avg_price > under_construction_avg_price:
    print("Ready-to-move properties cost more than under-construction properties.")
else:
    print("Under-construction properties cost more than ready-to-move properties.") 

#Q5 Do RERA-approved properties command a price premium?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
rera_not_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()
if rera_approved_avg_price > rera_not_approved_avg_price:
    print("RERA-approved properties command a price premium.")
else:
    print("RERA-approved properties do not command a price premium.")

#Q6 How does area (sqft) impact property price?
sns.scatterplot(data=df, x='area', y='price')
plt.title('Area vs Price')
plt.xlabel('Area (sqft)')
plt.ylabel('Price')
plt.show()

#Q7 Which BHK configuration is the most expensive on average on the basis of per square foot?
most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive BHK configuration on average per square foot is: {most_expensive_bhk} BHK."  )


#Q8 Which property type (Apartment, Floor, Plot) is the costliest on the basis of per square foot?
costliest_property_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f"The costliest property type on the basis of per square foot is: {costliest_property_type}.")

#Q9 Do certain builders or companies consistently price higher?
#print top builders that price higher
print("Top  5 builders that price higher:", end=" ")
top_5_builders = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5)
for builder in top_5_builders.index:
    print(builder, end=", ")

#Q10 Are larger homes always more expensive per square foot?
sns.lineplot(data=df, x='area', y='rate_per_sqft')
plt.title('Area vs Rate per Square Foot')
plt.xlabel('Area (sqft)')
plt.ylabel('Rate per Square Foot')
plt.show()
