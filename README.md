# Weni MCP Server

MCP (Model Context Protocol) server that exposes tools to query the Weni Insights Engine API.

## Available Tools

### `get_conversation_totals`

Fetches total conversation metrics for a Weni project within a given period.

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `project_uuid` | string | Weni project UUID |
| `start_date` | string | Start date (YYYY-MM-DD) |
| `end_date` | string | End date (YYYY-MM-DD) |

**Returns:** total conversations, resolved, unresolved, and transferred to human support.

## Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation)

## Setup

1. Clone the repository:

```bash
git clone <repo-url>
cd v1_mcp
```

2. Install dependencies:

```bash
poetry install
```

3. Create a `.env` file in the project root:

```env
WENI_API_TOKEN=your_token_here
```

4. Test the server:

```bash
poetry run python server.py
```

The server runs over stdio and waits for commands (no visible output). Press `Ctrl+C` to stop.

## Cursor Configuration

Create the file `.cursor/mcp.json` in the project root:

```json
{
    "mcpServers": {
        "weni-insights": {
            "command": "poetry",
            "args": ["run", "python", "server.py"],
            "cwd": "/path/to/v1_mcp",
            "env": {
                "WENI_API_TOKEN": "your_token_here"
            }
        }
    }
}
```

> **Note (WSL):** if running on WSL from Windows, use `wsl` as the command:
>
> ```json
> {
>     "mcpServers": {
>         "weni-insights": {
>             "command": "wsl",
>             "args": [
>                 "bash", "-c",
>                 "cd /mnt/c/path/to/v1_mcp && /home/your_user/.local/bin/poetry run python server.py"
>             ],
>             "env": {
>                 "WENI_API_TOKEN": "your_token_here"
>             }
>         }
>     }
> }
> ```

After configuring, reload Cursor (`Ctrl+Shift+P` → "Developer: Reload Window") and enable the server in **Settings → Tools & MCP**.
