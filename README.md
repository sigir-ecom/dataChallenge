# DataChallenge
Repository for dataChallenge related scripts of Rakuten data challenge: https://sigir-ecom.github.io/data-task.html
Please sign up [here](https://docs.google.com/forms/d/e/1FAIpQLSdho-e_mpde6-j4CJPW7xhNbr_K98N7Y9sAXxPZULJwRK6tOg/viewform?c=0&w=1).

# Evaluation script
The final evaluation metrics will be weighted-{precision, recall, F1} ([reference](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html)) on the test set of _EXACT_ CeategoryIdPath match. Since the product distribution over the taxonomy tree is highly imbalanced, weighted-{precision, recall, F1} make much more sense than macro- or micro- {precision, recall, F1} do. Please note that partial path match does not count as a correct prediction. Evaluation script is provided [here](eval.py) and the usage is shown below. Both PREDCITION\_FILE and GOLD\_FILE must be in the same tsv format as the training file where the first column is product title and the second column is CeategoryIdPath. The title order must be the same in both files.
```
$ python eval.py -pred $PREDCITION_FILE -gold $GOLD_FILE
```




