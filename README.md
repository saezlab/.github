<p align="center">
  <img src="https://github.com/saezlab/ali_saezlab.org/blob/e27b9a9a92788580e3698688f4f07eadec9e2849/assets/images/julio-logo.png" alt="lab logo"/>
</p>

# Welcome to the github page of the Saez Lab!

We are the [group of Julio Saez-Rodriguez][1], a research group at the
Heidelberg University Hospital. We develop software tools for systems level
analysis and mechanistic modeling of molecular and biomedical data.

Our goal is to acquire a functional understanding of the deregulation of
signalling networks in disease and to apply this knowledge to develop novel
therapeutics. We focus on cancer, auto-immune and fibrotic disease. Towards
this goal, we integrate big (‘Omics’) data with mechanistic molecular knowledge
into statistical and machine learning methods. To this end, we have developed
a range of tools in different areas of biomedical research, mainly using the
programming languages R and Python.

## Databases

* [`OmnipathR`: R client for the OmniPath web service][2]
* [Python client for the OmniPath web service][3]
* [`pypath`: database builder Python module for OmniPath][4]
* [`BioCypher`: graph database (Neo4j) framework for molecular databases][5]
* [`DoRothEA`: a comprehensive gene regulatory network][9]

## Footprint methods

### Functional omics tutorial

We have a [comprehensive tutorial][19] for a typical functional omics workflow.
It uses footprint methods to infer transcription factor and pathway
activities from transcriptomics data, and uses causal reasoning to infer
the upstream pathways based on these activities.

### Functional omics web app

Our functional omics pipeline is also available as a web application called
FUNKI. Check out the [app here][27], find the code in the [git repo][28],
and read more in our [preprint][29].

### PROGENy

PROGENy stands for Pathway RespOnsive GENe activity inference. It is a
footprint method to infer activities of canonical signaling pathways based
on gene expression data. Read more in the repos below and in our [paper][8].

* [R package][6]
* [Python module][7]

### DoRothEA

DoRothEA is a comprehensive gene regulatory network compiled from literature,
TF binding site prediction, ChIP-Seq and gene expression based inference
methods. It is also a footprint method to infer transcription factor
activities based on gene expression data, using the [VIPER algorithm][11].
Read more in our [paper][12] and in the repos below. DoRothEA data is also
available in OmniPath.

* [R package][9]
* [Python module][10]

### decouplR

decouplR is a unified framework to extract functional signatures from omics
data. Read more in our [preprint][15].

* [R package][13]
* [Python module][14] (not yet public)

## Causality

### CARNIVAL

CARNIVAL uses causal reasoning to find the most plausible networks that
explain the activity patterns derived from omics data. See details in our
[paper][16].

* [R package][17]
* [CARNIPHAL][18]: R package for running CARNIVAL with phosphoproteomics data
* Python module: coming soon!

### COSMOS

COSMOS applies causal reasoning (using CARNIVAL) for the combined analysis
of multiple omics data: phosphoproteomics, transcriptomics and metabolomics.
See more in our [paper][24], the [video tutorial][25] and the repos below.

* [R package][26]

### Boolean modeling

CellNOpt creates predictive, mechanistic models of signaling networks using
logic formalisms (Boolean, fuzzy, or differential equations) based on the
combination of prior knowledge and omics data. Read our [paper][30] and
check out the [CellNOpt landing page][31] and the repos below.

* [R package][32]
* [Miscellaneous packages][33]

PHONEMeS train Boolean models on phosphoproteomics data. See more in the
[PHONEMeS page][34], the papers ([ILP implementation][35], [original][36])
and the repo below.

* [R package, ILP implementation][37]
* [R package, original implementation][38]

## Intercellular and spatial signaling

### LIANA

LIANA is a framework combining a number of ligand-receptor database
resources with a number of methods to infer ligand-receptor activities from
single-cell transcriptomics data. More details in our [preprint][20] and
the repos below.

* [R package][21]

### MISTy

MISTy leverages on explainable machine learning to find relationships between
the expression of various markers across a number of spatial contexts (views;
e.g. intrinsic, juxtacrine, paracrine). Read more in our [preprint][22] and
the repos below.

* [R package][23]

## Metabolomics

### Enzyme enrichment analysis

The enzyme enrichment analysis is a footprint method for inferring enzyme
activities from metabolomics data. It is implemented in the OCEAN package.

* [R package][39]

[1]: https://saezlab.org/
[2]: /OmnipathR
[3]: /omnipath
[4]: /BioCypher
[5]: /pypath
[6]: /progeny
[7]: /progeny-py
[8]: https://www.nature.com/articles/s41467-017-02391-6
[9]: /dorothea
[10]: /dorothea-py
[11]: https://www.nature.com/articles/ng.3593
[12]: https://doi.org/10.1101/gr.240663.118
[13]: /decouplR
[14]: /decoupler-py
[15]: https://doi.org/10.1101/2021.11.04.467271
[16]: https://www.nature.com/articles/s41540-019-0118-z
[17]: /CARNIVAL
[18]: /CARNIPHAL
[19]: /transcriptutorial
[20]: https://www.biorxiv.org/content/10.1101/2021.05.21.445160v1
[21]: /liana
[22]: https://doi.org/10.1101/2020.05.08.084145
[23]: /mistyR
[24]: https://www.embopress.org/doi/full/10.15252/msb.20209730
[25]: https://embl-ebi.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=318f7091-b6bf-44ee-939f-adb10121fc1b
[26]: /cosmosR
[27]: https://saezlab.github.io/ShinyFUNKI/
[28]: /ShinyFUNKI
[29]: https://arxiv.org/abs/2109.05796
[30]: https://academic.oup.com/bioinformatics/article/36/16/4523/5855133
[31]: https://saezlab.github.io/CellNOptR/
[32]: /CellNOptR
[33]: /cellnopt
[34]: https://saezlab.github.io/PHONEMeS/
[35]: https://pubs.acs.org/doi/full/10.1021/acs.jproteome.0c00958
[36]: http://www.nature.com/articles/ncomms9033
[37]: /PHONEMeS-ILP
[38]: /PHONEMeS
[39]: /ocean
