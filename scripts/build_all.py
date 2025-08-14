#!/usr/bin/env python3
"""
Build script to create both CLI and GUI executables
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def build_executables():
    """Build both CLI and GUI executables."""
    
    print("🔨 Building Email Alias Generator executables...")
    
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
    
    # Create dist directory
    os.makedirs('dist', exist_ok=True)
    
    # Build CLI version
    print("\n🚀 Building CLI version...")
    cli_cmd = [
        "pyinstaller",
        "--onefile",
        "--console",
        "--name=EmailAliasGenerator-CLI",
        "--add-data=data/adjectives.txt;data",
        "--add-data=data/nouns.txt;data",
        "--add-data=data/verbs.txt;data",
        "--distpath=dist",
        "--workpath=build",
        "src/alias_generator.py"
    ]
    
    try:
        subprocess.check_call(cli_cmd)
        cli_path = Path("dist/EmailAliasGenerator-CLI.exe")
        if cli_path.exists():
            size_mb = cli_path.stat().st_size / (1024 * 1024)
            print(f"✅ CLI version created: {size_mb:.1f} MB")
        else:
            print("❌ CLI build failed")
            return False
    except subprocess.CalledProcessError as e:
        print(f"❌ CLI build failed: {e}")
        return False
    
    # Build GUI version
    print("\n🚀 Building GUI version...")
    gui_cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",  # No console window
        "--name=EmailAliasGenerator-GUI",
        "--add-data=data/adjectives.txt;data",
        "--add-data=data/nouns.txt;data",
        "--add-data=data/verbs.txt;data",
        "--distpath=dist",
        "--workpath=build",
        "gui/gui_tkinter.py"
    ]
    
    try:
        subprocess.check_call(gui_cmd)
        gui_path = Path("dist/EmailAliasGenerator-GUI.exe")
        if gui_path.exists():
            size_mb = gui_path.stat().st_size / (1024 * 1024)
            print(f"✅ GUI version created: {size_mb:.1f} MB")
        else:
            print("❌ GUI build failed")
            return False
    except subprocess.CalledProcessError as e:
        print(f"❌ GUI build failed: {e}")
        return False
    
    return True

def create_installer_script():
    """Create installer script that lets users choose CLI or GUI."""
    
    installer_content = '''@echo off
echo.
echo ========================================
echo    Email Alias Generator Installer
echo ========================================
echo.
echo Choose your preferred version:
echo.
echo [1] GUI Version (Recommended for beginners)
echo     - Easy-to-use graphical interface
echo     - Click buttons, no typing commands
echo     - Perfect for non-technical users
echo.
echo [2] CLI Version (Advanced users)
echo     - Command-line interface
echo     - Faster for power users
echo     - Can be used in scripts/automation
echo.
echo [3] Install Both Versions
echo     - Get both CLI and GUI versions
echo     - Choose which one to use each time
echo.
echo [4] Exit installer
echo.

:choice
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto install_gui
if "%choice%"=="2" goto install_cli
if "%choice%"=="3" goto install_both
if "%choice%"=="4" goto exit_installer
echo Invalid choice. Please enter 1, 2, 3, or 4.
goto choice

:install_gui
echo.
echo Installing GUI Version...
set INSTALL_DIR=%USERPROFILE%\\EmailAliasGenerator
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
copy "EmailAliasGenerator-GUI.exe" "%INSTALL_DIR%\\EmailAliasGenerator.exe" >nul
echo.
echo ✅ GUI Version installed successfully!
echo.
echo To use: Double-click "%INSTALL_DIR%\\EmailAliasGenerator.exe"
echo Or run: "%INSTALL_DIR%\\EmailAliasGenerator.exe"
goto finish

:install_cli
echo.
echo Installing CLI Version...
set INSTALL_DIR=%USERPROFILE%\\EmailAliasGenerator
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
copy "EmailAliasGenerator-CLI.exe" "%INSTALL_DIR%\\EmailAliasGenerator.exe" >nul
echo.
echo ✅ CLI Version installed successfully!
echo.
echo To use from anywhere, add this to your PATH:
echo %INSTALL_DIR%
echo.
echo Or run directly: "%INSTALL_DIR%\\EmailAliasGenerator.exe"
goto finish

:install_both
echo.
echo Installing Both Versions...
set INSTALL_DIR=%USERPROFILE%\\EmailAliasGenerator
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
copy "EmailAliasGenerator-GUI.exe" "%INSTALL_DIR%\\EmailAliasGenerator-GUI.exe" >nul
copy "EmailAliasGenerator-CLI.exe" "%INSTALL_DIR%\\EmailAliasGenerator-CLI.exe" >nul

REM Create launcher script
echo @echo off > "%INSTALL_DIR%\\EmailAliasGenerator.bat"
echo echo Choose version: >> "%INSTALL_DIR%\\EmailAliasGenerator.bat"
echo echo [1] GUI Version >> "%INSTALL_DIR%\\EmailAliasGenerator.bat"
echo echo [2] CLI Version >> "%INSTALL_DIR%\\EmailAliasGenerator.bat"
echo set /p ver="Enter choice (1 or 2): " >> "%INSTALL_DIR%\\EmailAliasGenerator.bat"
echo if "%%ver%%"=="1" start "" "%%~dp0EmailAliasGenerator-GUI.exe" >> "%INSTALL_DIR%\\EmailAliasGenerator.bat"
echo if "%%ver%%"=="2" "%%~dp0EmailAliasGenerator-CLI.exe" >> "%INSTALL_DIR%\\EmailAliasGenerator.bat"

echo.
echo ✅ Both versions installed successfully!
echo.
echo To use: Run "%INSTALL_DIR%\\EmailAliasGenerator.bat"
echo Or run specific versions:
echo   - GUI: "%INSTALL_DIR%\\EmailAliasGenerator-GUI.exe"
echo   - CLI: "%INSTALL_DIR%\\EmailAliasGenerator-CLI.exe"
goto finish

:finish
echo.
echo Installation completed in: %INSTALL_DIR%
echo.
echo 📧 Email Alias Generator is ready to use!
echo.
echo ========================================
pause
goto :eof

:exit_installer
echo.
echo Installation cancelled.
echo.
pause
'''
    
    with open("installer.bat", "w", encoding='utf-8') as f:
        f.write(installer_content)
    
    print("📦 Created enhanced installer.bat with version selection")

if __name__ == "__main__":
    if build_executables():
        create_installer_script()
        print("\n🎯 Build Summary:")
        print("   ✅ CLI Version: EmailAliasGenerator-CLI.exe")
        print("   ✅ GUI Version: EmailAliasGenerator-GUI.exe") 
        print("   ✅ Smart Installer: installer.bat")
        print("\n🚀 Next steps:")
        print("   1. Test both versions")
        print("   2. Run installer.bat to test installation flow")
        print("   3. Create new GitHub release with both executables")
    else:
        print("\n❌ Build failed - check errors above")
