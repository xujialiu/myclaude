# CLAUDE.md Best Practices

Detailed guidance for creating effective CLAUDE.md files.

## Why CLAUDE.md Matters

LLMs are stateless - they only know what you provide in each session. CLAUDE.md enters every conversation, making it the primary mechanism for onboarding Claude to your codebase.

## The WHAT, WHY, HOW Framework

### WHAT to Include
- Project structure and codebase map (critical for monorepos)
- Technology stack and versions
- Key directories and their purposes

### WHY to Include
- Project purpose and goals
- Function of different components
- Relationship between parts

### HOW to Include
- Build and test procedures
- Verification methods
- Required tools (e.g., bun vs node, conda vs pip)

## Length Guidelines

| Metric | Target |
|--------|--------|
| Total lines | Under 50 |
| Instructions | ~20-30 actionable items max |
| Sections | 5-7 focused sections |

Research indicates frontier LLMs can follow ~150-200 instructions consistently. Claude Code's system prompt already contains ~50 instructions, so CLAUDE.md should stay lean.

## What NOT to Include

### Code Style Rules
Never include formatting guidelines. Use deterministic tools instead:
- ESLint, Prettier for JavaScript/TypeScript
- Black, Ruff for Python
- gofmt for Go

LLMs learn patterns in-context naturally from the codebase.

### Auto-generated Content
Don't use `/init` or similar auto-generation. CLAUDE.md is high-leverage - each line affects every workflow phase. Manual curation ensures quality.

### Task-specific Information
Information about unrelated tasks distracts the model. Keep only universally applicable content.

## Progressive Disclosure Strategy

Instead of bloating CLAUDE.md, create separate documentation:

```
project/
├── CLAUDE.md              # <50 lines, essential info only
└── docs/
    └── architecture.md    # Detailed patterns and decisions
```

Reference from CLAUDE.md:
```markdown
## Additional Documentation
- [Architecture & Patterns](docs/architecture.md)
```

Use `file:line` pointers instead of copying code snippets to maintain accuracy.

## docs/architecture.md Contents

Document patterns observed across multiple files:

### Architectural Patterns
- Dependency injection approach
- State management strategy
- Error handling conventions
- Logging patterns

### Design Decisions
- Why certain libraries were chosen
- Trade-offs considered
- Future considerations

### Conventions
- Naming patterns (but not formatting)
- File organization logic
- Component structure patterns

### API Patterns
- Endpoint naming conventions
- Request/response patterns
- Authentication approach

## Quality Checklist

Before finalizing CLAUDE.md:

- [ ] Under 50 lines total
- [ ] No formatting/linting rules
- [ ] References docs/architecture.md for details
- [ ] Includes conda env instructions for Python projects
- [ ] Build/test commands are accurate
- [ ] Tech stack versions are current
- [ ] No duplicated info from config files

## Example: Minimal CLAUDE.md

```markdown
# TaskFlow API

RESTful task management service with PostgreSQL backend.

## Tech Stack
- Python 3.11 / FastAPI
- PostgreSQL 15, Redis
- Docker Compose for local dev

## Structure
```
src/
  api/        # FastAPI routes
  models/     # SQLAlchemy models
  services/   # Business logic
tests/        # pytest tests
```

## Development
```bash
docker-compose up -d
conda run -n taskflow python -m uvicorn src.main:app --reload
```

## Testing
```bash
conda run -n taskflow pytest
```

## Additional Documentation
- [Architecture](docs/architecture.md) - Patterns and conventions
```

This example is ~30 lines and covers essentials without bloat.
