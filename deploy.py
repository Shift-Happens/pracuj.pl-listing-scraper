import subprocess
import sys
import os

def run_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        sys.exit(1)

def deploy():
    # Build SAM application
    print("Building SAM application...")
    run_command(["sam", "build"])
    
    # Deploy with guided setup
    print("\nDeploying SAM application...")
    run_command(["sam", "deploy", "--guided"])

if __name__ == "__main__":
    deploy()