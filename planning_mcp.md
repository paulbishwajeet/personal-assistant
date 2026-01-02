# Planning MCP (Stateful)

## Purpose
Store and manage tasks/goals/reflections across conversations.

## Storage
SQLite (local file) for v1.

## Entity: Task
Fields:
- id: string (UUID)
- title: string
- description: string (optional)
- status: string ("pending" | "done")
- created_at: string (ISO-8601)
- updated_at: string (ISO-8601)
- tags: list[string] (optional)

## Tools
- create_task: creates a new pending task and returns the full task object.
- list_tasks: returns a list of tasks, filtered by status if provided.
- update_task: updates an existing task and returns the full task object.
- complete_task: marks a task as done and returns the full task object.

## Error Rules
- If task id not found: return a clear error message.
- If invalid status: return a clear error message.


### create_task
Inputs:
- title: string
- description: string (optional)
- tags: list[string] (optional)

Behavior:
- Creates a new task with status set to "pending".
- Generates a unique task id.
- Sets created_at and updated_at timestamps.
- Stores the task persistently.

Returns:
- The full created task object.

Errors:
- If title is missing or empty: return a clear error message.

