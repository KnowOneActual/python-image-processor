# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a Python-based image processing project in its early stages. The repository currently contains:
- Basic project scaffolding with empty source files
- Standard documentation templates (README, CONTRIBUTING, CHANGELOG)
- Git workflow automation via `start-work.sh`
- Issue templates for bug reports and feature requests

## Development Workflow

### Starting New Work
Use the provided Git workflow script:
```bash
./start-work.sh
```
This script:
1. Checks for uncommitted changes
2. Prompts for a new branch name
3. Syncs the main branch with remote
4. Creates and switches to the new feature branch

### Branch Management
- Main branch: `main`
- Follow conventional branch naming (e.g., `feature/add-user-login`, `bugfix/memory-leak`)
- Always start new work from an updated main branch

## Project Structure

- `src/` - Source code directory (currently contains empty `main` file)
- `tests/` - Test directory (currently empty)
- `docs/` - Documentation directory (contains empty `index.md`)
- `.github/ISSUE_TEMPLATE/` - GitHub issue templates for bugs and features

## Code Standards

### Editor Configuration
The project uses `.editorconfig` with the following standards:
- **Indentation**: 2 spaces for all files
- **Line endings**: LF (Unix-style)
- **Charset**: UTF-8
- **Trailing whitespace**: Trimmed
- **Final newline**: Required

### Git Workflow
- Clean working directory required before starting new features
- Pull latest changes from `origin/main` before branching
- Use descriptive branch names following the pattern shown in `start-work.sh`

## Development Notes

### Current State
This project is in its initial setup phase:
- No Python dependencies or requirements files yet defined
- No build system, testing framework, or CI/CD configured
- Source code structure not yet established
- No package configuration (setup.py, pyproject.toml) present

### Future Setup Considerations
When developing Python code for this project, typical patterns will likely include:
- Setting up virtual environments for dependency management
- Adding requirements.txt or pyproject.toml for dependencies
- Implementing a proper Python package structure in `src/`
- Adding testing framework setup (pytest, unittest, etc.)
- Configuring linting and formatting tools (black, flake8, mypy)

### Git Configuration
The `.gitignore` includes comprehensive exclusions for:
- Python bytecode and virtual environments
- OS-specific files (macOS .DS_Store, Windows Thumbs.db)
- Editor/IDE configurations
- Build and distribution artifacts
- Environment variables and secrets
- Personal scratch files and shortcuts