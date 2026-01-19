# 🚀 VYNO: Autonomous Driving Ecosystem

VYNO is a modular autonomous agent ecosystem developed by **Eray Özer**, designed for the CARLA Simulator. This repository serves as a technical masterclass for architecting autonomous systems from the ground up, focusing on engineering discipline and fail-safe logic.

---

## 📂 Project Structure

Following a professional engineering approach, the repository is organized into progressive development modules:

- **`01-Environment-Setup`**: Infrastructure, dependency management, and Dockerization.
- **`02-Perception-Layer`**: Lidar and camera data processing (Sensor Fusion logic).
- **`03-The-Orchestrator`**: The central control loop, task synchronization, and AI decision logic.
- **`04-Healer-Safety-System`**: The "Immune System" - Emergency protocols and health monitoring.
- **`05-Advanced-Swarm-Logic`**: Blueprints for V2X (Vehicle-to-Everything) and decentralized coordination.

---

## 🧠 Core Technical Logic

### 📡 Perception & Lidar Handling

In Module 02, we process raw Lidar point clouds to determine the distance to the nearest obstacle. The system filters points in the forward direction ($X > 0$) and calculates safety margins to prevent collisions in dynamic environments.

### 🛡️ The Healer (Safety Layer)

The "Healer" mechanism ensures system immunity. It acts as a high-priority watchdog that continuously monitors sensor integrity and overrides AI commands if the distance to an obstacle falls below a predefined safety threshold ($d < d_{safe}$).

---

## 🛠️ Prerequisites

Before running the system, ensure you have:

- **CARLA Simulator** (0.9.12 or later recommended).
- **Python 3.8+**
- **NVIDIA GPU** with at least 4GB VRAM (for real-time simulation).
- **Docker & Docker Compose** (Optional but recommended).

---

## 🚀 Execution Guide

### 1. Start CARLA Server

First, launch your CARLA simulator server.

### 2. Install Dependencies (Local Setup)

```bash
pip install -r requirements.txt
```
