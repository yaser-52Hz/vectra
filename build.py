"""
Build script for the vectors library

This script automates the build process for the C++ extension module.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def build_extensions():
    """Build the C++ extension using pybind11 and setuptools."""
    print("Building vectors library...")
    print("=" * 50)
    
    # Clean previous builds
    if os.path.exists("build"):
        print("Cleaning previous build...")
        shutil.rmtree("build")
    
    if os.path.exists("dist"):
        print("Cleaning previous distribution...")
        shutil.rmtree("dist")
    
    # Remove old .egg-info
    for item in Path(".").glob("*.egg-info"):
        if item.is_dir():
            shutil.rmtree(item)
    
    # Build the extension
    try:
        subprocess.check_call([sys.executable, "setup.py", "build_ext", "--inplace"])
        print("\nBuild completed successfully!")
        print("=" * 50)
        return True
    except subprocess.CalledProcessError as e:
        print(f"\nBuild failed with error: {e}")
        return False


if __name__ == "__main__":
    success = build_extensions()
    sys.exit(0 if success else 1)

