@echo off

REM Create directories
mkdir src\matrix_operations src\vector_operations src\utils
mkdir tests\test_matrix_operations tests\test_vector_operations
mkdir docs

REM Create files in src
echo. > src\__init__.py
echo. > src\matrix_operations\__init__.py
echo. > src\matrix_operations\addition.py
echo. > src\matrix_operations\multiplication.py
echo. > src\matrix_operations\inverse.py

echo. > src\vector_operations\__init__.py
echo. > src\vector_operations\dot_product.py
echo. > src\vector_operations\cross_product.py

echo. > src\utils\__init__.py
echo. > src\utils\helpers.py

REM Create files in tests
echo. > tests\__init__.py
echo. > tests\test_matrix_operations\__init__.py
echo. > tests\test_matrix_operations\test_addition.py
echo. > tests\test_matrix_operations\test_multiplication.py
echo. > tests\test_matrix_operations\test_inverse.py

echo. > tests\test_vector_operations\__init__.py
echo. > tests\test_vector_operations\test_dot_product.py
echo. > tests\test_vector_operations\test_cross_product.py

REM Create README in docs
echo. > docs\README.md

echo Setup completed successfully.