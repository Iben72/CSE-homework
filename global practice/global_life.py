# creativity was added by asking users to choose a country 
# and the life expectancy indices was determine for the country choosen as seen in ln 87 to ln 101.

# Simplified Life Expectancy Program

# Simplified Life Expectancy Program (with protections)

# Open the CSV file
with open(r"C:\Users\HP\Documents\CSE homework\global practice\life-expectancy1.csv") as f:
    lines = f.readlines()

# Remove the header row and keep only the data rows
header = lines[0].strip().split(",")
data_lines = lines[1:]

# Turn each row into a tuple (Country, Code, Year, LifeExpectancy)
data = []
for line in data_lines:
    country, code, year, life_exp = line.strip().split(",")
    data.append((country, code, int(year), float(life_exp)))

# Overall statistics
years = [row[2] for row in data]
life_exps = [row[3] for row in data]

print(f"Year range: {min(years)} - {max(years)}")
print(f"Lowest life expectancy: {min(data, key=lambda r: r[3])}")
print(f"Highest life expectancy: {max(data, key=lambda r: r[3])}")
print(f"Overall average life expectancy: {sum(life_exps) / len(life_exps):.2f}")

# -----------------------------
# Ask user for a year
# -----------------------------
choose_input = input("\nEnter a year: ").strip()

if choose_input.isdigit():   # make sure input is a number
    choose_year = int(choose_input)
    year_data = [row for row in data if row[2] == choose_year]

    if year_data:
        avg_year = sum(r[3] for r in year_data) / len(year_data)
        print(f"\nAverage in {choose_year}: {avg_year:.2f}")
        print("Lowest:", min(year_data, key=lambda r: r[3]))
        print("Highest:", max(year_data, key=lambda r: r[3]))
    else:
        print(f"No data for {choose_year}.")
else:
    print("Invalid year entered.")

# -----------------------------
# Ask user for a country
# -----------------------------
choose_country = input("\nEnter a country: ").strip().lower()
country_data = [row for row in data if row[0].lower() == choose_country]

if country_data:
    avg_country = sum(r[3] for r in country_data) / len(country_data)
    print(f"\nLife Expectancy for {choose_country.title()}:")
    print(f"  Average: {avg_country:.2f}")
    print("  Lowest:", min(country_data, key=lambda r: r[3]))
    print("  Highest:", max(country_data, key=lambda r: r[3]))
else:
    print(f"No data for country: {choose_country}")
