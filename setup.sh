source .venv/bin/activate
python -m build .
pip uninstall git-compose -y
pip install dist/*.whl
git-compose --version
