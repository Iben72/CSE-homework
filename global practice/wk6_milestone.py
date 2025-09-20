with open("life-expectancy1.csv") as global_life:
    

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