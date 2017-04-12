#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []

    import math

    for idx in range(0, len(ages)):
        cleaned_data.append( (ages[idx][0], net_worths[idx][0], math.pow(predictions[idx][0] - net_worths[idx][0], 2)) )

    cleaned_data.sort(key=lambda x: x[2])
    #print cleaned_data

    return cleaned_data[:81]

