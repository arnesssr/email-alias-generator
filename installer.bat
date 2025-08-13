@echo off
echo.
echo ================================
echo Email Alias Generator Installer
echo ================================
echo.

REM Create installation directory
set INSTALL_DIR=%USERPROFILE%\EmailAliasGenerator
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

REM Copy executable
copy "EmailAliasGenerator.exe" "%INSTALL_DIR%\" >nul

REM Add to PATH (optional)
echo.
echo The Email Alias Generator has been installed to:
echo %INSTALL_DIR%
echo.
echo To use from anywhere, you can:
echo 1. Add %INSTALL_DIR% to your PATH environment variable, OR
echo 2. Run directly: %INSTALL_DIR%\EmailAliasGenerator.exe
echo.
echo Installation complete!
pause
