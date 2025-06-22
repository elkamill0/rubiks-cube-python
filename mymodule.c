#include <Python.h>

// Definicja funkcji add(a, b)
static PyObject* mymodule_add(PyObject* self, PyObject* args) {
    int a, b;
    // Parsujemy argumenty: oczekujemy dwóch intów
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;  // jeśli błędne argumenty, zwracamy NULL (wyjątek)
    }
    int result = a + b;
    // Zwracamy wynik jako Pythonowy int
    return PyLong_FromLong(result);
}

// Definicja metod modułu
static PyMethodDef MyModuleMethods[] = {
    {"add", mymodule_add, METH_VARARGS, "Add two integers"},
    {NULL, NULL, 0, NULL}
};

// Definicja modułu
static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "mymodule",    // nazwa modułu
    "Example module that adds two numbers",  // dokumentacja modułu
    -1,
    MyModuleMethods
};

// Funkcja inicjująca moduł
PyMODINIT_FUNC PyInit_mymodule(void) {
    return PyModule_Create(&mymodule);
}
