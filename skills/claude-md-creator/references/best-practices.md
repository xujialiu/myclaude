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

### Creation Checklist

Before finalizing a new CLAUDE.md:

- [ ] Under 50 lines total
- [ ] No formatting/linting rules
- [ ] References docs/architecture.md for details
- [ ] Includes conda env instructions for Python projects
- [ ] Build/test commands are accurate
- [ ] Tech stack versions are current
- [ ] No duplicated info from config files

### Update Checklist

Before finalizing updates to existing CLAUDE.md:

- [ ] Read existing CLAUDE.md before making changes
- [ ] Identified what actually changed in codebase
- [ ] Preserved user customizations and custom sections
- [ ] Updated only sections that are now outdated
- [ ] Verified all commands still work
- [ ] Confirmed referenced files/paths exist
- [ ] Kept file under 50 lines
- [ ] Did not reintroduce previously removed content

## Updating Existing CLAUDE.md

When a CLAUDE.md already exists, update rather than recreate.

### When to Update

- New dependencies or frameworks added
- Project structure changed significantly
- Build/test commands changed
- Documented paths no longer exist
- Tech stack versions are outdated

### Update Strategy

**Minimal changes preferred**: Only modify sections that are actually outdated. Don't rewrite the entire file if only one section needs updating.

**Detect user customizations**: Look for:
- Non-standard section headings
- Comments like `<!-- custom -->` or `<!-- keep -->`
- Project-specific warnings or notes
- Links to team wikis or external docs

**Merge, don't replace**: When adding new information, integrate it into existing structure rather than replacing sections wholesale.

### Common Update Scenarios

| Scenario | Action |
|----------|--------|
| New dependency added | Add to Tech Stack section |
| Directory renamed | Update Project Structure |
| New script added | Add to Development commands |
| Deprecated command | Remove or update command |
| New doc file created | Add to Additional Documentation |
| Framework upgraded | Update version in Tech Stack |

### Handling Conflicts

If codebase contradicts CLAUDE.md:
1. Verify which is correct (run commands, check files)
2. Update CLAUDE.md to match reality
3. If user made intentional customizations, ask before overwriting

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
