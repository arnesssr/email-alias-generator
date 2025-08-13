"""
Email alias generation strategies
"""

import random
import string
from pathlib import Path


def load_word_lists():
    """Load adjectives and nouns from text files."""
    current_dir = Path(__file__).parent
    
    try:
        with open(current_dir / 'adjectives.txt', 'r') as f:
            adjectives = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        # Fallback adjectives if file not found
        adjectives = [
            'happy', 'sunny', 'cool', 'swift', 'bright', 'clever', 'quick',
            'brave', 'calm', 'wise', 'noble', 'keen', 'bold', 'sharp', 'smart'
        ]
    
    try:
        with open(current_dir / 'nouns.txt', 'r') as f:
            nouns = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        # Fallback nouns if file not found
        nouns = [
            'eagle', 'tiger', 'wolf', 'fox', 'hawk', 'bear', 'lion',
            'storm', 'wind', 'fire', 'star', 'moon', 'sun', 'sky', 'ocean'
        ]
    
    return adjectives, nouns


def generate_random_alias(adjectives, nouns, domain='gmail.com'):
    """Generate a random email alias using word combinations."""
    strategies = [
        # adjective + noun + number
        lambda: f"{random.choice(adjectives)}{random.choice(nouns)}{random.randint(1, 999)}@{domain}",
        # adjective + _ + noun
        lambda: f"{random.choice(adjectives)}_{random.choice(nouns)}@{domain}",
        # adjective + . + noun + number
        lambda: f"{random.choice(adjectives)}.{random.choice(nouns)}{random.randint(10, 99)}@{domain}",
        # noun + adjective + number
        lambda: f"{random.choice(nouns)}{random.choice(adjectives)}{random.randint(1, 999)}@{domain}",
        # single word + year-like number
        lambda: f"{random.choice(nouns)}{random.randint(2020, 2025)}@{domain}",
    ]
    
    return random.choice(strategies)()


def generate_variations(base_email, count):
    """Generate variations of a base email address."""
    if '@' not in base_email:
        return []
    
    username, domain = base_email.split('@')
    variations = []
    
    # Different variation strategies
    for i in range(count):
        strategy = i % 10  # Cycle through strategies
        
        if strategy == 0 and '.' not in username:
            # Add dots in username (if no dots exist)
            if len(username) > 2:
                pos = random.randint(1, len(username) - 1)
                variation = f"{username[:pos]}.{username[pos:]}@{domain}"
            else:
                variation = f"{username}{random.randint(1, 99)}@{domain}"
        elif strategy == 1:
            # Add numbers at the end
            variation = f"{username}{random.randint(1, 999)}@{domain}"
        elif strategy == 2:
            # Add year
            variation = f"{username}{random.randint(2020, 2025)}@{domain}"
        elif strategy == 3:
            # Add underscore and number
            variation = f"{username}_{random.randint(1, 99)}@{domain}"
        elif strategy == 4:
            # Prepend number
            variation = f"{random.randint(1, 9)}{username}@{domain}"
        elif strategy == 5:
            # Add common suffixes
            suffix = random.choice(['pro', 'mail', 'contact', 'info', 'official'])
            variation = f"{username}.{suffix}@{domain}"
        elif strategy == 6:
            # Double the username
            variation = f"{username}{username}@{domain}"
        elif strategy == 7:
            # Reverse username
            variation = f"{username[::-1]}@{domain}"
        elif strategy == 8:
            # Add dots and numbers
            if len(username) > 3:
                pos = len(username) // 2
                variation = f"{username[:pos]}.{username[pos:]}{random.randint(1, 99)}@{domain}"
            else:
                variation = f"{username}.{random.randint(100, 999)}@{domain}"
        else:
            # Mix letters with numbers
            variation = f"{username}{random.choice(string.ascii_lowercase)}{random.randint(10, 99)}@{domain}"
        
        variations.append(variation)
    
    return variations


def generate_plus_aliases(base_email, count, custom_words=None):
    """Generate plus addressing aliases (Gmail style)."""
    if '@' not in base_email:
        return []
    
    username, domain = base_email.split('@')
    aliases = []
    
    # Default words if none provided
    if not custom_words:
        custom_words = [
            'shopping', 'newsletter', 'social', 'work', 'personal',
            'updates', 'notifications', 'promo', 'info', 'contact',
            'register', 'signup', 'temp', 'test', 'backup'
        ]
    
    for i in range(count):
        if i < len(custom_words):
            word = custom_words[i]
        else:
            # Generate random combinations after exhausting custom words
            word = random.choice(custom_words)
            if random.choice([True, False]):
                word = f"{word}{random.randint(1, 99)}"
        
        alias = f"{username}+{word}@{domain}"
        aliases.append(alias)
    
    return aliases


def generate_mixed_aliases(base_email, total_count):
    """Generate a mix of different alias types automatically."""
    if '@' not in base_email:
        return []
    
    username, domain = base_email.split('@')
    aliases = []
    
    # For Gmail, only plus addressing and dots work as true aliases
    # For other providers, we'll generate variations
    is_gmail = domain.lower() in ['gmail.com', 'googlemail.com']
    
    if is_gmail:
        # Gmail supports dots and plus addressing
        strategies = [
            ('gmail_dots', 0.5),   # 50% chance - dots in username
            ('plus', 0.5),         # 50% chance - plus addressing
        ]
    else:
        # Other providers only support plus addressing as true aliases
        strategies = [
            ('plus', 1.0),         # 100% chance - only plus addressing works
        ]
    
    # Generate aliases
    generated_count = 0
    attempts = 0
    max_attempts = total_count * 10  # Prevent infinite loops
    
    while generated_count < total_count and attempts < max_attempts:
        attempts += 1
        
        # Choose strategy based on weights
        strategy_type = random.choices(
            [s[0] for s in strategies],
            weights=[s[1] for s in strategies]
        )[0]
        
        if strategy_type == 'gmail_dots':
            # Generate Gmail dot variations
            alias = generate_gmail_dot_variation(base_email)
            if alias and alias not in aliases:
                aliases.append(alias)
                generated_count += 1
        
        elif strategy_type == 'variation':
            # Generate a single variation
            variations = generate_variations(base_email, 1)
            if variations and variations[0] not in aliases:
                aliases.append(variations[0])
                generated_count += 1
        
        elif strategy_type == 'plus':
            # Generate a single plus alias
            plus_aliases = generate_plus_aliases(base_email, 1)
            if plus_aliases and plus_aliases[0] not in aliases:
                aliases.append(plus_aliases[0])
                generated_count += 1
    
    return aliases


def generate_gmail_dot_variation(base_email):
    """Generate Gmail-specific dot variations that actually work as aliases."""
    if '@' not in base_email:
        return None
    
    username, domain = base_email.split('@')
    
    # Remove existing dots for Gmail
    clean_username = username.replace('.', '')
    
    # If username is too short, just return None
    if len(clean_username) < 2:
        return None
    
    # Generate random dot positions
    num_dots = random.randint(1, min(3, len(clean_username) - 1))
    positions = sorted(random.sample(range(1, len(clean_username)), num_dots))
    
    # Insert dots at positions
    result = clean_username
    for i, pos in enumerate(positions):
        # Adjust position based on previously inserted dots
        adjusted_pos = pos + i
        result = result[:adjusted_pos] + '.' + result[adjusted_pos:]
    
    return f"{result}@{domain}"
