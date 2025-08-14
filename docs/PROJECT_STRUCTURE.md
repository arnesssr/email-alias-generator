# Email Alias Generator - Project Structure

This document describes the organized folder structure of the Email Alias Generator project.

## 📁 Directory Layout

```
email-alias-generator/
├── README.md                 # Main project documentation
├── setup.py                  # Python package setup configuration
├── requirements.txt          # Production dependencies
├── requirements-dev.txt      # Development dependencies
├── .gitignore                # Git ignore patterns
│
├── src/                      # 📂 Core application source code
│   ├── alias_generator.py    # Main CLI application entry point
│   └── generators.py         # Email alias generation logic
│
├── gui/                      # 📂 Graphical user interfaces
│   ├── gui_tkinter.py        # Main GUI using tkinter
│   └── gui_enhanced.py       # Enhanced CLI interface
│
├── data/                     # 📂 Word lists and data files
│   ├── adjectives.txt        # 200+ adjectives for creative aliases
│   ├── nouns.txt            # 400+ nouns for creative aliases
│   └── verbs.txt            # 300+ verbs for creative aliases
│
├── scripts/                  # 📂 Build and utility scripts
│   ├── build_all.py         # Build both CLI and GUI executables
│   ├── build_exe.py         # Original build script (legacy)
│   └── installer.bat        # Windows installer script
│
├── tests/                    # 📂 Test files and test data
│   └── test_aliases.json    # Sample test data
│
├── docs/                     # 📂 Documentation
│   └── PROJECT_STRUCTURE.md # This file
│
├── build/                    # 📂 Temporary build files (auto-generated)
│   └── [PyInstaller build artifacts]
│
└── dist/                     # 📂 Distribution files (auto-generated)
    ├── EmailAliasGenerator-CLI.exe    # CLI executable
    ├── EmailAliasGenerator-GUI.exe    # GUI executable
    └── installer.bat                  # Installer script
```

## 📄 File Descriptions

### Core Application (`src/`)
- **`alias_generator.py`**: Main CLI application with interactive and command-line modes
- **`generators.py`**: Core logic for generating email aliases with various strategies

### GUI Applications (`gui/`)
- **`gui_tkinter.py`**: Full-featured GUI using tkinter with buttons, file saving, copy functionality
- **`gui_enhanced.py`**: Enhanced CLI with better visual presentation

### Data Files (`data/`)
- **`adjectives.txt`**: 200+ descriptive words (vibrant, magnificent, creative, etc.)
- **`nouns.txt`**: 400+ nouns (animals, elements, professions, instruments, etc.)
- **`verbs.txt`**: 300+ action words (optimize, transform, create, excel, etc.)

### Build Scripts (`scripts/`)
- **`build_all.py`**: Modern build script that creates both CLI and GUI executables
- **`build_exe.py`**: Legacy build script (kept for compatibility)
- **`installer.bat`**: Smart Windows installer that lets users choose CLI or GUI

### Tests (`tests/`)
- **`test_aliases.json`**: Sample test data for development and testing

### Documentation (`docs/`)
- **`PROJECT_STRUCTURE.md`**: This documentation file

## 🔧 Build Process

The organized structure supports clean building:

1. **Data files** are properly bundled with PyInstaller from `data/` folder
2. **Source code** is separated in `src/` for better organization  
3. **GUI components** are isolated in `gui/` folder
4. **Build scripts** are centralized in `scripts/` folder
5. **Generated files** (`build/`, `dist/`) are kept separate from source

## 🚀 Usage

### Running from Source
```bash
# CLI version
python src/alias_generator.py

# GUI version  
python gui/gui_tkinter.py

# Build executables
python scripts/build_all.py
```

### Import Structure
```python
# From CLI
from src.generators import generate_mixed_aliases

# From GUI
from src.generators import generate_mixed_aliases
```

## 🎯 Benefits

1. **Clean Organization**: Related files are grouped together
2. **Easy Navigation**: Developers can quickly find what they need
3. **Scalable**: Easy to add new components in appropriate folders
4. **Professional**: Follows standard Python project conventions
5. **Build-Friendly**: PyInstaller can easily find and bundle resources
6. **Version Control**: `.gitignore` properly excludes build artifacts

This structure makes the project more maintainable and professional while supporting both development and distribution workflows.
