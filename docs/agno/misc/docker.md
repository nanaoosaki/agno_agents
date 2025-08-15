---
title: Docker
category: misc
source_lines: 73736-73869
line_count: 133
---

# Docker
Source: https://docs.agno.com/tools/toolkits/local/docker



**DockerTools** enable an Agent to interact with Docker containers, images, volumes, and networks.

## Prerequisites

The Docker tools require the `docker` Python package. You'll also need Docker installed and running on your system.

```shell
pip install docker
```

## Example

The following example creates an agent that can manage Docker resources:

```python cookbook/tools/docker_tools.py
import sys
from agno.agent import Agent

try:
    from agno.tools.docker import DockerTools

    docker_tools = DockerTools(
        enable_container_management=True,
        enable_image_management=True,
        enable_volume_management=True,
        enable_network_management=True,
    )

    # Create an agent with Docker tools
    docker_agent = Agent(
        name="Docker Agent",
        instructions=[
            "You are a Docker management assistant that can perform various Docker operations.",
            "You can manage containers, images, volumes, and networks.",
        ],
        tools=[docker_tools],
        show_tool_calls=True,
        markdown=True,
    )

    # Example: List all running Docker containers
    docker_agent.print_response("List all running Docker containers", stream=True)

    # Example: Pull and run an NGINX container
    docker_agent.print_response("Pull the latest nginx image", stream=True)
    docker_agent.print_response("Run an nginx container named 'web-server' on port 8080", stream=True)

except ValueError as e:
    print(f"\n❌ Docker Tool Error: {e}")
    print("\n🔍 Troubleshooting steps:")

    if sys.platform == "darwin":  # macOS
        print("1. Ensure Docker Desktop is running")
        print("2. Check Docker Desktop settings")
        print("3. Try running 'docker ps' in terminal to verify access")

    elif sys.platform == "linux":
        print("1. Check if Docker service is running:")
        print("   systemctl status docker")
        print("2. Make sure your user has permissions to access Docker:")
        print("   sudo usermod -aG docker $USER")

    elif sys.platform == "win32":
        print("1. Ensure Docker Desktop is running")
        print("2. Check Docker Desktop settings")
```

## Toolkit Params

| Parameter                     | Type   | Default | Description                                                      |
| ----------------------------- | ------ | ------- | ---------------------------------------------------------------- |
| `enable_container_management` | `bool` | `True`  | Enables container management functions (list, start, stop, etc.) |
| `enable_image_management`     | `bool` | `True`  | Enables image management functions (pull, build, etc.)           |
| `enable_volume_management`    | `bool` | `False` | Enables volume management functions                              |
| `enable_network_management`   | `bool` | `False` | Enables network management functions                             |

## Toolkit Functions

### Container Management

| Function             | Description                                     |
| -------------------- | ----------------------------------------------- |
| `list_containers`    | Lists all containers or only running containers |
| `start_container`    | Starts a stopped container                      |
| `stop_container`     | Stops a running container                       |
| `remove_container`   | Removes a container                             |
| `get_container_logs` | Retrieves logs from a container                 |
| `inspect_container`  | Gets detailed information about a container     |
| `run_container`      | Creates and starts a new container              |
| `exec_in_container`  | Executes a command inside a running container   |

### Image Management

| Function        | Description                              |
| --------------- | ---------------------------------------- |
| `list_images`   | Lists all images on the system           |
| `pull_image`    | Pulls an image from a registry           |
| `remove_image`  | Removes an image                         |
| `build_image`   | Builds an image from a Dockerfile        |
| `tag_image`     | Tags an image                            |
| `inspect_image` | Gets detailed information about an image |

### Volume Management

| Function         | Description                              |
| ---------------- | ---------------------------------------- |
| `list_volumes`   | Lists all volumes                        |
| `create_volume`  | Creates a new volume                     |
| `remove_volume`  | Removes a volume                         |
| `inspect_volume` | Gets detailed information about a volume |

### Network Management

| Function                            | Description                               |
| ----------------------------------- | ----------------------------------------- |
| `list_networks`                     | Lists all networks                        |
| `create_network`                    | Creates a new network                     |
| `remove_network`                    | Removes a network                         |
| `inspect_network`                   | Gets detailed information about a network |
| `connect_container_to_network`      | Connects a container to a network         |
| `disconnect_container_from_network` | Disconnects a container from a network    |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/docker.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/docker_tools.py)


