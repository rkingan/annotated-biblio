# annotated-biblio
Notes on papers

## Benchmarking Nearest Neighbor Search: Influence of Local Intrinsic Dimensionality and Result Diversity in Real-World Datasets

* *Authors:* Martin Aum¨uller and Matteo Ceccarello
* *Link:* https://imada.sdu.dk/Research/EDML/EDML19_paper_3.pdf
* *Annotated Copy:* [EDML19_paper_3_annotated.pdf](EDML19_paper_3_annotated.pdf)
* *Date read:* 31 March 2021
* *Keywords:* KNN, LID, search

### Summary

* The authors explore the relationship between local intrinsic dimensionality (LID) of query points and performance for several different approximate *k*-nearest neighbor (ANN) algorithms.

* They find that while ANNOY underperforms the graph-based methods, the graph-based methods also require a more subtle examination of their QPS vs. recall characteristics. In particular, while recall gradually shifts from 0 to 1 as QPS decreases for ANNOY, for the graph-based methods recall abruptly shifts from 0 to 1.

### Future reading and experiments

* To read: Source papers on LID and ONNG, the highest performing graph-based method

* Experiment: Try generating some toy data with different intrinsic and expressed dimensionalities and see how the LID values turn out.

## Judgment Prediction via Injecting Legal Knowledge into Neural Networks

* *Authors:* Leilei Gan, Kun Kuang, Yi Yang and Fei Wu
* *Link:* https://www.aaai.org/AAAI21Papers/AAAI-7838.GanL.pdf
* *Annotated Copy:* [AAAI-7838.GanL-annotated.pdf](AAAI-7838.GanL-annotated.pdf)
* *Date read:* 16 April 2021
* *Keywords:* NN, legal, logic

### Summary

* The authors develop a model for predicting legal judgements from expressions
  of facts and complaints that combines a neural network, specifically word
  embeddings and an LSTM, and first-order logic to predict a judge's decision
  given a specific set of facts and complaints.

* The experiment they did is extremely limited, restricted to one very specific
  area of law with easy to encode rules. Also, the authors are vague about how
  specifically they tie their logical rules to specific nodes from the neural
  network.

## Using Text Analytics to Predict Litigation Outcomes: A Preliminary Assessment

* *Authors:* Alexander, Charlotte and Al Jadda, Khalifeh and Feizollahi, Mohammed Javad and Tucker, Anne M.
* *Link:* https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3230224
* *Annotated copy:* [SSRN-id3230224-annotated.pdf](SSRN-id3230224-annotated.pdf)
* *Date read:* 16 April 2021
* *Keywords:* legal, NLP

### Summary

* The authors describe the process of data acquisition, data preprocessing and
  preliminary model training for a project to try to predict the outcome of a
  court case using information available at various stages. They use PACER data
  for 5111 cases from the U.S. District Court for the Northern District of
  Georgia. 

* The paper does not describe any very novel techniques for modeling case
  outcomes, and is a preliminary report. It does, however, contain a wealth of
  background information on things like the reliability of NOS cand cause of
  action codes on Federal dockets, the content of the various different data
  artifacts associated with a Federal case, and the role of magistrate judges in
  determining things like the outcome of motions for summary judgement.

## Revisiting k-means: New Algorithms via Bayesian Nonparametrics

* *Authors:* Kulis, Brian and Jordan, Michael I.
* *Link:* https://icml.cc/2012/papers/291.pdf
* *Annotated copy:* [291-annotated.pdf](291-annotated.pdf)
* *Date read:* 23 April 2021
* *Keywords:* clustering, bayesian, k-means

### Summary

The authors show how k-means clustering can be reinterpreted as the asymptotic
limit of a Gaussian mixture problem. They then extend the approach to a novel
algorithm that adjusts the number of clusters as it proceeds. They also develop
an algorithm that can share clusters across a family of related data sets. They
evaluate their methods on published and synthetic data sets.

## Text Summarization Techniques: A Brief Survey

* *Authors:* Mehdi Allahyari, Seyedamin Pouriyehy, Mehdi Assefiy, Saeid Safaeiy, Elizabeth D. Trippez,
Juan B. Gutierrezz, Krys Kochut
* *Link:* https://thesai.org/Downloads/Volume8No10/Paper_52-Text_Summarization_Techniques_a_Brief_Survey.pdf
* *Annotated copy:* [Paper_52-Text_Summarization_Techniques_a_Brief_Survey-annotated.pdf](Paper_52-Text_Summarization_Techniques_a_Brief_Survey-annotated.pdf)
* *Date read:* 14 May 2021
* *Keywords:* NLP, summarization

### Summary
The authors break down the process of generating extractive summaries of text, and describe different approaches to each of the component steps. The paper was published in 2017 and therefore predates some of the more recent work using transformer models, but it does provide a good overview, with a balance of supervised and unsupervised techniques described.
