# begin installing miniconda
if [[ "$TRAVIS_OS_NAME" != "windows" ]]; then
  echo "installing miniconda for posix";
  bash $HOME/download/miniconda.sh -b -u -p $MINICONDA_PATH;
elif  [[ "$TRAVIS_OS_NAME" == "windows" ]]; then
  echo "folder $MINICONDA_SUB_PATH does not exist"
  echo "installing miniconda for windows";
  choco install miniconda3 --params="'/JustMe /AddToPath:1 /D:$MINICONDA_PATH_WIN'";
fi;

# end installing miniconda
export PATH="$MINICONDA_PATH:$MINICONDA_SUB_PATH:$MINICONDA_LIB_BIN_PATH:$PATH";

# begin checking miniconda existance
echo "checking if folder $MINICONDA_SUB_PATH exists"
if [[ -d $MINICONDA_SUB_PATH ]]; then
  echo "folder $MINICONDA_SUB_PATH exists"
else
  echo "folder $MINICONDA_SUB_PATH does not exist"
fi;

# end checking miniconda existance
source $MINICONDA_PATH/etc/profile.d/conda.sh;
hash -r;
echo $TRAVIS_OS_NAME
echo $CONDA_PYTHON
python --version
conda config --set always_yes yes --set changeps1 no;
conda update -q conda;

# Useful for debugging any issues with conda
conda info -a
  
# See if test-environment already available
# As necessary, apply python module recipies
echo "create test-environment";
conda env create -n test-environment -f ./ci/environment.yml;
conda activate test-environment
conda install pytest
if  [[ "$TRAVIS_OS_NAME" == "windows" ]]; then
  conda install libpython m2w64-toolchain -c msys2;
elif [[ "$TRAVIS_OS_NAME" == "osx"]]; then
  conda install clang_osx-64;
else
  conda install gxx_linux-64
fi;
conda list
pip install . -vvv
pip install cibuildwheel