#!/usr/bin/env python3
"""
Enhanced CLI version with better user experience
"""

import click
import os
import sys
from alias_generator import interactive_mode

def enhanced_cli():
    """Enhanced CLI with better presentation."""
    
    # Clear screen and set window title
    os.system('cls' if os.name == 'nt' else 'clear')
    if os.name == 'nt':
        os.system('title Email Alias Generator')
    
    # Create a nice header
    print("=" * 60)
    print("          🌟 EMAIL ALIAS GENERATOR 🌟")
    print("=" * 60)
    print()
    print("📧 Generate email aliases instantly!")
    print("✨ No setup required - just enter your email!")
    print("🎯 Perfect for privacy, organization, and testing")
    print()
    print("=" * 60)
    print()
    
    try:
        interactive_mode()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for using Email Alias Generator!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("\nPress Enter to exit...")
        input()
    
    # Wait before closing
    print("\n" + "=" * 60)
    print("Press Enter to exit...")
    input()

if __name__ == '__main__':
    enhanced_cli()
