# Natural product likeness score

The model is a derivation of the natural product fingerprint (eos6tg8). In addition to generating specific natural product fingerprints, the activation value of the neuron that predicts if a molecule is a natural product or not can be used as a NP-likeness score. The method outperforms the NP\_Score implemented in RDKit.

## Identifiers

* EOS model ID: `eos9yui`
* Slug: `natural-product-likeness`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Regression`
* Output: `Score`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Higher score indicates higher natural product likeness

## References

* [Publication](https://www.sciencedirect.com/science/article/pii/S2001037021003226?)
* [Source Code](https://github.com/kochgroup/neural_npfp)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos9yui)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9yui.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos9yui) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://www.sciencedirect.com/science/article/pii/S2001037021003226?) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!