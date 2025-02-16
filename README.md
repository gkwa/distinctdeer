# distinctdeer

tldr:

1. Read names from a predefined list of names in a Markdown file
2. Allow you to select an available name
3. Automatically mark the selected name as "used" in the source markdown file
4. Copy the selected name to your clipboard for immediate use

## Motivation

When rapidly prototyping and experimenting with new ideas, starting with a clean slate is crucial to keeping a clear head. This tool `distinctdeer,` addresses two key challenges in the iterative development process:

1. The need to eliminate time spent thinking up a project name by quickly fetching it from a predefined list of acceptable names
2. Keeping track of which project names have been used

`distinctdeer` is especially useful when working with AI assistants (like Claude) for project scaffolding, where you want to:

- Start multiple variations of projects with different approaches
- Avoid being encumbered by existing dependencies
- Quickly abandon and restart ideas with a fresh environment
- Maintain a clear separation between different attempts

The name of the project is random and just some unique identifier... like distinctdeer (for example). I don't care what the name is as long as I can quickly generate an empty project quickly.

distinctdeer is better than project, project1, project2-1, etc. `distinctdeer` is just as arbitrary as project1, project2-1, etc. why not make it funner. `distinctdeer` is assumed to be unique and easily searchable.

## Why Arbitrary Names?

The concept of using arbitrary, non-meaningful names has a notable precedent in the webcomic xkcd. As creator Randall Munroe explains, the name "xkcd" itself has no particular significance - it's "simply a four-letter word without a phonetic pronunciation" that he describes as "a treasured and carefully guarded point in the space of four-character strings" [1].

This philosophy of arbitrary naming offers several benefits for development workflows:

1. Mental Clarity - Using meaningless names prevents emotional attachment to projects that may need to be abandoned
2. Rapid Iteration - No time spent brainstorming the "perfect" name for each experiment
3. Equal Status - All projects start as equals, without implied hierarchy or importance
4. Clean Separation - Distinct names prevent confusion between similar iterations
5. Reduced Cognitive Load - One less decision to make when starting a new project

[1] Source: https://en.wikipedia.org/wiki/Xkcd#:~:text=According%20to%20Munroe%2C%20the%20comic's,of%20four%2Dcharacter%20strings%22.

## Commands

Get commands (read-only):

```bash
distinctdeer get used    # List used project names
distinctdeer get unused  # List available project names
distinctdeer get all     # Show all project names
distinctdeer get rand    # Preview a random name without using it
```

Use commands (mark as used):

```bash
distinctdeer use rand           # Get random name and mark as used
distinctdeer use check <name>   # Mark specific name as used
```

Options:

```bash
--path PATH   # Custom markdown file path
--help        # Show help message
```

## Project Names Format

The tool uses a markdown file to track project names. Names are organized into categories and marked with checkboxes and timestamps when used:

```markdown
# Fun Project Names

## Playful & Energetic

- [x] zippypenguin ✅ 2025-02-08
- [ ] bouncyotter
- [x] whistlingtiger ✅ 2025-02-03

## Whimsical & Magical

- [ ] mysticmoth
- [x] dreamydolphin ✅ 2025-02-01
- [ ] starrysloth
```

Features of the naming system:

- Names are organized into themed categories
- Checkbox `[x]` indicates a used name
- ✅ emoji and timestamp track when name was used
- Names follow a descriptive compound format (e.g., `zippypenguin`, `mysticmoth`)

## Workflow Integration

Typical workflow:

1. Need to start a new project variation
2. Run `distinctdeer get rand` to preview a fresh project name
3. If you like it, run `distinctdeer use rand` to get a new name and mark it as used
4. Create new directory using the name (already in clipboard)
5. Use AI assistant (e.g., Claude) to scaffold the new project
6. Iterate on the idea without dependency conflicts

This approach enables rapid prototyping by:

- Eliminating the cognitive load of thinking up project names
- Ensuring each attempt starts clean
- Making it easy to manage multiple variations of similar ideas
- Streamlining the project initialization process

## Usage Examples

```bash
# Get general help
distinctdeer --help

# Get help for 'get' commands
distinctdeer get --help

# Get help for 'use' commands
distinctdeer use --help

# View all used project names
distinctdeer get used

# View available project names
distinctdeer get unused

# Get a random name without using it
distinctdeer get rand

# Get and mark a random name as used
distinctdeer use rand

# Mark a specific name as used
distinctdeer use check cosmic-penguin

# Use custom project names file
distinctdeer --path /path/to/names.md get all
```
