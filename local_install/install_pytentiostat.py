import subprocess
import sys


def create_conda_env(env_name):
    """Create a new conda environment."""
    try:
        subprocess.check_call(
            [
                sys.executable,
                "-m",
                "conda",
                "create",
                "-n",
                env_name,
                "python=3.12",
                "-y",
            ]
        )
        print(f"Conda environment '{env_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating conda environment: {e}")
        sys.exit(1)


def install_pytentiostat(env_name):
    """Install pytentiostat in the specified conda environment."""
    try:
        subprocess.check_call(["conda", "activate", env_name])
        subprocess.check_call(["pip", "install", "pytentiostat"])
        print("pytentiostat installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing pytentiostat: {e}")
        sys.exit(1)


def main():
    env_name = "pytentiostat_env"
    create_conda_env(env_name)
    install_pytentiostat(env_name)


if __name__ == "__main__":
    main()
