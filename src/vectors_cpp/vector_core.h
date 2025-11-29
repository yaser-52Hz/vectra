#ifndef VECTOR_CORE_H
#define VECTOR_CORE_H

#include <vector>
#include <cmath>
#include <stdexcept>
#include <initializer_list>

namespace vectors {

/**
 * VectorND - Core n-dimensional vector implementation for high-performance operations
 * 
 * This class provides the fundamental n-dimensional vector operations that will be
 * exposed to Python through pybind11 bindings.
 */
class VectorND {
public:
    // Constructors
    VectorND();
    VectorND(size_t dimensions);
    VectorND(size_t dimensions, double value);
    VectorND(const std::vector<double>& data);
    VectorND(std::initializer_list<double> data);
    VectorND(const VectorND& other);
    VectorND(VectorND&& other) noexcept;
    
    // Assignment
    VectorND& operator=(const VectorND& other);
    VectorND& operator=(VectorND&& other) noexcept;
    
    // Destructor
    ~VectorND() = default;
    
    // Accessors
    size_t size() const { return data_.size(); }
    size_t dimensions() const { return data_.size(); }
    
    double get(size_t index) const;
    void set(size_t index, double value);
    double operator[](size_t index) const;
    double& operator[](size_t index);
    
    // Convenience accessors for 2D/3D vectors (for backward compatibility)
    double x() const;
    double y() const;
    double z() const;
    void set_x(double x);
    void set_y(double y);
    void set_z(double z);
    
    // Access underlying data
    const std::vector<double>& data() const { return data_; }
    std::vector<double>& data() { return data_; }
    
    // Mathematical operations
    VectorND operator+(const VectorND& other) const;
    VectorND operator-(const VectorND& other) const;
    VectorND operator*(double scalar) const;
    VectorND operator/(double scalar) const;
    VectorND operator-() const; // Negation
    
    bool operator==(const VectorND& other) const;
    bool operator!=(const VectorND& other) const;
    
    // Vector operations
    double magnitude() const;
    double magnitude_squared() const;
    VectorND normalize() const;
    double dot(const VectorND& other) const;
    
    // Cross product (only for 3D vectors)
    VectorND cross(const VectorND& other) const;
    bool is_3d() const { return data_.size() == 3; }
    
    // Distance and angle
    double distance(const VectorND& other) const;
    double distance_squared(const VectorND& other) const;
    double angle_between(const VectorND& other) const;
    
    // Advanced operations
    VectorND projection(const VectorND& onto) const;
    VectorND reflection(const VectorND& normal) const;
    
    // Rotation using Rodrigues' rotation formula (only for 3D vectors)
    VectorND rotate(const VectorND& axis, double angle) const;
    
    // Additional n-dimensional operations
    VectorND lerp(const VectorND& other, double t) const;
    double cosine_similarity(const VectorND& other) const;
    VectorND clamp(double min_val, double max_val) const;
    
    // Resize
    void resize(size_t new_size);
    void resize(size_t new_size, double value);
    
private:
    std::vector<double> data_;
    
    // Helper to check dimension compatibility
    void check_dimensions(const VectorND& other, const char* operation) const;
};

// Non-member functions for batch operations
void batch_add(VectorND* v1, VectorND* v2, VectorND* result, size_t count);
void batch_dot_product(const VectorND* v1, const VectorND* v2, double* result, size_t count);
VectorND centroid(const VectorND* vectors, size_t count);
VectorND weighted_average(const VectorND* vectors, const double* weights, size_t count);

// Element-wise operations
VectorND element_wise_multiply(const VectorND& v1, const VectorND& v2);
VectorND element_wise_divide(const VectorND& v1, const VectorND& v2);
double sum(const VectorND& v);
double max(const VectorND& v);
double min(const VectorND& v);
double mean(const VectorND& v);

} // namespace vectors

#endif // VECTOR_CORE_H

