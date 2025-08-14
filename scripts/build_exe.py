#!/usr/bin/env python3
"""
Build script to create executable using PyInstaller
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def build_executable():
    """Build the executable using PyInstaller."""
    
    print("🔨 Building Email Alias Generator executable...")
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("❌ PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Clean up previous builds
    build_dirs = ['build', 'dist', '__pycache__']
    for dir_name in build_dirs:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"🧹 Cleaned up {dir_name}")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",                    # Create a single executable file
        "--console",                    # Keep console window (for interactive mode)
        "--name=EmailAliasGenerator",   # Name of the executable
        "--add-data=adjectives.txt;.",  # Include data files
        "--add-data=nouns.txt;.",
        "--distpath=dist",              # Output directory
        "--workpath=build",             # Work directory
        "alias_generator.py"            # Main Python file
    ]
    
    try:
        print(f"🚀 Running PyInstaller...")
        print(f"Command: {' '.join(cmd)}")
        subprocess.check_call(cmd)
        
        # Check if executable was created
        exe_path = Path("dist/EmailAliasGenerator.exe")
        if exe_path.exists():
            size_mb = exe_path.stat().st_size / (1024 * 1024)
            print(f"✅ Success! Executable created:")
            print(f"   📁 Path: {exe_path.absolute()}")
            print(f"   📏 Size: {size_mb:.1f} MB")
            print(f"")
            print(f"🎉 Your executable is ready! Users can now:")
            print(f"   1. Download EmailAliasGenerator.exe")
            print(f"   2. Double-click to run (no Python installation needed)")
            print(f"   3. Use it from command line: EmailAliasGenerator.exe --help")
        else:
            print("❌ Build failed - executable not found")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed with error: {e}")
        return False
    
    return True

def create_installer_script():
    """Create a simple installer script."""
    
    installer_content = '''@echo off
echo.
echo ================================
echo Email Alias Generator Installer
echo ================================
echo.

REM Create installation directory
set INSTALL_DIR=%USERPROFILE%\\EmailAliasGenerator
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

REM Copy executable
copy "EmailAliasGenerator.exe" "%INSTALL_DIR%\\" >nul

REM Add to PATH (optional)
echo.
echo The Email Alias Generator has been installed to:
echo %INSTALL_DIR%
echo.
echo To use from anywhere, you can:
echo 1. Add %INSTALL_DIR% to your PATH environment variable, OR
echo 2. Run directly: %INSTALL_DIR%\\EmailAliasGenerator.exe
echo.
echo Installation complete!
pause
'''
    
    with open("installer.bat", "w") as f:
        f.write(installer_content)
    
    print("📦 Created installer.bat for easy installation")

if __name__ == "__main__":
    if build_executable():
        create_installer_script()
        print("\n🎯 Next steps:")
        print("   1. Test the executable: .\\dist\\EmailAliasGenerator.exe")
        print("   2. Distribute the .exe file to users")
        print("   3. Optionally, include installer.bat for easy installation")
