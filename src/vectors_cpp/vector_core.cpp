#include "vector_core.h"
#include <limits>
#include <algorithm>
#include <numeric>

namespace vectors {

// Constructors
VectorND::VectorND() : data_(3, 0.0) {}

VectorND::VectorND(size_t dimensions) : data_(dimensions, 0.0) {}

VectorND::VectorND(size_t dimensions, double value) : data_(dimensions, value) {}

VectorND::VectorND(const std::vector<double>& data) : data_(data) {}

VectorND::VectorND(std::initializer_list<double> data) : data_(data) {}

VectorND::VectorND(const VectorND& other) : data_(other.data_) {}

VectorND::VectorND(VectorND&& other) noexcept : data_(std::move(other.data_)) {}

// Assignment operators
VectorND& VectorND::operator=(const VectorND& other) {
    if (this != &other) {
        data_ = other.data_;
    }
    return *this;
}

VectorND& VectorND::operator=(VectorND&& other) noexcept {
    if (this != &other) {
        data_ = std::move(other.data_);
    }
    return *this;
}

// Accessors
double VectorND::get(size_t index) const {
    if (index >= data_.size()) {
        throw std::out_of_range("Vector index out of range");
    }
    return data_[index];
}

void VectorND::set(size_t index, double value) {
    if (index >= data_.size()) {
        throw std::out_of_range("Vector index out of range");
    }
    data_[index] = value;
}

double VectorND::operator[](size_t index) const {
    return data_[index];
}

double& VectorND::operator[](size_t index) {
    return data_[index];
}

// Convenience accessors for 2D/3D
double VectorND::x() const { return data_.size() > 0 ? data_[0] : 0.0; }
double VectorND::y() const { return data_.size() > 1 ? data_[1] : 0.0; }
double VectorND::z() const { return data_.size() > 2 ? data_[2] : 0.0; }

void VectorND::set_x(double x) {
    if (data_.size() > 0) data_[0] = x;
}

void VectorND::set_y(double y) {
    if (data_.size() > 1) data_[1] = y;
}

void VectorND::set_z(double z) {
    if (data_.size() > 2) data_[2] = z;
}

// Dimension checking
void VectorND::check_dimensions(const VectorND& other, const char* operation) const {
    if (data_.size() != other.data_.size()) {
        throw std::runtime_error(
            std::string("Dimension mismatch in ") + operation + 
            ": " + std::to_string(data_.size()) + 
            " vs " + std::to_string(other.data_.size())
        );
    }
}

// Arithmetic operations
VectorND VectorND::operator+(const VectorND& other) const {
    check_dimensions(other, "addition");
    VectorND result(data_.size());
    for (size_t i = 0; i < data_.size(); ++i) {
        result.data_[i] = data_[i] + other.data_[i];
    }
    return result;
}

VectorND VectorND::operator-(const VectorND& other) const {
    check_dimensions(other, "subtraction");
    VectorND result(data_.size());
    for (size_t i = 0; i < data_.size(); ++i) {
        result.data_[i] = data_[i] - other.data_[i];
    }
    return result;
}

VectorND VectorND::operator*(double scalar) const {
    VectorND result(data_.size());
    for (size_t i = 0; i < data_.size(); ++i) {
        result.data_[i] = data_[i] * scalar;
    }
    return result;
}

VectorND VectorND::operator/(double scalar) const {
    if (scalar == 0.0) {
        throw std::runtime_error("Division by zero");
    }
    VectorND result(data_.size());
    for (size_t i = 0; i < data_.size(); ++i) {
        result.data_[i] = data_[i] / scalar;
    }
    return result;
}

VectorND VectorND::operator-() const {
    VectorND result(data_.size());
    for (size_t i = 0; i < data_.size(); ++i) {
        result.data_[i] = -data_[i];
    }
    return result;
}

bool VectorND::operator==(const VectorND& other) const {
    if (data_.size() != other.data_.size()) return false;
    const double eps = 1e-9;
    for (size_t i = 0; i < data_.size(); ++i) {
        if (std::abs(data_[i] - other.data_[i]) >= eps) {
            return false;
        }
    }
    return true;
}

bool VectorND::operator!=(const VectorND& other) const {
    return !(*this == other);
}

// Vector operations
double VectorND::magnitude() const {
    if (data_.empty()) return 0.0;
    double sum_sq = 0.0;
    for (double val : data_) {
        sum_sq += val * val;
    }
    return std::sqrt(sum_sq);
}

double VectorND::magnitude_squared() const {
    if (data_.empty()) return 0.0;
    double sum_sq = 0.0;
    for (double val : data_) {
        sum_sq += val * val;
    }
    return sum_sq;
}

VectorND VectorND::normalize() const {
    double mag = magnitude();
    if (mag < std::numeric_limits<double>::epsilon()) {
        throw std::runtime_error("Cannot normalize zero vector");
    }
    return *this / mag;
}

double VectorND::dot(const VectorND& other) const {
    check_dimensions(other, "dot product");
    double result = 0.0;
    for (size_t i = 0; i < data_.size(); ++i) {
        result += data_[i] * other.data_[i];
    }
    return result;
}

VectorND VectorND::cross(const VectorND& other) const {
    if (data_.size() != 3 || other.data_.size() != 3) {
        throw std::runtime_error("Cross product only defined for 3D vectors");
    }
    
    VectorND result(3);
    result[0] = data_[1] * other.data_[2] - data_[2] * other.data_[1];
    result[1] = data_[2] * other.data_[0] - data_[0] * other.data_[2];
    result[2] = data_[0] * other.data_[1] - data_[1] * other.data_[0];
    return result;
}

double VectorND::distance(const VectorND& other) const {
    check_dimensions(other, "distance");
    return (*this - other).magnitude();
}

double VectorND::distance_squared(const VectorND& other) const {
    check_dimensions(other, "distance squared");
    return (*this - other).magnitude_squared();
}

double VectorND::angle_between(const VectorND& other) const {
    check_dimensions(other, "angle calculation");
    double mag1 = this->magnitude();
    double mag2 = other.magnitude();
    
    if (mag1 < std::numeric_limits<double>::epsilon() || 
        mag2 < std::numeric_limits<double>::epsilon()) {
        throw std::runtime_error("Cannot calculate angle with zero vector");
    }
    
    double cos_angle = this->dot(other) / (mag1 * mag2);
    cos_angle = std::max(-1.0, std::min(1.0, cos_angle));
    
    return std::acos(cos_angle);
}

VectorND VectorND::projection(const VectorND& onto) const {
    check_dimensions(onto, "projection");
    double mag2_sq = onto.magnitude_squared();
    
    if (mag2_sq < std::numeric_limits<double>::epsilon()) {
        throw std::runtime_error("Cannot project onto zero vector");
    }
    
    double scalar = this->dot(onto) / mag2_sq;
    return onto * scalar;
}

VectorND VectorND::reflection(const VectorND& normal) const {
    check_dimensions(normal, "reflection");
    return *this - normal * (2.0 * this->dot(normal));
}

VectorND VectorND::rotate(const VectorND& axis, double angle) const {
    if (data_.size() != 3) {
        throw std::runtime_error("Rotation only defined for 3D vectors");
    }
    
    // Rodrigues' rotation formula
    double cos_a = std::cos(angle);
    double sin_a = std::sin(angle);
    
    VectorND term1 = *this * cos_a;
    VectorND term2 = this->cross(axis) * sin_a;
    VectorND term3 = axis * (axis.dot(*this) * (1.0 - cos_a));
    
    return term1 + term2 + term3;
}

VectorND VectorND::lerp(const VectorND& other, double t) const {
    check_dimensions(other, "lerp");
    return *this + (other - *this) * t;
}

double VectorND::cosine_similarity(const VectorND& other) const {
    double mag1 = magnitude();
    double mag2 = other.magnitude();
    
    if (mag1 < std::numeric_limits<double>::epsilon() || 
        mag2 < std::numeric_limits<double>::epsilon()) {
        throw std::runtime_error("Cannot calculate cosine similarity with zero vector");
    }
    
    return dot(other) / (mag1 * mag2);
}

VectorND VectorND::clamp(double min_val, double max_val) const {
    if (min_val > max_val) {
        throw std::runtime_error("Invalid clamp range");
    }
    
    VectorND result(data_.size());
    for (size_t i = 0; i < data_.size(); ++i) {
        result.data_[i] = std::max(min_val, std::min(max_val, data_[i]));
    }
    return result;
}

void VectorND::resize(size_t new_size) {
    resize(new_size, 0.0);
}

void VectorND::resize(size_t new_size, double value) {
    data_.resize(new_size, value);
}

// Non-member batch operations
void batch_add(VectorND* v1, VectorND* v2, VectorND* result, size_t count) {
    for (size_t i = 0; i < count; ++i) {
        result[i] = v1[i] + v2[i];
    }
}

void batch_dot_product(const VectorND* v1, const VectorND* v2, double* result, size_t count) {
    for (size_t i = 0; i < count; ++i) {
        result[i] = v1[i].dot(v2[i]);
    }
}

VectorND centroid(const VectorND* vectors, size_t count) {
    if (count == 0) {
        throw std::runtime_error("Cannot calculate centroid of empty array");
    }
    
    VectorND sum = vectors[0];
    for (size_t i = 1; i < count; ++i) {
        sum = sum + vectors[i];
    }
    return sum / static_cast<double>(count);
}

VectorND weighted_average(const VectorND* vectors, const double* weights, size_t count) {
    if (count == 0) {
        throw std::runtime_error("Cannot calculate weighted average of empty array");
    }
    
    VectorND sum = vectors[0] * weights[0];
    double total_weight = weights[0];
    
    for (size_t i = 1; i < count; ++i) {
        sum = sum + vectors[i] * weights[i];
        total_weight += weights[i];
    }
    
    if (total_weight < std::numeric_limits<double>::epsilon()) {
        throw std::runtime_error("Total weight cannot be zero");
    }
    
    return sum / total_weight;
}

// Element-wise operations
VectorND element_wise_multiply(const VectorND& v1, const VectorND& v2) {
    if (v1.size() != v2.size()) {
        throw std::runtime_error("Dimension mismatch in element-wise multiply");
    }
    
    VectorND result(v1.size());
    for (size_t i = 0; i < v1.size(); ++i) {
        result[i] = v1[i] * v2[i];
    }
    return result;
}

VectorND element_wise_divide(const VectorND& v1, const VectorND& v2) {
    if (v1.size() != v2.size()) {
        throw std::runtime_error("Dimension mismatch in element-wise divide");
    }
    
    VectorND result(v1.size());
    for (size_t i = 0; i < v1.size(); ++i) {
        if (std::abs(v2[i]) < std::numeric_limits<double>::epsilon()) {
            throw std::runtime_error("Division by zero in element-wise divide");
        }
        result[i] = v1[i] / v2[i];
    }
    return result;
}

double sum(const VectorND& v) {
    return std::accumulate(v.data().begin(), v.data().end(), 0.0);
}

double max(const VectorND& v) {
    if (v.size() == 0) {
        throw std::runtime_error("Cannot find max of empty vector");
    }
    return *std::max_element(v.data().begin(), v.data().end());
}

double min(const VectorND& v) {
    if (v.size() == 0) {
        throw std::runtime_error("Cannot find min of empty vector");
    }
    return *std::min_element(v.data().begin(), v.data().end());
}

double mean(const VectorND& v) {
    if (v.size() == 0) {
        throw std::runtime_error("Cannot find mean of empty vector");
    }
    return sum(v) / v.size();
}

} // namespace vectors
