---
name: claude-md-creator
description: Create or update CLAUDE.md files for projects. Use when (1) starting a new project that needs a CLAUDE.md, (2) updating an existing CLAUDE.md, (3) user asks to document a project for Claude, or (4) user mentions "CLAUDE.md", "claude md", or "project documentation for AI".
---

# CLAUDE.md Creator

Create concise, effective CLAUDE.md files that onboard Claude to codebases.

## Core Principles

1. **Under 50 lines** - Focus only on universally applicable information
2. **No code style rules** - Linters handle formatting; don't duplicate
3. **Progressive disclosure** - Reference docs/architecture.md for details
4. **Conda for Python** - Always use `conda run -n <env_name> python` for Python execution

## Workflow

### 1. Analyze the Codebase

Explore the project structure:
- Identify tech stack, frameworks, key directories
- Find existing documentation, READMEs, config files
- Detect patterns: dependency injection, state management, API design
- Note build/test commands from package.json, Makefile, etc.

### 2. Create docs/architecture.md

Extract observed patterns into docs/architecture.md covering:
- **Architectural patterns** - e.g., "Repository pattern for data access"
- **Design decisions** - e.g., "Redux for global state, React Query for server state"
- **Conventions** - e.g., "Components in PascalCase, hooks prefixed with use"
- **API patterns** - e.g., "REST endpoints follow /api/v1/{resource}/{id}"

Only document patterns appearing in multiple files.

### 3. Create CLAUDE.md

Structure (aim for ~40-50 lines max):

```markdown
# Project Name

Brief 1-2 sentence description of what this project does.

## Tech Stack

- Language/runtime versions
- Key frameworks and libraries
- Database/infrastructure

## Project Structure

```
src/
  components/    # React components
  services/      # Business logic
  api/           # API routes
```

## Development

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Run tests
npm test
```

## Python Execution

Always use conda environment:
```bash
conda run -n <env_name> python script.py
```

## Code Review

Use the code-reviewer agent after completing major implementation steps.

## Additional Documentation

- [Architecture & Patterns](docs/architecture.md) - Design decisions and conventions
```

### 4. Verify with Code Review

After creating CLAUDE.md and docs/architecture.md, use the code-reviewer agent to validate:
- Coverage of essential project information
- Accuracy of documented patterns
- No unnecessary detail or style rules

## Anti-patterns

- Including formatting/linting rules (use .eslintrc, .prettierrc instead)
- Documenting every file or function
- Adding "nice to have" sections
- Exceeding 50 lines in CLAUDE.md
- Duplicating info already in package.json or configs

## Reference

See [references/best-practices.md](references/best-practices.md) for detailed guidance on CLAUDE.md authoring.
