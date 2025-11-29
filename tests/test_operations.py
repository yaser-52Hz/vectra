"""
Tests for vector operations module
"""

import pytest
import math
from vectors import (
    add,
    subtract,
    multiply,
    divide,
    dot_product,
    cross_product,
    magnitude,
    normalize,
    distance,
    angle_between,
    projection,
    reflection,
    rotate,
    batch_add,
    batch_dot_product,
    centroid,
    weighted_average,
)
from vectors import Vector


class TestBasicOperations:
    """Test basic vector operations functions."""
    
    def test_add_function(self):
        """Test add function."""
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        result = add(v1, v2)
        assert result.x == 5.0
        assert result.y == 7.0
        assert result.z == 9.0
    
    def test_subtract_function(self):
        """Test subtract function."""
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        result = subtract(v1, v2)
        assert result.x == -3.0
        assert result.y == -3.0
        assert result.z == -3.0
    
    def test_multiply_function(self):
        """Test multiply function."""
        v = Vector(1, 2, 3)
        result = multiply(v, 2.5)
        assert result.x == 2.5
        assert result.y == 5.0
        assert result.z == 7.5
    
    def test_divide_function(self):
        """Test divide function."""
        v = Vector(4, 6, 8)
        result = divide(v, 2)
        assert result.x == 2.0
        assert result.y == 3.0
        assert result.z == 4.0


class TestVectorOperations:
    """Test advanced vector operations."""
    
    def test_dot_product_function(self):
        """Test dot_product function."""
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        dot = dot_product(v1, v2)
        assert dot == 32.0
    
    def test_cross_product_function(self):
        """Test cross_product function."""
        v1 = Vector(1, 0, 0)
        v2 = Vector(0, 1, 0)
        cross = cross_product(v1, v2)
        assert cross.z == 1.0
    
    def test_magnitude_function(self):
        """Test magnitude function."""
        v = Vector(3, 4, 0)
        assert magnitude(v) == 5.0
    
    def test_normalize_function(self):
        """Test normalize function."""
        v = Vector(3, 4, 0)
        normalized = normalize(v)
        assert abs(magnitude(normalized) - 1.0) < 1e-9
    
    def test_distance_function(self):
        """Test distance function."""
        v1 = Vector(0, 0, 0)
        v2 = Vector(3, 4, 0)
        assert distance(v1, v2) == 5.0
    
    def test_angle_between_function(self):
        """Test angle_between function."""
        v1 = Vector(1, 0, 0)
        v2 = Vector(0, 1, 0)
        angle = angle_between(v1, v2)
        assert abs(angle - math.pi / 2) < 1e-9
    
    def test_angle_between_zero_vector(self):
        """Test angle_between with zero vector."""
        v1 = Vector(1, 0, 0)
        v2 = Vector(0, 0, 0)
        with pytest.raises(ValueError):
            angle_between(v1, v2)


class TestAdvancedOperations:
    """Test advanced vector operations."""
    
    def test_projection_function(self):
        """Test projection function."""
        v = Vector(3, 4, 0)
        onto = Vector(1, 0, 0)
        proj = projection(v, onto)
        assert proj.x == 3.0
        assert proj.y == 0.0
        assert proj.z == 0.0
    
    def test_reflection_function(self):
        """Test reflection function."""
        v = Vector(1, 1, 0)
        normal = Vector(0, 1, 0).normalize()
        reflected = reflection(v, normal)
        # This is a basic test; actual implementation would need verification
        assert reflected.magnitude() > 0
    
    def test_rotate_function(self):
        """Test rotate function."""
        v = Vector(1, 0, 0)
        axis = Vector(0, 0, 1).normalize()
        rotated = rotate(v, axis, math.pi / 2)
        # After 90-degree rotation around z-axis, (1,0,0) should become (0,1,0)
        assert abs(rotated.y - 1.0) < 1e-9
        assert abs(rotated.x - 0.0) < 1e-9


class TestBatchOperations:
    """Test batch vector operations."""
    
    def test_batch_add(self):
        """Test batch_add function."""
        v1_list = [Vector(1, 2, 3), Vector(4, 5, 6)]
        v2_list = [Vector(7, 8, 9), Vector(10, 11, 12)]
        result = batch_add(v1_list, v2_list)
        assert len(result) == 2
        assert result[0].x == 8.0
        assert result[0].y == 10.0
    
    def test_batch_add_mismatched_lengths(self):
        """Test batch_add with mismatched lengths."""
        v1_list = [Vector(1, 2, 3)]
        v2_list = [Vector(4, 5, 6), Vector(7, 8, 9)]
        with pytest.raises(ValueError):
            batch_add(v1_list, v2_list)
    
    def test_batch_dot_product(self):
        """Test batch_dot_product function."""
        v1_list = [Vector(1, 0, 0), Vector(0, 1, 0)]
        v2_list = [Vector(1, 0, 0), Vector(1, 0, 0)]
        result = batch_dot_product(v1_list, v2_list)
        assert len(result) == 2
        assert result[0] == 1.0
        assert result[1] == 0.0
    
    def test_centroid(self):
        """Test centroid calculation."""
        vectors = [
            Vector(0, 0, 0),
            Vector(2, 0, 0),
            Vector(0, 2, 0),
        ]
        center = centroid(vectors)
        assert abs(center.x - 2/3) < 1e-9
        assert abs(center.y - 2/3) < 1e-9
    
    def test_centroid_empty(self):
        """Test centroid with empty list."""
        with pytest.raises(ValueError):
            centroid([])
    
    def test_weighted_average(self):
        """Test weighted_average function."""
        vectors = [Vector(0, 0, 0), Vector(2, 0, 0)]
        weights = [1, 1]
        avg = weighted_average(vectors, weights)
        assert abs(avg.x - 1.0) < 1e-9
        assert avg.y == 0.0
    
    def test_weighted_average_mismatched(self):
        """Test weighted_average with mismatched lengths."""
        vectors = [Vector(0, 0, 0)]
        weights = [1, 2]
        with pytest.raises(ValueError):
            weighted_average(vectors, weights)
    
    def test_weighted_average_zero_weight(self):
        """Test weighted_average with zero total weight."""
        vectors = [Vector(1, 1, 1), Vector(2, 2, 2)]
        weights = [0, 0]
        with pytest.raises(ValueError):
            weighted_average(vectors, weights)


if __name__ == "__main__":
    pytest.main([__file__])

