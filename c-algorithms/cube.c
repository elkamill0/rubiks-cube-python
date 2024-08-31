#include </usr/include/python3.10/Python.h>
#define PY_SSIZE_T_CLEAN

// Define the Cube object structure
typedef struct {
    PyObject_HEAD
    PyObject *cube;
    PyObject *cube_backup;
} CubeObject;

// Method to initialize the Cube object
static int Cube_init(CubeObject *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"moves", NULL};
    char *moves = NULL;
    
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|s", kwlist, &moves)) {
        return -1;
    }

    // Create the initial cube list of lists
    PyObject *cube = PyList_New(6);
    if (cube == NULL) {
        return -1;
    }

    for (int i = 0; i < 6; ++i) {
        PyObject *face = PyList_New(9);
        if (face == NULL) {
            Py_DECREF(cube);
            return -1;
        }
        for (int j = 0; j < 9; ++j) {
            PyObject *num = PyLong_FromLong(j);
            if (num == NULL) {
                Py_DECREF(cube);
                Py_DECREF(face);
                return -1;
            }
            PyList_SET_ITEM(face, j, num);  // Steals reference to num
        }
        PyList_SET_ITEM(cube, i, face);  // Steals reference to face
    }

    self->cube = cube;

    // Create a deep copy of the cube list for backup
    self->cube_backup = PyList_GetSlice(cube, 0, 6);  // Create a shallow copy first
    if (self->cube_backup == NULL) {
        Py_DECREF(cube);
        return -1;
    }

    // Deep copy each sublist
    for (int i = 0; i < 6; ++i) {
        PyObject *face_copy = PyList_GetSlice(PyList_GET_ITEM(cube, i), 0, 9);
        if (face_copy == NULL) {
            Py_DECREF(cube);
            Py_DECREF(self->cube_backup);
            return -1;
        }
        PyList_SET_ITEM(self->cube_backup, i, face_copy);  // Steals reference to face_copy
    }

    return 0;
}

// Define the Cube type
static PyTypeObject CubeType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "cube.Cube",
    .tp_doc = "Cube object",
    .tp_basicsize = sizeof(CubeObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
    .tp_init = (initproc)Cube_init,
    .tp_dealloc = (destructor)PyObject_Del,
};

// Define module methods
static PyMethodDef cube_methods[] = {
    {NULL, NULL, 0, NULL}  // Sentinel
};

// Define the module
static struct PyModuleDef cubemodule = {
    PyModuleDef_HEAD_INIT,
    .m_name = "cube",
    .m_doc = "Example module that creates a Cube",
    .m_size = -1,
    .m_methods = cube_methods,
};

// Initialize the module
PyMODINIT_FUNC PyInit_cube(void) {
    PyObject *m;
    if (PyType_Ready(&CubeType) < 0)
        return NULL;

    m = PyModule_Create(&cubemodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&CubeType);
    if (PyModule_AddObject(m, "Cube", (PyObject *)&CubeType) < 0) {
        Py_DECREF(&CubeType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}


typedef struct {
    PyObject_HEAD;
    PyObject *cube;
    PyObject *cube_backup;
} CubeObject;

static int Cube(CubeObject *self, PyObject *args, PyObject *kwds){
    static char *kwlist[] = {"moves", NULL};
    char *moves = NULL;
}