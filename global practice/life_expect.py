with open(r"C:\Users\HP\Documents\CSE homework\global practice\life-expectancy1.csv") as global_life: 

        header_line = next(global_life, None)
        if header_line is None:
            print("File is empty.")
            raise SystemExit

        header = [h.strip() for h in header_line.strip().split(",")]
        print("Header (row 1):", header)

        line_number = 2
        data = []
        preview_count = 0

        for raw_line in global_life:  
            line = raw_line.strip()
            if not line:
                print(f"Skipping blank line at row {line_number}")
                line_number += 1
                continue

            parts = [p.strip() for p in line.split(",")]
            if len(parts) != 4:
                print(f"Skipping malformed line at row {line_number}: {parts}")
                line_number += 1
                continue

            entity, code, year_str, le_str = parts

            try:
                year = int(year_str)
                life_expectancy = float(le_str)
            except ValueError:
                print(f"Skipping invalid row at {line_number}")
                line_number += 1
                continue

            data.append((entity, code, year, life_expectancy))

            if preview_count < 5:
                print(f"Valid Row {preview_count+1}: {entity} ({code}), {year}, {life_expectancy}")
                preview_count += 1

            line_number += 1

        
        if not data:
            print("No valid data found.")
        else:
            earliest_year = min(row[2] for row in data)
            latest_year = max(row[2] for row in data)
            total_le_overall = sum(row[3] for row in data)
            lowest_row = min(data, key=lambda r: r[3])
            highest_row = max(data, key=lambda r: r[3])

            average_expectancy = total_le_overall / len(data)

            print(f"\nYear range: from {earliest_year} to {latest_year}")
            print(f"Lowest life expectancy overall: {lowest_row[0]} ({lowest_row[1]}) - {lowest_row[3]:.2f} ({lowest_row[2]})")
            print(f"Highest life expectancy overall: {highest_row[0]} ({highest_row[1]}) - {highest_row[3]:.2f} ({highest_row[2]})")
            print(f"Overall average life expectancy: {average_expectancy:.2f}")

            choose_input = input("\nType in a year of your choice: ").strip()
            try:
                choose = int(choose_input)
            except ValueError:
                print("Invalid year entered.")
            else:
                chosen_year_data = [row for row in data if row[2] == choose]
                if not chosen_year_data:
                    print(f"No data for {choose}.")
                else:
                    year_total = sum(row[3] for row in chosen_year_data)
                    year_low = min(chosen_year_data, key=lambda r: r[3])
                    year_high = max(chosen_year_data, key=lambda r: r[3])

                    avg_for_year = year_total / len(chosen_year_data)

                    print(f"\nAverage life expectancy in {choose}: {avg_for_year:.2f}")
                    print(f"Lowest in {choose}: {year_low[0]} ({year_low[1]}) - {year_low[3]:.2f}")
                    print(f"Highest in {choose}: {year_high[0]} ({year_high[1]}) - {year_high[3]:.2f}")

                    choose_country = input("\nType in a country name to analyze: ").strip().lower()
        chosen_country_data = [row for row in data if row[0].lower() == choose_country]

        if not chosen_country_data:
            print(f"No data for country: {choose_country}")
        else:
            country_total = sum(row[3] for row in chosen_country_data)
            country_low = min(chosen_country_data, key=lambda r: r[3])
            country_high = max(chosen_country_data, key=lambda r: r[3])
            avg_for_country = country_total / len(chosen_country_data)

            print(f"\nLife Expectancy Statistics for {country_low[0]}:")
            print(f"  Average: {avg_for_country:.2f}")
            print(f"  Lowest: {country_low[3]:.2f} in {country_low[2]}")
            print(f"  Highest: {country_high[3]:.2f} in {country_high[2]}")




