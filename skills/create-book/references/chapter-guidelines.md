# Chapter Writing Guidelines

Follow these guidelines when writing book chapters (Markdown files and companion notebooks).

## Core Philosophy

**The Feynman Method:**
- Explain core intuition as if to a bright child before mathematics or code
- Use plain English; define technical terms immediately with common-sense analogies
- Acknowledge when concepts are "weird" or counter-intuitive—never say "trivially"

**The O'Reilly Standard:**
- Problem-solution oriented sections
- Production-ready, PEP 8 compliant code with comments
- Clear progression from basic to advanced

## Chapter Structure

Every chapter follows this format with **progressive difficulty**:

```
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

## Progressive Difficulty Guidelines

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

Each section must reference concepts from previous sections.

## Markdown File Guidelines

**Imports and code flow:**
- No need to duplicate imports—assume sequential reading
- Introduce imports when first needed, then use freely afterward
- Focus on explanation and narrative flow

**Narrative cells:**
Build intuition before code:

```markdown
## The Core Idea

Imagine you're organizing a library. **A hash table** is like giving every book
a specific shelf number based on its title—you don't search; you calculate
exactly where it belongs.

The key insight: we trade *memory* for *speed*.
```

**Code blocks:**
- Clean, well-commented code
- PEP 8 compliant for Python
- Explain what the code does before showing it

**Math explanations:**
Conceptual explanation first, then LaTeX:

```markdown
The **collision probability** grows as the table fills. If we have $n$ items
in a table of size $m$:

$$P(\text{collision}) = \frac{n}{m}$$
```

## Data and Output Directories

**Data files (`./data/chapter_<num>/`):**
- Store input data (CSV, JSON, images, etc.) used by the chapter
- Create directory before saving: `os.makedirs("./data/chapter_01", exist_ok=True)`
- Reference in code as `./data/chapter_01/filename.csv`

**Output files (`./output/chapter_<num>/`):**
- Store notebook-generated outputs (plots, models, results)
- Create directory before saving: `os.makedirs("./output/chapter_01", exist_ok=True)`
- Save outputs to `./output/chapter_01/figure.png`

Example:
```python
import os
import pandas as pd
import matplotlib.pyplot as plt

# Create output directory
os.makedirs("./output/chapter_01", exist_ok=True)

# Load data
df = pd.read_csv("./data/chapter_01/sales.csv")

# Save output
fig, ax = plt.subplots()
ax.plot(df["date"], df["revenue"])
fig.savefig("./output/chapter_01/revenue_plot.png")
```

## Companion Notebook Guidelines (Python Only)

For Python books, create a companion `.ipynb` file that mirrors the Markdown chapter.

**CRITICAL: Each cell must run independently** without executing previous cells:

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

**Why independent cells?**
- Readers can run any cell without running the whole notebook
- Easier to debug and test individual concepts
- More robust for teaching—no hidden state issues

## Quality Checklist

### Markdown File
- [ ] Learning objective is specific and measurable
- [ ] Every concept has an analogy before formalism
- [ ] Code blocks are properly formatted
- [ ] Logical flow from basic to advanced
- [ ] No "trivially" or "it is easy to see"

### Companion Notebook (Python only)
- [ ] Mirrors the Markdown structure
- [ ] **Each code cell runs independently:**
  - [ ] All imports included in every cell
  - [ ] Functions/data redefined when needed
  - [ ] No undefined variables from previous cells
- [ ] Visualizations have axis labels and titles
- [ ] Challenge exercise is included
- [ ] Data loaded from `./data/chapter_<num>/`
- [ ] Outputs saved to `./output/chapter_<num>/`
