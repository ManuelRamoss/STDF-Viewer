sudo yum install git


git clone https://nxp-cce@dev.azure.com/nxp-cce/EBI/_git/EDM-Infra

43r62l5fm6ua2tus4smu3pflthdfo3uzcrxwj3u5wlurt2cmm4vq

git clone https://github.com/ManuelRamoss/STDF-Viewer.git

cd STDF-Viewer

sudo yum install gcc openssl-devel bzip2-devel libffi-devel 

pip install -r requirements.txt

sudo yum install python3-devel

python -m pip install cython==3.0a6

cd ./deps/cystdf

python cystdf_amalgamation_setup.py build_ext --inplace


python -c "import os, PyInstaller; \
          qthook=os.path.join(os.path.dirname(PyInstaller.__file__), 'utils', 'hooks', 'qt.py'); \
          rthooks=os.path.join(os.path.dirname(PyInstaller.__file__), 'hooks', 'rthooks.dat'); \
          qtpatchpath=os.path.join('.github', 'workflows', 'qt.py.patch'); \
          rthookpatchpath=os.path.join('.github', 'workflows', 'rthooks.dat.patch'); \
          command1='patch -u '+qthook+' '+qtpatchpath; \
          command2='patch -u '+rthooks+' '+rthookpatchpath; \
          os.system(command1); \
          os.system(command2); \
          print(command1); print(command2)"

cd ../..

python build_tools/removePyinstallerHooks.py

pip install numpy==1.17.2

python -m PyInstaller build_tools/linux.spec


                                                                                                                                          3,1           All
import _cystdf

stdfRecordAnalyzer('test_stdf.stdf.gz',None,None,None)




import _cystdf
import sys

atdf=_cystdf.analyzeSTDF(sys.argv[1],None,None,None)
print(atdf)






"analize.py" 12L, 187B                                                                                                                                                                    9,22          All
import _cystdf
import sys

class stdfProps(object):
    filepath_c = ''

props = stdfProps()
props.filepath_c=sys.argv[1]
print(props.filepath_c)
atdf=_cystdf.analyze(props)
print(atdf)




************************* Install Python 3.9 ************************

cd /opt 
sudo yum install libffi-devel
sudo wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz 
sudo tar xzf Python-3.9.6.tgz 

cd Python-3.9.6 
sudo ./configure --enable-optimizations 
sudo make altinstall

sudo rm -f /opt/Python-3.9.6.tgz 
