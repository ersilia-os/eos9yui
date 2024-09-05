# imports
import os
import csv
import sys
import yaml

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
from neural_npfp.model import *
from neural_npfp.utils import *

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

data = pd.DataFrame({"smiles":smiles_list})

model_paths = os.path.dirname(os.path.join(root,"data/trained_models/npl_nonorm_64/"))
settings = yaml.safe_load(open(os.path.join(model_paths,"settings.yml"), "r"))
ecfp4,index_error=get_fingerprints_user(data, label=0)


model = MLP(settings["aux_model"]["layers"],1 ,settings["aux_model"]["dropout"])
model.load_state_dict(torch.load(os.path.join(model_paths,"aux_cv0.pt"), map_location=torch.device('cpu')))
model.eval()

_, npl, nnfp = model(torch.tensor(ecfp4.values, dtype= torch.float))
nnfp = nnfp.detach().clone().numpy()
nnfp[index_error,:] = np.nan
nnfp = pd.DataFrame(nnfp)

npl = npl[:,[0]].detach().clone().numpy()
npl[index_error,:] = np.nan
outputs = npl.flatten().tolist()

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["np_score"])  # header
    for o in outputs:
        writer.writerow([o])