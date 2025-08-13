# Email Alias Generator

A simple, interactive tool for generating email aliases automatically. Just enter your email and the number of aliases you need - the tool handles the rest!

## Features

- **Interactive Mode**: Simple 2-step process - enter email, choose count, done!
- **Automatic Mix**: Generates a smart mix of variations, plus addresses, and random aliases
- **No Configuration**: The tool automatically decides the best mix of alias types
- **Save Options**: Optionally save your aliases to text, JSON, or CSV files
- **Lightweight**: Only ~100KB total, minimal dependencies

## Installation

1. Clone or download this repository
2. Install the required dependency:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Interactive Mode (Recommended)

Simply run:
```bash
python alias_generator.py
```

You'll be prompted to:
1. Enter your email address
2. Choose how many aliases you want (default: 5)
3. That's it! Your aliases are generated automatically

The tool will generate a smart mix of:
- Variations of your email (john.doe123@gmail.com, j.ohndoe@gmail.com)
- Plus addresses (john.doe+shopping@gmail.com)
- Creative random aliases (happywolf123@gmail.com)

### Quick Command Mode

For automation or scripts:
```bash
python alias_generator.py --email john.doe@gmail.com --count 10
```

Save directly to file:
```bash
python alias_generator.py --email john.doe@gmail.com --count 20 --output aliases.txt
```

Different formats:
```bash
python alias_generator.py --email john.doe@gmail.com --count 15 --output aliases.json --format json
```

## Example Output

When you run the tool, you'll see something like:
```
🌟 Welcome to Email Alias Generator!

Enter your email address: john.doe@gmail.com
How many aliases do you want to generate? [5]: 10

⏳ Generating aliases...

📧 Your Generated Email Aliases:

  1. john.doe+shopping@gmail.com
  2. john.doe123@gmail.com
  3. happyeagle47@gmail.com
  4. j.ohndoe@gmail.com
  5. john.doe+work@gmail.com
  6. cosmic_star@gmail.com
  7. john.doe2024@gmail.com
  8. john.doe.pro@gmail.com
  9. swiftphoenix99@gmail.com
  10. john.doe+newsletter@gmail.com

✅ Total: 10 unique aliases generated!

Would you like to save these aliases to a file? [y/N]:
```

## Command Line Options

- `--interactive, -i`: Run in interactive mode (default)
- `--email, -e`: Email address for quick generation
- `--count, -c`: Number of aliases to generate
- `--output, -o`: Output file path
- `--format, -f`: Output format (text, json, csv)

## Customization

You can customize the word lists by editing:
- `adjectives.txt`: Add your own adjectives for random aliases
- `nouns.txt`: Add your own nouns for random aliases

## License

MIT License - Feel free to use and modify as needed!
