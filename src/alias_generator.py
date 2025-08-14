#!/usr/bin/env python3
"""
Email Alias Generator - A simple interactive tool for generating email aliases
"""

import click
import json
import csv
import random
from pathlib import Path
from generators import (
    generate_random_alias,
    generate_variations,
    generate_plus_aliases,
    load_word_lists,
    generate_mixed_aliases
)


def interactive_mode():
    """Interactive mode for generating aliases."""
    click.clear()
    click.echo("\n🌟 Welcome to Email Alias Generator!\n")
    
    # Get user's email
    while True:
        email = click.prompt("Enter your email address", type=str).strip().lower()
        if '@' in email and '.' in email.split('@')[1]:
            break
        else:
            click.echo("❌ Please enter a valid email address (e.g., user@gmail.com)")
    
    # Check if it's Gmail
    domain = email.split('@')[1]
    is_gmail = domain in ['gmail.com', 'googlemail.com']
    
    if is_gmail:
        click.echo("\n✨ Great! Gmail supports true aliases with dots and plus addressing.")
        click.echo("All generated aliases will forward to your inbox!")
    else:
        click.echo(f"\n📌 Note: {domain} aliases use plus addressing (+) which most providers support.")
        click.echo("Check if your email provider supports plus addressing.")
    
    # Get number of aliases
    count = click.prompt("\nHow many aliases do you want to generate?", type=int, default=5)
    
    click.echo("\n⏳ Generating aliases...\n")
    
    # Generate mixed aliases automatically
    aliases = generate_mixed_aliases(email, count)
    
    # Display results with type indicators
    click.echo("📧 Your Generated Email Aliases:\n")
    username = email.split('@')[0]
    
    for i, alias in enumerate(aliases, 1):
        # Indicate type of alias
        if '+' in alias:
            alias_type = " (plus address)"
        elif alias.split('@')[0].replace('.', '') == username.replace('.', '') and is_gmail:
            alias_type = " (Gmail dot variation)"
        else:
            alias_type = " (variation)"
        
        click.echo(f"  {i}. {alias}{alias_type}")
    
    click.echo(f"\n✅ Total: {len(aliases)} unique aliases generated!")
    
    # Ask if user wants to save
    if click.confirm("\nWould you like to save these aliases to a file?"):
        filename = click.prompt("Enter filename (without extension)", default="my_aliases")
        format_choice = click.prompt(
            "Choose format (text/json/csv)", 
            type=click.Choice(['text', 'json', 'csv']), 
            default='text'
        )
        
        filepath = f"{filename}.{format_choice if format_choice != 'text' else 'txt'}"
        save_to_file(aliases, filepath, format_choice)
        click.echo(f"\n💾 Saved to {filepath}")
    
    # Ask if user wants to generate more
    if click.confirm("\nWould you like to generate more aliases?"):
        interactive_mode()
    else:
        click.echo("\n👋 Thanks for using Email Alias Generator!\n")


@click.command()
@click.option('--interactive', '-i', is_flag=True, help='Run in interactive mode (default)')
@click.option('--email', '-e', help='Email address for quick generation')
@click.option('--count', '-c', default=5, help='Number of aliases to generate')
@click.option('--output', '-o', help='Output file path')
@click.option('--format', '-f', 
              type=click.Choice(['text', 'json', 'csv']), 
              default='text',
              help='Output format')
def main(interactive, email, count, output, format):
    """Email Alias Generator - Create email aliases easily!"""
    
    # If no arguments provided or interactive flag, run interactive mode
    if interactive or (not email and not output):
        interactive_mode()
    else:
        # Quick generation mode
        if not email:
            click.echo("Error: --email is required for non-interactive mode", err=True)
            return
        
        if '@' not in email or '.' not in email.split('@')[1]:
            click.echo("Error: Please provide a valid email address", err=True)
            return
        
        aliases = generate_mixed_aliases(email, count)
        
        if output:
            save_to_file(aliases, output, format)
            click.echo(f"✓ Generated {len(aliases)} aliases and saved to {output}")
        else:
            display_aliases(aliases, format)


def display_aliases(aliases, format):
    """Display aliases in the specified format."""
    if format == 'json':
        click.echo(json.dumps(aliases, indent=2))
    elif format == 'csv':
        click.echo("email")
        for alias in aliases:
            click.echo(alias)
    else:  # text
        click.echo("\n📧 Generated Email Aliases:\n")
        for i, alias in enumerate(aliases, 1):
            click.echo(f"  {i}. {alias}")
        click.echo(f"\n✓ Total: {len(aliases)} aliases")


def save_to_file(aliases, filepath, format):
    """Save aliases to a file in the specified format."""
    path = Path(filepath)
    
    if format == 'json':
        with open(path, 'w') as f:
            json.dump(aliases, f, indent=2)
    elif format == 'csv':
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['email'])
            for alias in aliases:
                writer.writerow([alias])
    else:  # text
        with open(path, 'w') as f:
            for alias in aliases:
                f.write(f"{alias}\n")


if __name__ == '__main__':
    main()
