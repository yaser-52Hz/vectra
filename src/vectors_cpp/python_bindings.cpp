#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <pybind11/operators.h>
#include "vector_core.h"

namespace py = pybind11;
using namespace vectors;

void init_vector_module(py::module &m) {
    // VectorND class binding
    py::class_<VectorND>(m, "VectorND")
        // Constructors
        .def(py::init<>())
        .def(py::init<size_t>())
        .def(py::init<size_t, double>())
        .def(py::init<const std::vector<double>&>())
        .def(py::init([](py::list data) {
            std::vector<double> vec;
            for (const auto& item : data) {
                vec.push_back(item.cast<double>());
            }
            return VectorND(vec);
        }), "Initializes VectorND from Python list")
        .def(py::init([](py::array_t<double> arr) {
            auto buf = arr.request();
            double* ptr = static_cast<double*>(buf.ptr);
            return VectorND(std::vector<double>(ptr, ptr + buf.size));
        }), "Initializes VectorND from NumPy array")
        
        // Properties
        .def_property_readonly("size", &VectorND::size)
        .def_property_readonly("dimensions", &VectorND::dimensions)
        .def("__len__", &VectorND::size)
        
        // Element access
        .def("__getitem__", [](const VectorND& v, size_t i) {
            if (i >= v.size()) {
                throw py::index_error("Index out of range");
            }
            return v[i];
        })
        .def("__setitem__", [](VectorND& v, size_t i, double val) {
            if (i >= v.size()) {
                throw py::index_error("Index out of range");
            }
            v[i] = val;
        })
        .def("get", &VectorND::get)
        .def("set", &VectorND::set)
        
        // Convenience accessors for x, y, z
        .def_property("x", &VectorND::x, &VectorND::set_x)
        .def_property("y", &VectorND::y, &VectorND::set_y)
        .def_property("z", &VectorND::z, &VectorND::set_z)
        
        // Data access
        .def_property_readonly("data", 
            [](const VectorND& v) {
                return py::cast(v.data());
            }, 
            py::return_value_policy::reference_internal)
        
        // Operators (using pybind11::operators)
        .def(py::self + py::self)
        .def(py::self - py::self)
        .def(py::self * double())
        .def(double() * py::self)
        .def(py::self / double())
        .def(-py::self)
        .def(py::self == py::self)
        .def(py::self != py::self)
        
        // Vector operations
        .def("magnitude", &VectorND::magnitude)
        .def("magnitude_squared", &VectorND::magnitude_squared)
        .def("normalize", &VectorND::normalize)
        .def("dot", &VectorND::dot)
        .def("cross", &VectorND::cross)
        .def("is_3d", &VectorND::is_3d)
        
        // Distance and angle
        .def("distance", &VectorND::distance)
        .def("distance_squared", &VectorND::distance_squared)
        .def("angle_between", &VectorND::angle_between)
        
        // Advanced operations
        .def("projection", &VectorND::projection)
        .def("reflection", &VectorND::reflection)
        .def("rotate", &VectorND::rotate)
        
        // N-dimensional operations
        .def("lerp", &VectorND::lerp)
        .def("cosine_similarity", &VectorND::cosine_similarity)
        .def("clamp", &VectorND::clamp)
        
        // Resize
        .def("resize", py::overload_cast<size_t>(&VectorND::resize))
        .def("resize", py::overload_cast<size_t, double>(&VectorND::resize))
        
        // String representation
        .def("__repr__", [](const VectorND& v) {
            if (v.size() == 0) {
                return "VectorND()";
            }
            std::string result = "VectorND(";
            for (size_t i = 0; i < v.size(); ++i) {
                if (i > 0) result += ", ";
                result += std::to_string(v[i]);
            }
            result += ")";
            return result;
        })
        .def("__str__", [](const VectorND& v) {
            if (v.size() == 0) {
                return "()";
            }
            std::string result = "(";
            for (size_t i = 0; i < v.size(); ++i) {
                if (i > 0) result += ", ";
                result += std::to_string(v[i]);
            }
            result += ")";
            return result;
        });
    
    // Batch operations
    m.def("batch_add", [](const std::vector<VectorND>& v1, 
                          const std::vector<VectorND>& v2) {
        if (v1.size() != v2.size()) {
            throw std::runtime_error("Vector lists must have the same size");
        }
        std::vector<VectorND> result(v1.size());
        batch_add(const_cast<VectorND*>(v1.data()), 
                 const_cast<VectorND*>(v2.data()), 
                 result.data(), v1.size());
        return result;
    }, "Adds corresponding vectors from two lists");
    
    m.def("batch_dot_product", [](const std::vector<VectorND>& v1, 
                                  const std::vector<VectorND>& v2) {
        if (v1.size() != v2.size()) {
            throw std::runtime_error("Vector lists must have the same size");
        }
        std::vector<double> result(v1.size());
        batch_dot_product(v1.data(), v2.data(), result.data(), v1.size());
        return result;
    }, "Calculates dot products for corresponding vector pairs");
    
    m.def("centroid", [](const std::vector<VectorND>& vectors) {
        return centroid(vectors.data(), vectors.size());
    }, "Calculates the centroid of a list of vectors");
    
    m.def("weighted_average", [](const std::vector<VectorND>& vectors, 
                                const std::vector<double>& weights) {
        if (vectors.size() != weights.size()) {
            throw std::runtime_error("Vectors and weights must have the same size");
        }
        return weighted_average(vectors.data(), weights.data(), vectors.size());
    }, "Calculates weighted average of vectors");
    
    // Element-wise operations
    m.def("element_wise_multiply", &element_wise_multiply,
          "Multiply two vectors element-wise");
    m.def("element_wise_divide", &element_wise_divide,
          "Divide two vectors element-wise");
    
    // Statistical operations
    m.def("sum", [](const VectorND& v) { return sum(v); },
          "Calculate sum of vector elements");
    m.def("max", [](const VectorND& v) { return max(v); },
          "Find maximum element");
    m.def("min", [](const VectorND& v) { return min(v); },
          "Find minimum element");
    m.def("mean", [](const VectorND& v) { return mean(v); },
          "Calculate mean of vector elements");
}

PYBIND11_MODULE(_vectors_core, m) {
    m.doc() = "Vector Library - High-performance n-dimensional vector operations (C++ core)";
    m.attr("__version__") = "0.2.0";
    init_vector_module(m);
}
