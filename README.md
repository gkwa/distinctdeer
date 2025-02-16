-- README.md --

# distinctdeer

A command-line tool to streamline project creation workflow by automating project name management.

## Motivation

When rapidly prototyping and experimenting with new ideas, starting with a clean slate is crucial. This tool addresses two key challenges in the iterative development process:

1. The need to eliminate time spent thinking up project names by quickly fetching them from a predefined list
2. Keeping track of which project names have been used

The tool is especially useful when working with AI assistants (like Claude) for project scaffolding, where you want to:

- Start multiple variations of projects with different approaches
- Avoid being encumbered by existing dependencies
- Quickly abandon and restart ideas with a fresh environment
- Maintain a clear separation between different attempts

The name of the project is random and just some unique identifier... like distinctdeer (for example). I don't care what the name is as long as I can quickly generate an empty project quickly.

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
