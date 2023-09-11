include <Python.h>
/**
 * print_python_list_info - A function that prints basic info
 * about Python lists.
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int sz, allc, itr;
	PyObject *object;

	sz = Py_SIZE(p);
	allc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", sz);
	printf("[*] Allocated = %d\n", allc);

	for (itr = 0; itr < sz; itr++)
	{
		printf("Element %d: ", itr);

		object = PyList_GetItem(p, itr);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
