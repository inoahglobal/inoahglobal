"""
iNoah System Orchestrator
Starts all iNoah services in the correct order.
"""

import os
import sys
import time
import subprocess
import signal
from pathlib import Path

# Add shared to path
sys.path.insert(0, str(Path(__file__).parent))

from shared import get_config, get_logger, OllamaClient
from shared.config_loader import get_service_config

# Logger
logger = get_logger("orchestrator")

# Service definitions
SERVICES = [
    {
        "name": "serverbridge",
        "path": Path(__file__).parent.parent / "serverbridge-main" / "main.py",
        "port": get_service_config("serverbridge").get("port", 8000),
    },
    {
        "name": "inoahbrain",
        "path": Path(__file__).parent.parent / "inoahbrain" / "main.py",
        "port": get_service_config("inoahbrain").get("port", 8001),
    },
    {
        "name": "inoahphoto",
        "path": Path(__file__).parent.parent / "inoahphoto" / "main.py",
        "port": get_service_config("inoahphoto").get("port", 8002),
    },
]

# Track running processes
processes = []


def check_ollama():
    """Check if Ollama is running and available."""
    logger.info("Checking Ollama availability...")
    client = OllamaClient()
    
    if client.is_available():
        models = client.list_models()
        logger.info(f"Ollama is online. Models available: {', '.join(models) if models else 'none'}")
        
        # Check for required models
        config = get_config()
        required = [
            config.get("ollama", {}).get("models", {}).get("reasoning", "llama3"),
            config.get("ollama", {}).get("models", {}).get("vision", "llava"),
        ]
        
        missing = [m for m in required if m not in models]
        if missing:
            logger.warning(f"Missing models: {', '.join(missing)}")
            logger.warning("Run: ollama pull <model_name>")
        
        return True
    else:
        logger.error("Ollama is not running!")
        logger.error("Start Ollama first: ollama serve")
        return False


def start_service(service: dict) -> subprocess.Popen:
    """Start a single service."""
    name = service["name"]
    script_path = service["path"]
    port = service["port"]
    
    if not script_path.exists():
        logger.error(f"Service script not found: {script_path}")
        return None
    
    logger.info(f"Starting {name} on port {port}...")
    
    # Start the service
    process = subprocess.Popen(
        [sys.executable, str(script_path)],
        cwd=str(script_path.parent),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )
    
    # Give it a moment to start
    time.sleep(1)
    
    if process.poll() is None:
        logger.info(f"{name} started (PID: {process.pid})")
        return process
    else:
        logger.error(f"{name} failed to start")
        return None


def stop_all():
    """Stop all running services."""
    logger.info("Stopping all services...")
    
    for process in processes:
        if process and process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
    
    logger.info("All services stopped.")


def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully."""
    print()  # New line after ^C
    stop_all()
    sys.exit(0)


def main():
    """Main orchestrator entry point."""
    logger.info("=" * 60)
    logger.info("iNoah System Orchestrator")
    logger.info("=" * 60)
    
    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Check Ollama first
    if not check_ollama():
        logger.error("Cannot start without Ollama. Exiting.")
        sys.exit(1)
    
    # Start all services
    logger.info("-" * 60)
    logger.info("Starting services...")
    
    for service in SERVICES:
        process = start_service(service)
        if process:
            processes.append(process)
        else:
            logger.warning(f"Skipping {service['name']} due to startup failure")
    
    # Summary
    logger.info("-" * 60)
    logger.info("iNoah System Status:")
    for service in SERVICES:
        logger.info(f"  {service['name']}: http://localhost:{service['port']}")
    logger.info("-" * 60)
    logger.info("Press Ctrl+C to stop all services")
    
    # Keep running and forward output
    try:
        while True:
            for i, process in enumerate(processes):
                if process and process.poll() is None:
                    # Read and print any output
                    line = process.stdout.readline()
                    if line:
                        print(f"[{SERVICES[i]['name']}] {line.rstrip()}")
                elif process:
                    # Process died
                    logger.warning(f"{SERVICES[i]['name']} stopped unexpectedly")
                    processes[i] = None
            
            # Check if all processes are dead
            if all(p is None or p.poll() is not None for p in processes):
                logger.error("All services have stopped!")
                break
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        pass
    finally:
        stop_all()


if __name__ == "__main__":
    main()

