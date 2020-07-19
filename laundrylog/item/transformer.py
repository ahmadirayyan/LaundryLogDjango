def transform(values):
    arr = []

    for item in values:
        arr.append(singleTransform(item))

    return arr

def singleTransform(values):
    return {
        'id': values.id,
        'category': values.category,
        'color': values.color,
        'brand': values.brand,
        'price': values.price,
        'desc': values.desc,
        'status': values.status,
        'datebought': str(values.datebought),
        'created_at': str(values.created_at),
        'updated_at': str(values.updated_at)
    }