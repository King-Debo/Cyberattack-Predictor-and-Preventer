# Step 2: Use requests and BeautifulSoup libraries to scrape the data from the data source URL and store it in the database.

# Import the necessary modules
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from predictor.models import CyberAttack

# Define a custom command to scrape and save the data
class Command(BaseCommand):
    # The data source URL
    url = "https://www.cyber.gov.au/acsc/view-all-content/reports-and-statistics/cyber-security-incidents-reported-acsc"

    # The method that executes the command
    def handle(self, *args, **options):
        # Get the HTML content from the URL
        response = requests.get(self.url)
        content = response.text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(content, "html.parser")

        # Find the table that contains the data
        table = soup.find("table", class_="table table-striped")

        # Find all the rows in the table
        rows = table.find_all("tr")

        # Loop through each row except the first one (header)
        for row in rows[1:]:
            # Find all the cells in the row
            cells = row.find_all("td")

            # Extract the data from each cell
            date = cells[0].text.strip()
            country = cells[1].text.strip()
            region = cells[2].text.strip()
            type = cells[3].text.strip()
            source = cells[4].text.strip()
            target = cells[5].text.strip()
            impact = cells[6].text.strip()

            # Create a CyberAttack object with the data
            cyberattack = CyberAttack(
                date=date,
                country=country,
                region=region,
                type=type,
                source=source,
                target=target,
                impact=impact,
            )

            # Save the CyberAttack object to the database
            cyberattack.save()

        # Print a success message
        self.stdout.write(self.style.SUCCESS("Data scraped and saved successfully!"))
