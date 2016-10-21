def get_attribute(data, attribute_name):
    header = data[0]
    idx = header.index(attribute_name)
    return [record[idx] for record in data[1:]]


def to_float(attribute_list):
    return list(map(float, attribute_list))