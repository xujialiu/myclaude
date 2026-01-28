---
name: create-book
description: "Author technical book chapters as Markdown files combining Richard Feynman's pedagogical style (simple analogies, first principles, plain English) with O'Reilly's technical depth (problem-solution oriented, production-ready code). For Python books, generate companion Jupyter notebooks for testing code. Use when asked to write tutorials, create educational technical content, explain programming concepts, author book chapters on technical topics, or build learning materials with code and narrative."
---

# Feynman-O'Reilly Book Author

Author technical book chapters as Markdown files that teach through intuition before formalism. For Python books, generate companion Jupyter notebooks for code testing.

## Core Philosophy

**The Feynman Method:**
- Explain core intuition as if to a bright child before mathematics or code
- Use plain English; define technical terms immediately with common-sense analogies
- Acknowledge when concepts are "weird" or counter-intuitive—never say "trivially"

**The O'Reilly Standard:**
- Problem-solution oriented sections
- Production-ready, PEP 8 compliant code with comments
- Clear progression from basic to advanced

## Output Format

**Primary format: Markdown (.md)**
- Clean, readable prose with code blocks
- No need to duplicate imports—assume sequential reading
- Focus on explanation and narrative flow

**For Python books: Companion Jupyter notebooks (.ipynb)**
- One notebook per chapter for testing code
- **Each cell runs independently**—include all imports and definitions
- Mirrors the Markdown structure for easy reference

## Directory Structure

```
[book-slug]/
├── 01_intro.md
├── 01_intro.ipynb          # Python only
├── 02_basics.md
├── 02_basics.ipynb         # Python only
├── data/
│   ├── chapter_01/         # Data files for chapter 1
│   └── chapter_02/         # Data files for chapter 2
└── output/
    ├── chapter_01/         # Notebook outputs for chapter 1
    └── chapter_02/         # Notebook outputs for chapter 2
```

**Data files (`./data/chapter_<num>/`):**
- Store input data (CSV, JSON, images, etc.) used by the chapter
- Reference in code as `./data/chapter_01/filename.csv`

**Output files (`./output/chapter_<num>/`):**
- Store notebook-generated outputs (plots, models, results)
- Save outputs to `./output/chapter_01/figure.png`

## Chapter Structure

Every chapter follows this format with **progressive difficulty**:

```markdown
# Chapter Title

## Learning Objective
[1-2 sentences: what the reader will understand/build]

## Basic: [Foundation Concept]
[Core intuition, simplest case, minimal code]

## Intermediate: [Building On Basics]
[Add complexity, handle edge cases, introduce patterns]

## Advanced: [Real-World Application]
[Production concerns, optimization, integration]

## Challenge Exercise
[Hands-on task at intermediate/advanced level]
```

### Progressive Difficulty Guidelines

**Basic section:**
- Introduce the core concept with simplest possible example
- Use toy data and minimal parameters
- Focus on "what" and "why", not edge cases

**Intermediate section:**
- Build on basic example with realistic complexity
- Handle common edge cases and errors
- Introduce configuration options and parameters

**Advanced section:**
- Address production concerns (performance, scale, error handling)
- Show integration with other tools/libraries
- Discuss trade-offs and when to use alternatives

## Markdown Patterns

### Narrative with Code

Build intuition before code. In Markdown, imports flow naturally:

```markdown
## The Core Idea

Imagine you're organizing a library. **A hash table** is like giving every book
a specific shelf number based on its title—you don't search; you calculate
exactly where it belongs.

The key insight: we trade *memory* for *speed*.

### Implementation

First, import what we need:

```python
import numpy as np
from collections import defaultdict
```

Now let's build our hash function:

```python
def hash_function(key: str, table_size: int) -> int:
    """Convert a string key to an array index."""
    ascii_sum = sum(ord(char) for char in key)
    return ascii_sum % table_size

# Demonstrate with concrete example
books = ["Moby Dick", "1984", "Dune"]
for book in books:
    print(f"'{book}' → shelf {hash_function(book, 10)}")
```
```

### Math Explanation

Conceptual explanation first, then LaTeX:

```markdown
The **collision probability** grows as the table fills. If we have $n$ items
in a table of size $m$:

$$P(\text{collision}) = \frac{n}{m}$$

This is why hash tables typically resize when they're about 70% full.
```

## Companion Notebook Patterns (Python Books)

For Python books, each chapter has a companion `.ipynb` file. **Each cell must run independently**:

```python
# Cell 1: Basic example (self-contained)
import numpy as np
from collections import defaultdict

def hash_function(key: str, table_size: int) -> int:
    """Convert a string key to an array index."""
    ascii_sum = sum(ord(char) for char in key)
    return ascii_sum % table_size

books = ["Moby Dick", "1984", "Dune"]
for book in books:
    print(f"'{book}' → shelf {hash_function(book, 10)}")
```

```python
# Cell 2: Visualization (must redefine function and data)
import matplotlib.pyplot as plt

def hash_function(key: str, table_size: int) -> int:
    return sum(ord(char) for char in key) % table_size

books = ["Moby Dick", "1984", "Dune"]
indices = [hash_function(book, 10) for book in books]

fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(range(10), [indices.count(i) for i in range(10)])
ax.set_xlabel("Shelf Number")
ax.set_ylabel("Books Assigned")
ax.set_title("Hash Distribution Across Shelves")
plt.show()
```

