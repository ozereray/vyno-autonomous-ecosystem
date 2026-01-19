# 🛠️ CARLA Simulation Setup Guide

This guide ensures that your local environment is correctly configured to communicate with the VYNO ecosystem. CARLA uses a **Server-Client architecture**, where the simulator acts as the server and VYNO acts as the client.

---

## 1. Prerequisites

Before initializing the VYNO Docker container, ensure your host machine meets these requirements:

- **CARLA Version:** 0.9.12 or 0.9.13 (Recommended).
- **GPU:** NVIDIA GeForce RTX 2060 or higher (with latest drivers).
- **Operating System:** Windows 10/11 or Ubuntu 20.04+.

---

## 2. Installing CARLA

### Local Installation (Windows/Linux)

1. Download the CARLA release from the [Official CARLA GitHub](https://github.com/carla-simulator/carla/releases).
2. Extract the package to a directory (e.g., `C:/CARLA_0.9.13`).
3. (Windows) Run `CarlaUE4.exe` to start the server.
4. (Linux) Run `./CarlaUE4.sh` to start the server.

---

## 3. Configuring the Bridge

The connection between the simulator and VYNO happens via the **CARLA Python API**.

- **Host IP:** Usually `127.0.0.1` (localhost).
- **Port:** Default is `2000`.
- **Traffic Manager Port:** Default is `8000`.

### Troubleshooting Connection

If you see a `Connection Refused` error:

1. Ensure the CARLA simulator is already running _before_ starting the Docker container.
2. Check if your firewall is blocking port `2000`.

---

## 4. Environment Variables

In the VYNO ecosystem, we use a `docker-compose.yml` that expects the host machine's network. Ensure your `network_mode: "host"` is set in the compose file to allow the container to access the CARLA server on your local machine.

---

## 5. Tesla Model 3 Assets

To use the Tesla Model 3 within VYNO:

- The blueprints are part of the standard CARLA blueprint library.
- Ensure the server has loaded `town01` or `town04` for optimal testing conditions.

---

**Next Step:** Proceed to [Module 02: Perception Layer](../02-Perception-Layer/README.md) once the simulation connection is stable.
