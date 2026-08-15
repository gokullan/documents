## LSP (Language Server Protocol)
- Protocol of communication between an editor and the programming-language (for which the editor is used)
- Step-by-step
 - The editor transalates user's commands (eg: go to the definition of this variable / function) into the universal JSON-RPC LSP format
 - There is a server (the language server) that undertands this JSON and responds back in JSON (eg: the definition is on line #20) (the logic of finding out where the definition is, differs based on the language)
 - The editor now does the reverse - it transalates the JSON-response to perform the action requested by the user (eg: moving the cursor to line #20)

## MCP (Model Context Protocol)
- Protocol of communication between an AI-model (base frontier models) and tools (Postgres, Jira, ...) it interacts with
- Step-by-step
  - (Pre-requisite): The tool (eg: Postgres) has its own implementation of the MCP-JSON (which is run in the "MCP server") that actually performs the core-actions (eg: executing a query) 
  - The AI-model parses the user's prompt into one of the commands exposed by the tool's MCP and sends it to the AI-host (like Cline) which then calls the tool's MCP server
  - The MCP-server does the core-action (eg: running a select query on the DB) and returns the results in the same MCP-JSON format back to the AI-host when then forwards it again to the AI-model
  - The AI-model then has the ability to transalate this JSON-response back into natural language
