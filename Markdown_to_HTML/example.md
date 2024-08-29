# Advanced Markdown Example with CSS

This Markdown file demonstrates various Markdown features, enhanced with CSS styling.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Code Blocks](#code-blocks)
3. [Tables](#tables)
4. [Blockquotes](#blockquotes)
5. [Lists](#lists)
6. [Images](#images)
7. [Links](#links)
8. [Footnotes](#footnotes)
9. [Math](#math)
10. [Task Lists](#task-lists)

## Introduction

Markdown is a lightweight markup language that you can use to add formatting elements to plaintext text documents. This example file contains:

- Headers
- Code blocks with syntax highlighting
- Tables
- Blockquotes
- Lists
- Images and Links
- Footnotes
- Math expressions
- Task lists

## Code Blocks

### Python Example

```python
def fibonacci(n):
    """Return the nth Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci(10))  # Output: 55
