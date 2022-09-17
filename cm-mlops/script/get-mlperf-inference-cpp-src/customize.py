from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']
    source_files = []
    script_path = i['run_script_input']['path']
    env['CM_SOURCE_FOLDER_PATH'] = os.path.join(script_path, "src")
    for file in os.listdir(env['CM_SOURCE_FOLDER_PATH']):
        if file.endswith(".c") or file.endswith(".cpp"):
            source_files.append(file)
    env['CM_CXX_SOURCE_FILES'] = ";".join(source_files)
    if '+CXX_INCLUDE_PATH' not in env:
        env['+CXX_INCLUDE_PATH']  = []
    env['+CXX_INCLUDE_PATH'].append(os.path.join(script_path, "inc")) 
    env['+C_INCLUDE_PATH'].append(os.path.join(script_path, "inc"))
    if '+ CXXFLAGS' not in env:
        env['+ CXXFLAGS'] = []
    env['+ CXXFLAGS'].append("-std=c++14")
    if '+ LDCXXFLAGS' not in env:
        env['+ LDCXXFLAGS'] = [ ]
    env['+ LDCXXFLAGS'] += [ "-lmlperf_loadgen", "-lonnxruntime" ]
    env['CM_LINKER_LANG'] = 'CXX'
    env['CM_RUN_DIR'] = os.getcwd()

    return {'return':0}

def postprocess(i):

    env = i['env']
    return {'return':0}