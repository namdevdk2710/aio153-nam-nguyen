def classification_model(tp: int, fp: int, fn: int):
    if not isinstance(tp, int):
        print("tp must be int")
        return

    if not isinstance(fp, int):
        print("fp must be int")
        return

    if not isinstance(fn, int):
        print("fn must be int")
        return
    
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return
    
    precision = tp / (tp + fp)
    recal = tp / (tp + fn)
    f1_score = 2 * (precision * recal) / (precision + recal)
    
    print("Precision is ", precision)
    print("Recall is ", recal)
    print("F1-score is ", f1_score)


classification_model(tp=2, fp=3, fn=4)
print("=====================================")
classification_model(tp='a', fp=3, fn=4)
print("=====================================")
classification_model(tp=2, fp='a', fn=4)
print("=====================================")
classification_model(tp=2, fp=3, fn='a')
print("=====================================")
classification_model(tp=2.1, fp=3, fn=4)
print("=====================================")
classification_model(tp=0, fp=3, fn=4)
