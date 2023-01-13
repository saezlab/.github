# Welcome to the github page of Saez Lab!

We are the [group of Julio Saez-Rodriguez][1], a research group at the
Heidelberg University Hospital. We develop software tools for systems level
analysis and mechanistic modeling of molecular and biomedical data.

Our goal is to acquire a functional understanding of the deregulation of
signalling networks in disease and to apply this knowledge to develop novel
therapeutics. We focus on cancer, auto-immune and fibrotic disease. Towards
this goal, we integrate big (‘omics’) data with mechanistic molecular knowledge
into statistical and machine learning methods. To this end, we have developed
a range of tools in different areas of biomedical research, mainly using the
programming languages R and Python.

## Databases

Database knowledge is essential for many of our methods, to this end we
maintain our own database called **[OmniPath][40],** combining data from about
150 original resources. **OmniPath** consists of a database builder Python
module (`pypath`), a public web service, and web service clients for R,
Python and Cytoscape. Read more about OmniPath in our [paper][41], and
check out the repos below.

* [`OmnipathR`: R client for the OmniPath web service][2]
* [Python client for the OmniPath web service][3]
* [Cytoscape client][42]
* [`pypath`: database builder Python module for OmniPath][5]
* [`BioCypher`: graph database (Neo4j) framework for molecular databases][4]
* [`DoRothEA`: a comprehensive gene regulatory network][9]

## Footprint methods

### Functional omics pipeline

We have a [comprehensive tutorial][19] presenting a typical functional omics
workflow. It uses footprint methods to infer transcription factor and pathway
activities from transcriptomics data, and uses causal reasoning to infer
the upstream pathways based on these activities.

### Functional omics web app

Our functional omics pipeline is also available as a web application called
**FUNKI.** Check out the [app here][27], find the code in the [git repo][28],
and read more in our [preprint][29].

### Pathway activities

**PROGENy** stands for Pathway RespOnsive GENe activity inference. It is a
footprint method to infer activities of canonical signaling pathways based
on gene expression data. Read more in the repos below and in our [paper][8].

* [R package][6]
* [Python module][7]

### Transcription factor activities

**DoRothEA** is a comprehensive gene regulatory network compiled from
literature, TF binding site prediction, ChIP-Seq and gene expression based
inference methods. It is also a footprint method to infer transcription factor
activities based on gene expression data, using the [VIPER algorithm][11].
Read more in our [paper][12] and in the repos below. DoRothEA data is also
available in OmniPath.

* [R package][9]
* [Python module][10]

### Functional signatures

**decoupleR** is a unified framework to extract functional signatures from
omics data. Read more in our [preprint][15].

* [R package][13]
* [Python module][14] (not yet public)

## Causality

### Causal reasoning

**CARNIVAL** uses causal reasoning to find the most plausible networks that
explain the activity patterns derived from omics data. See details in our
[paper][16].

* [R package][17]
* [CARNIPHAL][18]: R package for running CARNIVAL with phosphoproteomics data
* Python module: coming soon!

### Causal reasoning for multi-omics

**COSMOS** applies causal reasoning (using CARNIVAL) for the combined analysis
of multiple omics data: phosphoproteomics, transcriptomics and metabolomics.
See more in our [paper][24], the [video tutorial][25] and the repos below.

* [R package][26]

### Boolean modeling

**CellNOpt** creates predictive, mechanistic models of signaling networks
using logic formalisms (Boolean, fuzzy, or differential equations) based on
the combination of prior knowledge and omics data. Read our [paper][30] and
check out the [CellNOpt landing page][31] and the repos below.

* [R package][32]
* [Miscellaneous packages][33]

**PHONEMeS** trains Boolean models on phosphoproteomics data. See more in the
[PHONEMeS page][34], the papers ([ILP implementation][35], [original][36])
and the repo below.

* [R package, ILP implementation][37]
* [R package, original implementation][38]

## Intercellular and spatial signaling

### Ligand-receptor activities

**LIANA** is a framework combining a number of ligand-receptor database
resources with a number of methods to infer ligand-receptor activities from
single-cell transcriptomics data. More details in our [manuscript][20] and
the repos below.

* [R package][21]

### Intercellular spatial modeling

**MISTy** leverages on explainable machine learning to find relationships
between the expression of various markers across a number of spatial contexts
(views; e.g. intrinsic, juxtacrine, paracrine). Read more in our
[preprint][22] and the repos below.

* [R package][23]

## Metabolomics

### Enzyme enrichment analysis

The enzyme enrichment analysis is a footprint method for inferring enzyme
activities from metabolomics data. It is implemented in the **OCEAN** package.

* [R package][39]

[1]: https://saezlab.org/
[2]: https://github.com/saezlab/OmnipathR
[3]: https://github.com/saezlab/omnipath
[4]: https://github.com/saezlab/BioCypher
[5]: https://github.com/saezlab/pypath
[6]: https://github.com/saezlab/progeny
[7]: https://github.com/saezlab/progeny-py
[8]: https://www.nature.com/articles/s41467-017-02391-6
[9]: https://github.com/saezlab/dorothea
[10]: https://github.com/saezlab/dorothea-py
[11]: https://www.nature.com/articles/ng.3593
[12]: https://doi.org/10.1101/gr.240663.118
[13]: https://github.com/saezlab/decoupleR
[14]: https://github.com/saezlab/decoupler-py
[15]: https://doi.org/10.1101/2021.11.04.467271
[16]: https://www.nature.com/articles/s41540-019-0118-z
[17]: https://github.com/saezlab/CARNIVAL
[18]: https://github.com/saezlab/CARNIPHAL
[19]: https://github.com/saezlab/transcriptutorial
[20]: https://www.nature.com/articles/s41467-022-30755-0
[21]: https://github.com/saezlab/liana
[22]: https://doi.org/10.1101/2020.05.08.084145
[23]: https://github.com/saezlab/mistyR
[24]: https://www.embopress.org/doi/full/10.15252/msb.20209730
[25]: https://embl-ebi.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=318f7091-b6bf-44ee-939f-adb10121fc1b
[26]: https://github.com/saezlab/cosmosR
[27]: https://saezlab.github.io/ShinyFUNKI/
[28]: https://github.com/saezlab/ShinyFUNKI
[29]: https://arxiv.org/abs/2109.05796
[30]: https://academic.oup.com/bioinformatics/article/36/16/4523/5855133
[31]: https://saezlab.github.io/CellNOptR/
[32]: https://github.com/saezlab/CellNOptR
[33]: https://github.com/saezlab/cellnopt
[34]: https://saezlab.github.io/PHONEMeS/
[35]: https://pubs.acs.org/doi/full/10.1021/acs.jproteome.0c00958
[36]: http://www.nature.com/articles/ncomms9033
[37]: https://github.com/saezlab/PHONEMeS-ILP
[38]: https://github.com/saezlab/PHONEMeS
[39]: https://github.com/saezlab/ocean
[40]: https://omnipathdb.org/
[41]: http://europepmc.org/abstract/MED/33749993
[42]: https://apps.cytoscape.org/apps/omnipath
