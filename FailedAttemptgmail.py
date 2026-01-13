try:
    with open('signup.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    print("HTML content successfully loaded into a string variable.")

    # Step 3 (Optional): Parse the HTML using BeautifulSoup
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_content, 'html.parser')

    # Example: Extract all paragraph text
    #paragraphs = soup.find_all('p')
    #print("\nExtracted Paragraphs:")
    #for p in paragraphs:
    #    print(p.get_text())

    username = soup.find("Username")
    password = soup.find("Password")

    # Example: Find a specific element by ID
    #specific_div = soup.find('div', id='my_data_section')
    #if specific_div:
    #    print(f"\nContent of 'my_data_section':\n{specific_div.get_text()}")
    #else:
    #    print("\n'my_data_section' not found.")

except FileNotFoundError:
    print("Error: 'your_file.html' not found. Please ensure the file exists in the correct directory.")
except Exception as e:
    print(f"An error occurred: {e}")
