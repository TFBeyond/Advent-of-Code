from pathlib import Path
import inspect



def getAoCInput(*args):
 
    if len(args) == 0:
        calling_filename = inspect.stack()[1].filename
    else: calling_filename = args[0]

    this_day_input = "{}_input.txt".format("_".join(Path(calling_filename).stem.split('_')[:-1]))
    path = (Path(__file__).parent / "../Inputs"  / this_day_input).resolve()
    input = path.open()
    return(input)

def getSplitAoCInput(split_on=' '):
    calling_filename = inspect.stack()[1].filename
    lines = []
    input = getAoCInput(calling_filename)
    lines = [line.strip().split(split_on) for line in input]
    return(lines)
    
    