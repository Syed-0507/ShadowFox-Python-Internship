import requests
from bs4 import BeautifulSoup
import csv


# Website URL
url = "https://www.shadowfox.in/"

# Browser-like header
headers = {
    "User-Agent": "Mozilla/5.0"
}


try:
    # Send request to website
    response = requests.get(url, headers=headers, timeout=10)

    # Check for request errors
    response.raise_for_status()

    print("Website accessed successfully!")

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")


    # Names currently present in the testimonial section
    testimonial_names = [
        "Chetan Yadav",
        "Anushka Nair",
        "Patrick Udegor",
        "Prarthana R Karanth",
        "Shuban V Rao",
        "Rashi Sharma"
    ]


    testimonials = []


    # Search for each testimonial name
    for name in testimonial_names:

        name_tag = soup.find(
            "h4",
            string=lambda text: text and text.strip() == name
        )

        if name_tag:

            container = name_tag

            # Move upward through parent elements
            # until enough related text is found
            for _ in range(5):

                if container.parent:

                    container = container.parent

                    texts = list(container.stripped_strings)

                    if len(texts) >= 2:
                        break


            texts = list(container.stripped_strings)


            # Find position of the person's name
            if name in texts:

                name_index = texts.index(name)

                # The next text item is the domain
                if name_index + 1 < len(texts):
                    domain = texts[name_index + 1]
                else:
                    domain = "Not Available"


                testimonials.append({
                    "Name": name,
                    "Domain": domain
                })


    # Display scraped data
    print("\n----- ShadowFox Testimonials -----\n")

    for item in testimonials:

        print("Name:", item["Name"])
        print("Domain:", item["Domain"])
        print("-" * 50)


    # CSV file name
    output_file = "shadowfox_testimonials.csv"


    # Save data to CSV
    with open(
        output_file,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        fieldnames = [
            "Name",
            "Domain"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(testimonials)


    print("\nScraping completed successfully!")
    print("Total testimonials scraped:", len(testimonials))
    print("Data saved to:", output_file)


except requests.exceptions.RequestException as error:

    print("Error accessing the website:")
    print(error)