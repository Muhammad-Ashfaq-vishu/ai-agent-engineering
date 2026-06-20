# Prompt Engineering: Zero-Shot, One-Shot, and Few-Shot Learning

## Overview

I learned three fundamental prompting techniques used with Large Language Models (LLMs): Zero-Shot, One-Shot, and Few-Shot Prompting.

These techniques help guide the model toward producing the desired output by providing different amounts of examples and context.

---

## 1. Zero-Shot Prompting

Zero-Shot Prompting means giving the model a task without providing any examples.

### Example

**Prompt:**

```text
Write a professional email requesting a meeting with a client.
```

The model relies entirely on its pre-trained knowledge and the instruction provided.

### Use Cases

* Simple tasks
* General question answering
* Summarization
* Content generation

---

## 2. One-Shot Prompting

One-Shot Prompting means providing a single example before asking the model to perform the task.

### Example

**Prompt:**

```text
Example:
Input: hey can we meet tomorrow
Output: Could we schedule a meeting for tomorrow?

Now convert:
Input: send me the report
Output:
```

The model learns the desired pattern from one example.

### Use Cases

* Style transfer
* Text formatting
* Consistent output generation

---

## 3. Few-Shot Prompting

Few-Shot Prompting means providing multiple examples before asking the model to perform the task.

### Example

**Prompt:**

```text
Example 1:
Input: hi
Output: Hello

Example 2:
Input: bye
Output: Goodbye

Example 3:
Input: thanks
Output: Thank you

Now convert:
Input: sorry
Output:
```

The model identifies the pattern from several examples and applies it to the new input.

### Use Cases

* Structured output generation
* Classification tasks
* Data extraction
* Complex formatting requirements

---

## Key Differences

| Technique | Number of Examples | Description                |
| --------- | ------------------ | -------------------------- |
| Zero-Shot | 0                  | Instruction only           |
| One-Shot  | 1                  | One example provided       |
| Few-Shot  | 2 or more          | Multiple examples provided |

---

## Key Takeaway

When building AI applications, start with Zero-Shot Prompting. If the model does not consistently follow the desired format, use One-Shot or Few-Shot Prompting to improve reliability and output quality.

These prompting techniques are commonly used in chatbots, AI agents, RAG systems, and automation workflows.
