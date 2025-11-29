"""
Tests for the Vector class and basic operations
"""

import pytest
from vectors import Vector


class TestVectorInitialization:
    """Test Vector initialization and basic properties."""
    
    def test_default_initialization(self):
        """Test creating a vector with default values."""
        v = Vector(0, 0, 0)
        assert v.x == 0.0
        assert v.y == 0.0
        assert v.z == 0.0
    
    def test_2d_vector(self):
        """Test creating a 2D vector."""
        v = Vector(1, 2)
        assert v.x == 1.0
        assert v.y == 2.0
        assert v.z == 0.0
    
    def test_3d_vector(self):
        """Test creating a 3D vector."""
        v = Vector(1, 2, 3)
        assert v.x == 1.0
        assert v.y == 2.0
        assert v.z == 3.0
    
    def test_from_list(self):
        """Test creating a vector from a list."""
        v = Vector.from_list([1, 2, 3])
        assert v.x == 1.0
        assert v.y == 2.0
        assert v.z == 3.0
        
        v2d = Vector.from_list([4, 5])
        assert v2d.x == 4.0
        assert v2d.y == 5.0
        assert v2d.z == 0.0
    
    def test_from_list_invalid(self):
        """Test that invalid list raises an error."""
        with pytest.raises(ValueError):
            Vector.from_list([1])
        with pytest.raises(ValueError):
            Vector.from_list([1, 2, 3, 4])


class TestVectorOperations:
    """Test basic vector operations."""
    
    def test_addition(self):
        """Test vector addition."""
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        result = v1 + v2
        assert result.x == 5.0
        assert result.y == 7.0
        assert result.z == 9.0
    
    def test_subtraction(self):
        """Test vector subtraction."""
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        result = v1 - v2
        assert result.x == -3.0
        assert result.y == -3.0
        assert result.z == -3.0
    
    def test_scalar_multiplication(self):
        """Test scalar multiplication."""
        v = Vector(1, 2, 3)
        result = v * 2
        assert result.x == 2.0
        assert result.y == 4.0
        assert result.z == 6.0
        
        # Test reverse multiplication
        result2 = 3 * v
        assert result2.x == 3.0
        assert result2.y == 6.0
        assert result2.z == 9.0
    
    def test_scalar_division(self):
        """Test scalar division."""
        v = Vector(4, 6, 8)
        result = v / 2
        assert result.x == 2.0
        assert result.y == 3.0
        assert result.z == 4.0
    
    def test_division_by_zero(self):
        """Test that division by zero raises an error."""
        v = Vector(1, 2, 3)
        with pytest.raises(ValueError):
            v / 0
    
    def test_negation(self):
        """Test vector negation."""
        v = Vector(1, 2, 3)
        neg = -v
        assert neg.x == -1.0
        assert neg.y == -2.0
        assert neg.z == -3.0
    
    def test_equality(self):
        """Test vector equality."""
        v1 = Vector(1, 2, 3)
        v2 = Vector(1, 2, 3)
        v3 = Vector(1, 2, 4)
        assert v1 == v2
        assert v1 != v3


class TestVectorMethods:
    """Test vector methods."""
    
    def test_magnitude(self):
        """Test magnitude calculation."""
        v = Vector(3, 4, 0)
        assert v.magnitude() == 5.0
        
        v3d = Vector(1, 2, 2)
        assert v3d.magnitude() == 3.0
    
    def test_normalize(self):
        """Test vector normalization."""
        v = Vector(3, 4, 0)
        normalized = v.normalize()
        assert abs(normalized.magnitude() - 1.0) < 1e-9
    
    def test_normalize_zero_vector(self):
        """Test that normalizing zero vector raises an error."""
        v = Vector(0, 0, 0)
        with pytest.raises(ValueError):
            v.normalize()
    
    def test_dot_product(self):
        """Test dot product."""
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        dot = v1.dot(v2)
        assert dot == 32.0  # 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
    
    def test_cross_product(self):
        """Test cross product."""
        v1 = Vector(1, 0, 0)
        v2 = Vector(0, 1, 0)
        cross = v1.cross(v2)
        assert cross.x == 0.0
        assert cross.y == 0.0
        assert cross.z == 1.0
    
    def test_conversion_methods(self):
        """Test conversion to list and tuple."""
        v = Vector(1, 2, 3)
        assert v.to_list() == [1.0, 2.0, 3.0]
        assert v.to_tuple() == (1.0, 2.0, 3.0)


if __name__ == "__main__":
    pytest.main([__file__])

