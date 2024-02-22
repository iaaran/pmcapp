def convert(feet, inches):
    meters = round((feet * 0.3048 + inches * 0.0254), 2)
    return meters
