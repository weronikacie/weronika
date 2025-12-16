import requests
from typing import Optional


class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        city: str,
        country: str,
        website_url: Optional[str],
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.country = country
        self.website_url = website_url

    def __str__(self) -> str:
        return (
            f"Browar: {self.name}\n"
            f"Typ: {self.brewery_type}\n"
            f"Miasto: {self.city}\n"
            f"Kraj: {self.country}\n"
            f"Strona: {self.website_url}\n"
            f"{'-' * 40}"
        )


def get_breweries() -> list[Brewery]:
    url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"
    response = requests.get(url)
    data = response.json()

    breweries = []
    for item in data:
        brewery = Brewery(
            id=item["id"],
            name=item["name"],
            brewery_type=item["brewery_type"],
            city=item["city"],
            country=item["country"],
            website_url=item.get("website_url"),
        )
        breweries.append(brewery)

    return breweries


if __name__ == "__main__":
    breweries_list = get_breweries()

    for brewery in breweries_list:
        print(brewery)