## Workflow

1. **Research** if uncertain about any topic
2. **Create book directory** and plan outline
3. **Spawn parallel agents** to write chapters (Markdown + notebooks for Python)
4. **Spawn verification agents** to review Markdown first, then notebooks
5. **Format code** with ruff

## Step 1: Research

Before planning, use WebSearch and WebFetch to consult official documentation when uncertain about APIs, best practices, or version-specific behavior.

## Step 2: Create Book Directory and Plan Outline

**Create the book directory structure:**

```bash
mkdir -p ./[book-slug]/data ./[book-slug]/output
```

**Then create the outline:**

```
# Book: [Title]
Directory: ./[book-slug]/
Language: [Python/JavaScript/etc. or "Conceptual" if no code]

## Overview
[2-3 sentences: what the reader will learn and build]

## Prerequisites
[List assumed knowledge]

## Chapter 1: [Title]
- Learning objective: [specific outcome]
- Key concepts: [list 3-5 topics]
- Markdown: 01_[slug].md
- Notebook: 01_[slug].ipynb (Python only)
- Data: data/chapter_01/ (if needed)
- Output: output/chapter_01/ (if needed)
- Dependencies: none

## Chapter 2: [Title]
- Learning objective: [specific outcome]
- Key concepts: [list 3-5 topics]
- Markdown: 02_[slug].md
- Notebook: 02_[slug].ipynb (Python only)
- Data: data/chapter_02/ (if needed)
- Output: output/chapter_02/ (if needed)
- Dependencies: Chapter 1

...
```

**Guidelines:**
- Order chapters from foundational → advanced
- Use numbered filenames: `01_intro.md`, `02_basics.md`, etc.
- Note if book is Python (needs notebooks) or other language (Markdown only)

## Step 3: Parallel Chapter Writing

Spawn Task agents to write chapters. Each agent writes both Markdown and notebook (for Python).

**Launch independent chapters in a single message:**

```
Use Task tool with subagent_type="general-purpose" for each chapter:

"Write a book chapter and save it to the specified path.

CHAPTER ASSIGNMENT:
- Title: [from outline]
- Learning objective: [from outline]
- Key concepts: [from outline]
- Language: [Python/other]
- Chapter number: [N]
- Save Markdown to: ./[book-slug]/[filename].md
- Save Notebook to: ./[book-slug]/[filename].ipynb (Python only)
- Data folder: ./[book-slug]/data/chapter_[N]/ (if chapter needs data files)
- Output folder: ./[book-slug]/output/chapter_[N]/ (for notebook outputs)

WRITING GUIDELINES (read references/chapter-guidelines.md):
- Explain intuition before formalism (Feynman style)
- Use plain English with analogies
- Structure: Learning Objective → Basic → Intermediate → Advanced → Challenge Exercise
- No 'trivially' or 'it is easy to see'

MARKDOWN FILE:
- Write clean prose with code blocks
- No need to duplicate imports—assume sequential reading
- Focus on explanation and narrative flow
- Reference data files as ./data/chapter_[N]/filename

NOTEBOOK FILE (Python only):
- CRITICAL: Each code cell must run independently
  - Include all imports in every cell
  - Redefine functions and data as needed
  - No reliance on variables from earlier cells
- Mirror the Markdown structure
- Include visualizations with labels and titles
- Load data from ./data/chapter_[N]/
- Save outputs (plots, models, results) to ./output/chapter_[N]/
- Create data/output directories if needed before saving

Save completed files to: ./[book-slug]/"
```

**Parallelization:**
- Launch all independent chapters together in one message
- Wait for dependencies before launching dependent chapters

## Step 4: Verification

After writing agents complete, spawn **verification agents for each chapter**. Verify Markdown first, then notebooks.

```
Use Task tool with subagent_type="general-purpose":

"Review and correct the chapter files at ./[book-slug]/[chapter-prefix].

VERIFICATION ORDER:
1. First verify the MARKDOWN file ([chapter].md)
2. Then verify the NOTEBOOK file ([chapter].ipynb) if it exists

MARKDOWN VERIFICATION CHECKLIST:
1. Verify structure: Learning Objective, Basic, Intermediate, Advanced, Challenge Exercise
2. Check Feynman style: analogies before formalism, no jargon without explanation
3. Verify no 'trivially' or 'it is easy to see'
4. Code blocks are properly formatted
5. Logical flow from basic to advanced

NOTEBOOK VERIFICATION CHECKLIST (do NOT execute cells):
1. CRITICAL: Verify each code cell is independently runnable
   - All imports present in every cell that needs them
   - Functions/classes redefined if used from earlier cells
   - Data redefined if used from earlier cells
   - No undefined variables from previous cells
2. Verify notebook mirrors Markdown structure
3. Check visualizations have axis labels and titles
4. Verify data paths use ./data/chapter_[N]/
5. Verify output paths use ./output/chapter_[N]/

INSTRUCTIONS:
- Read references/chapter-guidelines.md for style requirements
- Fix any issues found directly in the files
- Save corrections to the same files
- Report: what was checked (Markdown then Notebook), what was fixed"
```

**Run verification agents in parallel** for all chapters.

## Step 5: Format Code with Ruff

After all agents complete, format code:

```bash
# Format notebooks
ruff format ./[book-slug]/*.ipynb

# Check Markdown code blocks (manual review if needed)
```
