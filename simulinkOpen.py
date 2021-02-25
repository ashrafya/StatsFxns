import os.path
import matlab.engine
import subprocess


def openSLX(filename, path = ''):
    '''
    (str, str) --> simulink file obejct opened
    filename = the filename
    path = path of the file if not in the same directory    
           - path object set to empty srting initially for same directory
           
    als need to check if path exists first or not
    '''
    # merging the path
    file_to_open = os.path.join(path, filename)
    
    if not os.path.exists(file_to_open):
        print('False')
        raise ModuleNotFoundError('path does not exist')
    
    # using matlab engine to open slx file
    eng = matlab.engine.start_matlab()
    eng.load_system(file_to_open, nargout=0)
    eng.load_system(file_to_open)
    eng.sim(file_to_open)
    eng.close_system(file_to_open, nargout=0) # closing system
    return None
    
# have to defing the filename and filepath (if not in the same directory) in the main function
if __name__ == "__main__":
    filename = 'MCity_RoadObstacle.slx'
    path = 'D:\PL-0-2'
    openSLX(filename, path)
