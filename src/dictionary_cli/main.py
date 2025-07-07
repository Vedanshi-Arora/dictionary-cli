import click
import requests

API_KEY = "70ff34fa-8138-44a5-91b4-73446d6c35df"  # Get this from Merriam-Webster
BASE_URL = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"


@click.command()
@click.argument("word")
def cli(word):
    """Query Merriam-Webster dictionary for word definitions."""
    try:
        response = requests.get(f"{BASE_URL}{word}?key={API_KEY}")
        response.raise_for_status()
        data = response.json()

        if not data:
            click.echo(f"No definitions found for '{word}'")
            return

        if isinstance(data[0], str):
            click.echo(f"Word not found. Did you mean: {', '.join(data[:3])}?")
            return

        entry = data[0]
        if "hwi" in entry and "prs" in entry["hwi"]:
            pronunciation = entry["hwi"]["prs"][0]["mw"]
            click.echo(f"Pronunciation: {pronunciation}")

        if "shortdef" in entry:
            click.echo("\nDefinitions:")
            for i, definition in enumerate(entry["shortdef"], 1):
                click.echo(f"{i}. {definition}")

    except requests.exceptions.RequestException as e:
        click.echo(f"Error: {str(e)}")
