#include "./potentials.hpp"

double lennardJones (double sig, double eps, double rc, double r) {
    double result;
    if (r > rc) {
        return 0;
    }
    double sr2i = 1. / (sig * sig * r * r);
    double sr6i = sr2i * sr2i * sr2i;
    result = 4 * eps * (sr2i * sr6i - sr6i);
    return result;
}

double harmonic (double k, double r) {
    double result = k * r * r;
    return result;
}

double zero (double r) {
    return 0.0;
}

namespace py = pybind11;

PYBIND11_MODULE(potentials, m) {
    m.def("lennard_jones", &lennardJones, R"pbdoc(LJ)pbdoc", py::arg("sig"), py::arg("eps"), py::arg("rc"), py::arg("r") );
    m.def("harmonic", &harmonic, R"pbdoc(HARM)pbdoc", py::arg("k"), py::arg("r"));
    m.def("zero", &zero, "ZERO", R"pbdoc(ZERO)pbdoc", py::arg("r"));

    #ifdef VERSION_INFO
        m.attr("__version__") = VERSION_INFO;
    #else
        m.attr("__version__") = "dev";
    #endif
}