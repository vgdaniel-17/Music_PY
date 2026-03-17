"""
Program that removes duplicates from files
"""

def clean_links(file_name):
    unique_lines = []
    # Set to keep track of lines we have already processed
    seen_line = set()

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                clean_line = line.strip()

                if not clean_line:
                    continue

                if clean_line not in seen_line:
                    seen_line.add(clean_line)
                    unique_lines.append(clean_line)

        with open(file_name, 'w', encoding='utf-8') as file:
            for link in unique_lines:
                file.write(link + '\n')
    except FileNotFoundError:
        print("File not found")
    except Exception as error:
        print(error)

clean_links('links.txt')

