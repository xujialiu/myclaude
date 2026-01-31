# Chapter Writing Guidelines

Follow these guidelines when writing book chapters.

## Core Philosophy

**Feynman Method:**
- Explain intuition as if to a bright child before mathematics or code
- Plain English; define technical terms with common-sense analogies
- Acknowledge when concepts are counter-intuitive—never say "trivially"

**O'Reilly Standard:**
- Problem-solution oriented sections
- Production-ready code
- Clear progression from basic to advanced

## Directory Structure

```
<book>/
├── code/
│   ├── data/01_<chapter_name>/      # Input data
│   ├── output/01_<chapter_name>/    # Code outputs
│   ├── 01_<chapter_name>.ipynb      # Notebook (preferred)
│   └── 01_<chapter_name>/           # Python files (when needed)
│       └── 01_<example_name>.py
└── markdown/
    ├── attachments/                 # Images/figures
    └── 01_<chapter_name>.md         # Markdown files
```

## Code Format Selection

**Use Jupyter notebooks (preferred) for:**
- Interactive code exploration
- Data visualization
- Step-by-step tutorials
- Code with visual outputs

**Use Python files only for:**
- pytest test suites
- CLI applications
- Multi-file modules
- Code requiring specific execution order

## Chapter Structure

```markdown
# Chapter Title

## Learning Objective
[1-2 sentences: what reader will understand/build]

## Basic: [Foundation Concept]
[Core intuition, simplest case, minimal code]

## Intermediate: [Building On Basics]
[Add complexity, handle edge cases, introduce patterns]

## Advanced: [Real-World Application]
[Production concerns, optimization, integration]

## Challenge Exercise
[Hands-on task at intermediate/advanced level]
```

## Progressive Difficulty

**Basic:** Simplest example, toy data, focus on "what" and "why"

**Intermediate:** Realistic complexity, edge cases, configuration options

**Advanced:** Production concerns, optimization, trade-offs

## Figure Handling

Save all code-generated images to `markdown/attachments/`:

```python
import matplotlib.pyplot as plt
import os

# Create attachments directory
os.makedirs("../markdown/attachments", exist_ok=True)

fig, ax = plt.subplots()
ax.plot(data)
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_title("Figure Title")

# Save to attachments
fig.savefig("../markdown/attachments/01_intro_figure1.png", dpi=150, bbox_inches="tight")
plt.close()
```

Link in Markdown:
```markdown
![Revenue over time](./attachments/01_intro_figure1.png)
```

**Naming convention:** `[NN]_[chapter_slug]_[description].png`

## Data and Output Paths

```python
import os
import pandas as pd

# Paths relative to code/ directory
DATA_DIR = "./data/01_intro"
OUTPUT_DIR = "./output/01_intro"
ATTACHMENTS_DIR = "../markdown/attachments"

# Create directories
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ATTACHMENTS_DIR, exist_ok=True)

# Load data
df = pd.read_csv(f"{DATA_DIR}/sales.csv")

# Save outputs (non-figure files)
df.to_csv(f"{OUTPUT_DIR}/processed.csv", index=False)

# Save figures to attachments
fig.savefig(f"{ATTACHMENTS_DIR}/01_intro_sales_chart.png")
```

## Jupyter Notebook Guidelines

**Each cell must run independently:**
- Include all imports in every cell
- Redefine functions/data when needed
- No undefined variables from previous cells

```python
# Cell 1: Basic example (self-contained)
import numpy as np

def hash_function(key: str, table_size: int) -> int:
    return sum(ord(char) for char in key) % table_size

books = ["Moby Dick", "1984", "Dune"]
for book in books:
    print(f"'{book}' → shelf {hash_function(book, 10)}")
```

```python
# Cell 2: Visualization (redefines what it needs)
import matplotlib.pyplot as plt
import os

def hash_function(key: str, table_size: int) -> int:
    return sum(ord(char) for char in key) % table_size

books = ["Moby Dick", "1984", "Dune"]
indices = [hash_function(book, 10) for book in books]

os.makedirs("../markdown/attachments", exist_ok=True)

fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(range(10), [indices.count(i) for i in range(10)])
ax.set_xlabel("Shelf Number")
ax.set_ylabel("Books Assigned")
ax.set_title("Hash Distribution")
fig.savefig("../markdown/attachments/01_hash_distribution.png", dpi=150)
plt.show()
```

## Python File Guidelines (when notebooks unsuitable)

For pytest, CLI tools, or multi-file modules:

```
code/01_testing/
├── 01_test_basics.py
├── 02_test_fixtures.py
└── conftest.py
```

Run with:
```bash
conda activate books
cd code/01_testing
pytest -v
```

## Environment Commands

```bash
# Activate environment
conda activate books

# Install dependencies
uv pip install pandas matplotlib numpy

# Format code
ruff format ./code/
ruff check --fix ./code/

# Run notebook
jupyter nbconvert --execute --inplace ./code/01_intro.ipynb
```

## Quality Checklist

### Markdown
- [ ] Learning objective is specific
- [ ] Every concept has analogy before formalism
- [ ] No "trivially" or "it is easy to see"
- [ ] Figures linked from attachments/

### Notebook
- [ ] Each cell runs independently
- [ ] All visualizations have labels/titles
- [ ] Figures saved to attachments/
- [ ] Data from code/data/[chapter]/
- [ ] Outputs to code/output/[chapter]/

### Python Files
- [ ] Organized in chapter directory
- [ ] Numbered sequentially
- [ ] Tests pass with pytest
- [ ] Formatted with ruff
