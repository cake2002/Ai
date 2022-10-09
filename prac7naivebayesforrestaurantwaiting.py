#import operator
#data set => already taken for prediction
dataset = {
"Ans":             ["Yes","No"],
"Alternate":       ["Yes","No"],
"Bar":             ["No","Yes"],
"Fri/Sat":         ["Yes","No"],
"Hungry":          ["No","Yes"],
"Patrons":         ["Some","Full","None"],
"Price":           ["High","Low"],
"Raining":         ["Yes","No"],
"Reservation":     ["No","Yes"],
"Type":            ["French","Thai","Burger","Italian"],
"WaitEstimate":    ["10-30","0-10",">60","30-60"],
}

#input data to test or predict
test_case={
"Alternate":      "Yes",
"Bar":            "No",
"Fri/Sat":        "No",
"Hungry":         "Yes",
"Patrons":        "Full",
"Price":          "High",
"Raining":        "No",
"Reservation":    "No",
"Type":           "Thai",
"WaitEstimate":   "10-30"
}

def build_probs(ds, test_case):
    ans = ds["Ans"]#output attribute (ans)
    length = len(ans) #total length of output(ans)
    ans_set = set(ans) #unique (individual) classes yes and no
    count_ans = {k: ans.count(k) for k in ans_set}
    calc_prob = {k: count_ans[k] / length for k in ans_set}
    for ft in ds:
        if ft != "Ans":
            counts = {attr: {k: 0 for k in ans_set} for attr in set(ds[ft])}
            for i in range(length):
                counts[ds[ft][i]][ans[i]] +=1
            for k in ans_set:
                calc_prob[k] *= counts[test_case[ft]][k]/ count_ans[k]
    print(test_case,":\n",max(calc_prob, key=calc_prob.get))
build_probs(dataset, test_case)
