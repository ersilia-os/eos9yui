# Natural product likeness score

Scores how strongly a molecule resembles a natural product, using the activation of the output neuron in a network trained to distinguish natural from synthetic chemistry. Menke and co-workers reported that this learned score outperforms the NP-likeness score implemented in RDKit, which relies on fragment frequency statistics rather than a trained model. Higher values indicate closer resemblance to natural product chemical space, a property associated with structural complexity and biological relevance.

This model was incorporated on 2021-10-22.Last packaged on 2025-09-15.

## Information
### Identifiers
- **Ersilia Identifier:** `eos9yui`
- **Slug:** `natural-product-likeness`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Natural product`, `Drug-likeness`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Natural product likeness score where higher values indicate closer resemblance to natural products.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| np_score | float | high | Natural product likeness score |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos9yui](https://hub.docker.com/r/ersiliaos/eos9yui)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9yui.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9yui.zip)

### Resource Consumption
- **Model Size (Mb):** `63`
- **Environment Size (Mb):** `1548`
- **Image Size (Mb):** `1622.5`

**Computational Performance (seconds):**
- 10 inputs: `29.03`
- 100 inputs: `19.16`
- 10000 inputs: `145.26`

### References
- **Source Code**: [https://github.com/kochgroup/neural_npfp](https://github.com/kochgroup/neural_npfp)
- **Publication**: [https://doi.org/10.1016/j.csbj.2021.07.032](https://doi.org/10.1016/j.csbj.2021.07.032)
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
