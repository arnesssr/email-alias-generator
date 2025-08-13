@echo off
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
set INSTALL_DIR=%USERPROFILE%\EmailAliasGenerator
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
copy "EmailAliasGenerator-GUI.exe" "%INSTALL_DIR%\EmailAliasGenerator.exe" >nul
echo.
echo ✅ GUI Version installed successfully!
echo.
echo To use: Double-click "%INSTALL_DIR%\EmailAliasGenerator.exe"
echo Or run: "%INSTALL_DIR%\EmailAliasGenerator.exe"
goto finish

:install_cli
echo.
echo Installing CLI Version...
set INSTALL_DIR=%USERPROFILE%\EmailAliasGenerator
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
copy "EmailAliasGenerator-CLI.exe" "%INSTALL_DIR%\EmailAliasGenerator.exe" >nul
echo.
echo ✅ CLI Version installed successfully!
echo.
echo To use from anywhere, add this to your PATH:
echo %INSTALL_DIR%
echo.
echo Or run directly: "%INSTALL_DIR%\EmailAliasGenerator.exe"
goto finish

:install_both
echo.
echo Installing Both Versions...
set INSTALL_DIR=%USERPROFILE%\EmailAliasGenerator
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
copy "EmailAliasGenerator-GUI.exe" "%INSTALL_DIR%\EmailAliasGenerator-GUI.exe" >nul
copy "EmailAliasGenerator-CLI.exe" "%INSTALL_DIR%\EmailAliasGenerator-CLI.exe" >nul

REM Create launcher script
echo @echo off > "%INSTALL_DIR%\EmailAliasGenerator.bat"
echo echo Choose version: >> "%INSTALL_DIR%\EmailAliasGenerator.bat"
echo echo [1] GUI Version >> "%INSTALL_DIR%\EmailAliasGenerator.bat"
echo echo [2] CLI Version >> "%INSTALL_DIR%\EmailAliasGenerator.bat"
echo set /p ver="Enter choice (1 or 2): " >> "%INSTALL_DIR%\EmailAliasGenerator.bat"
echo if "%%ver%%"=="1" start "" "%%~dp0EmailAliasGenerator-GUI.exe" >> "%INSTALL_DIR%\EmailAliasGenerator.bat"
echo if "%%ver%%"=="2" "%%~dp0EmailAliasGenerator-CLI.exe" >> "%INSTALL_DIR%\EmailAliasGenerator.bat"

echo.
echo ✅ Both versions installed successfully!
echo.
echo To use: Run "%INSTALL_DIR%\EmailAliasGenerator.bat"
echo Or run specific versions:
echo   - GUI: "%INSTALL_DIR%\EmailAliasGenerator-GUI.exe"
echo   - CLI: "%INSTALL_DIR%\EmailAliasGenerator-CLI.exe"
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
