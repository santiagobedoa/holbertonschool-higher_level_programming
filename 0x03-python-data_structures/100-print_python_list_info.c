#include <Python.h>

/**
 * print_python_list_info - function that prints python lists info
 * @p: pointer to PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = Py_SIZE(p);
	Py_ssize_t i = 0;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (; i < size; i++)
	{
		printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
