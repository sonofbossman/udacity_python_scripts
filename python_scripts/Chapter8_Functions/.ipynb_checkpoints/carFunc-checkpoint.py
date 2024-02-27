def make_car(manufacturer, model, **features):
    features["Manufacturer"] = manufacturer
    features["Model"] = model
    return features