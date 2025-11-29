"""
Pytest configuration and fixtures
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path for testing
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture
def sample_vector_2d():
    """Fixture for a 2D vector."""
    from vectors import Vector
    return Vector(3, 4)


@pytest.fixture
def sample_vector_3d():
    """Fixture for a 3D vector."""
    from vectors import Vector
    return Vector(1, 2, 3)


@pytest.fixture
def zero_vector():
    """Fixture for a zero vector."""
    from vectors import Vector
    return Vector(0, 0, 0)


@pytest.fixture
def unit_vector_x():
    """Fixture for unit vector in x direction."""
    from vectors import Vector
    return Vector(1, 0, 0)


@pytest.fixture
def unit_vector_y():
    """Fixture for unit vector in y direction."""
    from vectors import Vector
    return Vector(0, 1, 0)


@pytest.fixture
def unit_vector_z():
    """Fixture for unit vector in z direction."""
    from vectors import Vector
    return Vector(0, 0, 1)

