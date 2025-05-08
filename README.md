# Natural product likeness score

The model is a derivation of the natural product fingerprint (eos6tg8). In addition to generating specific natural product fingerprints, the activation value of the neuron that predicts if a molecule is a natural product or not can be used as a NP-likeness score. The method outperforms the NP\_Score implemented in RDKit.

This model was incorporated on 2021-10-22.

## Information
### Identifiers
- **Ersilia Identifier:** `eos9yui`
- **Slug:** `natural-product-likeness`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Natural product`, `Drug-likeness`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Higher score indicates higher natural product likeness

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| np_score | float | high | Natural product likeness score |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos9yui](https://hub.docker.com/r/ersiliaos/eos9yui)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9yui.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9yui.zip)

### Resource Consumption
- **Model Size (Mb):** `63`
- **Environment Size (Mb):** `1529`
- **Image Size (Mb):** `1599.37`

**Computational Performance (seconds):**
- 10 inputs: `35.38`
- 100 inputs: `25.65`
- 10000 inputs: `532.36`

### References
- **Source Code**: [https://github.com/kochgroup/neural_npfp](https://github.com/kochgroup/neural_npfp)
- **Publication**: [https://www.sciencedirect.com/science/article/pii/S2001037021003226?](https://www.sciencedirect.com/science/article/pii/S2001037021003226?)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos9yui
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos9yui
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
